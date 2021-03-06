import telebot
import config
import datetime
import utils
import markups
import messages
import qr
import os
from dbQuery import Query
import cherrypy


db = Query()
bot = telebot.TeleBot(config.token)
# bot_name = telebot.TeleBot(config.bot_name)


# Начало диалога.
@bot.message_handler(commands=["start"])
def cmd_start(message):
    user_valid = utils.validate_state(db, message)  # Проверяем состояние пользователя
    bot.send_message(message.chat.id, user_valid[0], reply_markup=user_valid[1])


# Ловим имя
@bot.message_handler(func=lambda message: utils.validate_state2(db, message.chat.id, utils.States.S_ENTER_NAME.value))
def user_entering_name(message):
    bot.send_message(message.chat.id, messages.s_phone, reply_markup=markups.keyboardPhone)
    db.add_user_name(message.chat.id, message.text)  # Добавляем имя в базу


# Ловим номер телефона
@bot.message_handler(content_types=["contact"])
def read_contact_data(message):
    if message.from_user.id != message.contact.user_id:
        bot.send_message(message.chat.id, messages.s_phone_error, reply_markup=markups.keyboardPhone)
        return
    else:
        bot.send_message(message.chat.id, messages.s_birth, reply_markup=markups.hide_markup)
        db.add_user_phone(message.chat.id, message.contact.phone_number)  # Добавляем телефон в базу


# Ловим дату рождения
@bot.message_handler(func=lambda message: utils.validate_state2(db, message.chat.id, utils.States.S_BIRTHDAY.value))
def user_entering_birthday(message):
    # Проверка на дату
    if utils.validate_date(message.text):
        bot.send_message(message.chat.id, messages.s_birth_error)
        return
    birthday = utils.convert_date(message.text)
    current_date = datetime.datetime.now()

    if (current_date.year - birthday.year) > 100 or (current_date.year - birthday.year) < 2:
        bot.send_message(message.chat.id, messages.s_birth_cheat)
        return
    else:
        # Дата рождения введена корректно, можно идти дальше
        db.add_user_birth(message.chat.id, birthday)  # Добавляем ДР в базу
        utils.validate_ref(db, bot, message.chat.id)  # Дарим подарок
        bot.send_message(message.chat.id, messages.s_menu, reply_markup=markups.keyboardMain)


@bot.message_handler(commands=["Подарки"])
def gifts(message):
    if utils.validate_state2(db, message.chat.id, utils.States.S_MENU.value):
        gifts_list = utils.get_users_gifts(db, message.chat.id)
        bot.send_message(message.chat.id, messages.s_gifts, reply_markup=markups.keyboardMain)

        for i in gifts_list:
            msg = f"Название: {i['name']}. Статус: {i['status']}"
            bot.send_message(message.chat.id, msg, reply_markup=markups.keyboardMain)

        # bot.send_message(message.chat.id, messages.s_gifts + utils.get_users_gifts(bd, message.chat.id),
        # reply_markup=markups.keyboardMain)


@bot.message_handler(commands=["Пригласить_друга"])
def invite_friend(message):
    if utils.validate_state2(db, message.chat.id, utils.States.S_MENU.value):
        user_id = str(message.chat.id)
        # bot_name = 'vlgTest1Bot'
        # bot_name = telebot.TeleBot(config.bot_name)
        img_name = f'qr-{user_id}'
        tmp_path = 'tmp/'
        link = f'https://telegram.me/nextkz_bot?start={user_id}'
        qr.createQR(tmp_path, img_name, link)
        bot.send_message(message.chat.id, messages.s_qr, reply_markup=markups.keyboardMain)
        bot.send_photo(message.chat.id, open(f'{tmp_path}{img_name}.png', 'rb'), reply_markup=markups.keyboardMain)
        os.remove(f'{tmp_path}{img_name}.png')
        bot.send_message(message.chat.id, link, reply_markup=markups.keyboardMain)


@bot.message_handler(content_types=["text"])
def something_wrong(message):
    bot.send_message(message.chat.id, messages.s_text, reply_markup=markups.keyboardMain)


# --------

WEBHOOK_HOST = '54.186.203.196'     # используемый ip сервера
WEBHOOK_PORT = 443               # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'   # На некоторых серверах придется указывать такой же IP, что и выше
WEBHOOK_SSL_CERT = 'ssl/webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = 'ssl/webhook_pkey.pem'  # Путь к приватному ключу
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % config.token


# Наш вебхук-сервер
class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            # Эта функция обеспечивает проверку входящего сообщения
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)
# -----------------


if __name__ == '__main__':
    bot.remove_webhook()
    # bot.polling(none_stop=True)

    # Снимаем вебхук перед повторной установкой (избавляет от некоторых проблем)

    # Ставим заново вебхук
    bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH, certificate=open(WEBHOOK_SSL_CERT, 'r'))

    # Указываем настройки сервера CherryPy
    cherrypy.config.update({
        'server.socket_host': WEBHOOK_LISTEN,
        'server.socket_port': WEBHOOK_PORT,
        'server.ssl_module': 'builtin',
        'server.ssl_certificate': WEBHOOK_SSL_CERT,
        'server.ssl_private_key': WEBHOOK_SSL_PRIV
    })

     # Собственно, запуск!
    cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})

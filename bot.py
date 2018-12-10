import telebot
import config
import dbworker
import datetime
import utils
import markups
import messages
import qr
import os
from dbQuery import Query



bd = Query()
bot = telebot.TeleBot(config.token)
bot_name = telebot.TeleBot(config.bot_name)

# Дописать проверку на ДР


# Начало диалога
@bot.message_handler(commands=["start"])
def cmd_start(message):
    # Проверяем текущее состояние пользователя и отправляем ему соответствующее сообщение
    user_valid = utils.validate_state(bd, message)
    bot.send_message(message.chat.id, user_valid[0], reply_markup=user_valid[1])


# Ловим имя
@bot.message_handler(func=lambda message: utils.validate_state2(message.chat.id, utils.States.S_ENTER_NAME.value))
def user_entering_name(message):
    bot.send_message(message.chat.id, messages.s_phone, reply_markup=markups.keyboardPhone)
    dbworker.set_state(message.chat.id, utils.States.S_PHONE.value)  # Меняем состояние
    bd.addUserName(message.chat.id, message.text)  # Добавляем имя в базу


# Ловим номер телефона
@bot.message_handler(content_types=["contact"])
def read_contact_data(message):
    if message.from_user.id != message.contact.user_id:
        bot.send_message(message.chat.id, messages.s_phone_error, reply_markup=markups.keyboardPhone)
        return
    else:
        bot.send_message(message.chat.id, messages.s_birth, reply_markup=markups.hide_markup)
        dbworker.set_state(message.chat.id, utils.States.S_BIRTHDAY.value)  # Меняем состояние
        bd.addUserPhone(message.chat.id, message.contact.phone_number)  # Добавляем телефон в базу


# Ловим дату рождения
@bot.message_handler(func=lambda message: utils.validate_state2(message.chat.id, utils.States.S_BIRTHDAY.value))
def user_entering_birthday(message):
    # Проверка на дату
    if utils.validate_date(message.text) is False:
        bot.send_message(message.chat.id, messages.s_birth_error)
        return
    # На данном этапе мы уверены, что message.text можно преобразовать в дату, поэтому ничем не рискуем
    birthday = utils.convert_date(message.text)
    current_date = datetime.datetime.now()
    print(birthday)
    print(current_date)

    if (current_date.year - birthday.year) > 100 or (current_date.year - birthday.year) < 2:
        bot.send_message(message.chat.id, messages.s_birth_cheat)
        return
    else:
        # Дата рождения введена корректно, можно идти дальше
        dbworker.set_state(message.chat.id, utils.States.S_MENU.value)  # Меняем состояние
        bd.addUserBirth(message.chat.id, birthday)  # Добавляем ДР в базу
        utils.validate_ref(bd, bot, message.chat.id)  # Дарим подарок
        bot.send_message(message.chat.id, messages.s_menu, reply_markup=markups.keyboardMain)


@bot.message_handler(commands=["Подарки"])
def gifts(message):
    if utils.validate_state2(message.chat.id, utils.States.S_MENU.value):
        gifts_list = utils.get_users_gifts(bd, message.chat.id)
        bot.send_message(message.chat.id, messages.s_gifts, reply_markup=markups.keyboardMain)

        for i in gifts_list:
            msg = "Название: " + i['name'] + ". Статус: " + i['status']
            bot.send_message(message.chat.id, msg, reply_markup=markups.keyboardMain)

        #bot.send_message(message.chat.id, messages.s_gifts + utils.get_users_gifts(bd, message.chat.id),
        #                 reply_markup=markups.keyboardMain)


@bot.message_handler(commands=["Пригласить_друга"])
def invite_friend(message):
    if utils.validate_state2(message.chat.id, utils.States.S_MENU.value):
        user_id = str(message.chat.id)
        # bot_name = 'vlgTest1Bot'
        # bot_name = telebot.TeleBot(config.bot_name)
        img_name = 'qr-' + user_id
        tmp_path = 'tmp/'
        link = 'https://telegram.me/' + 'nextkz_bot' + '?start=' + user_id
        qr.createQR(tmp_path, img_name, link)
        bot.send_message(message.chat.id, messages.s_qr, reply_markup=markups.keyboardMain)
        bot.send_photo(message.chat.id, open(tmp_path + img_name + '.png', 'rb'), reply_markup=markups.keyboardMain)
        os.remove(tmp_path + img_name + '.png')
        bot.send_message(message.chat.id, link, reply_markup=markups.keyboardMain)


@bot.message_handler(content_types=["text"])
def something_wrong(message):
    bot.send_message(message.chat.id, messages.s_text, reply_markup=markups.keyboardMain)


if __name__ == '__main__':
    bot.polling(none_stop=True)

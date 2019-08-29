import datetime
import random
import markups
import messages
from enum import Enum


# Проверяем строку на дату
def validate_date(date_text):
    try:
        if date_text != datetime.datetime.strptime(date_text, "%d.%m.%Y").strftime("%d.%m.%Y"):
            raise ValueError
        return False
    except ValueError:
        return True


# Преобразование строки в дату
def convert_date(date_text):
    return datetime.datetime.strptime(date_text, "%d.%m.%Y")


# Дарим подарок юзеру
def gift_giving(db, bot, id_user, id_event):
    test = db.get_descript_gift_events_by_id(id_event)  # Получаем список
    new_list = []
    for i in test:
        if i['cnt'] > 0:  # Проверяем кол-во оставшихся подарков
            new_list.append(i)  # Добавляем эти подарки в новый список
    if len(new_list) == 0:
        bot.send_message(id_user, messages.s_gift_end)  # Подарки закончились
    else:
        gift = random.choice(new_list)  # Выбираем рандомом подарок
        db.add_gift_by_user_id_event_gift(id_user, gift['id_event_gift'])  # Дарим подарок
        db.change_count_gift_by_id_gift(gift['id_gift'])  # Уменьшаем количество подарков в базе
        bot.send_message(id_user, f'{messages.s_gift}{gift["name"]}\n{gift["descript"]}😊\n{messages.s_gifts_addr}',
                         reply_markup=markups.keyboardMain)
        bot.send_photo(
            id_user,
            (open(f'/home/ubuntu/bots/kidsReferal/env/APBot2test/media/{gift["img"]}', 'rb')),
            reply_markup=markups.keyboardMain)


# Проверка дня рождения
def check_birthday(db, bot, current_date):
    test = db.get_user_by_dt_birth(current_date)
    if len(test) != 0:
        for i in test:
            gift_giving(db, bot, i['id_user'], 4)


# Получение списка подарков юзера
# def get_users_gifts(bd, user_id):
#     spisok = bd.getGiftByIdUser(user_id)
#     stroka = ''
#     try:
#         for i in spisok:
#             stroka += "Название: " + i['name'] + ". Статус: " + i['status'] + "\n"
#         return stroka
#     except TypeError:
#         return messages.s_error
# Возвращаем полный список
def get_users_gifts(db, user_id):
    try:
        return db.get_gift_by_id_user(user_id)
    except TypeError:
        return messages.s_error


# Проверка состояния юзера
def validate_state(db, message):
    user_id = message.chat.id
    text = message.text
    s = " "
    markup = markups.hide_markup
    try:
        state = db.get_id_state(user_id)[0]['id_state']
        if state == States.S_ENTER_NAME.value:
            s = messages.s_name_remind
        elif state == States.S_PHONE.value:
            s = messages.s_phone_remind
            markup = markups.keyboardPhone
        elif state == States.S_BIRTHDAY.value:
            s = messages.s_birth_remind
        elif state == States.S_MENU.value:
            s = messages.s_menu
            markup = markups.keyboardMain
    except TypeError:
        s = messages.s_hello
        if len(text) > 6:
            db.add_user(user_id, text[7:])
        else:
            db.add_user(user_id, user_id)
    return [s, markup]


# Проверка состояния юзера2
def validate_state2(db, user_id, states):
    try:
        state_user = db.get_id_state(user_id)[0]['id_state']
        if state_user == states:
            return True
        else:
            return False
    except TypeError:
        print("validate_state2: TypeError")
        return False


# Проверка реферала
def validate_ref(db, bot, user_id):
    id_invite = int(db.get_id_invite(user_id)[0]['id_invite'])
    if id_invite != user_id:
        gift_giving(db, bot, user_id, 3)
        gift_giving(db, bot, id_invite, 2)
    else:
        gift_giving(db, bot, user_id, 1)


# Возможные состояния пользователя
class States(Enum):

    S_START = 0  # Начало нового диалога
    S_ENTER_NAME = 1  # Ввод имени
    S_PHONE = 2  # Ввод телефона
    S_BIRTHDAY = 3  # Ввод даты рождения
    S_MENU = 4  # Основное меню

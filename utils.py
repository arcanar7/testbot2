import datetime
import random
import dbworker
import markups
import messages
from enum import Enum


# Проверяем строку на дату
def validate_date(date_text):
    try:
        if date_text != datetime.datetime.strptime(date_text, "%d.%m.%Y").strftime("%d.%m.%Y"):
            raise ValueError
        return True
    except ValueError:
        return False


# Преобразование строки в дату
def convert_date(date_text):
    return datetime.datetime.strptime(date_text, "%d.%m.%Y")


# Дарим подарок юзеру
def gift_giving(bd, bot, id_user, id_event):
    test = bd.getDescriptGiftEventsById(id_event)  # Получаем список
    new_list = []
    for i in test:
        if i['cnt'] > 0:  # Проверяем кол-во оставшихся подарков
            new_list.append(i)  # Добавляем эти подарки в новый список
    if len(new_list) == 0:
        bot.send_message(id_user, messages.s_gift_end)  # Подарки закончились
    else:
        gift = random.choice(new_list)  # Выбираем рандомом подарок
        bd.addGiftByUserIdEventGift(id_user, gift['id_event_gift'])  # Дарим подарок
        bd.changeCountGiftByIdGift(gift['id_gift'])  # Уменьшаем количество подарков в базе

        # bot.send_message(id_user, messages.s_gift + gift['name'] + " (" +
        #                  gift['descript'] + ")", reply_markup=markups.keyboardMain)

        bot.send_message(id_user, f'{messages.s_gift}{gift["name"]}\n{gift["descript"]}😊\n{messages.s_gifts_addr}',
                         reply_markup=markups.keyboardMain)
        bot.send_photo(
            id_user,
            (open(f'/home/ubuntu/bots/kidsReferal/env/APBot2test/media/{gift["img"]}', 'rb')),
            reply_markup=markups.keyboardMain)


# Проверка дня рождения
def check_birthday(bd, bot, current_date):
    test = bd.getUserByDtBirth(current_date)
    if len(test) != 0:
        for i in test:
            gift_giving(bd, bot, i['id_user'], 4)


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
def get_users_gifts(bd, user_id):
    try:
        return bd.getGiftByIdUser(user_id)
    except TypeError:
        return messages.s_error


# Проверка состояния юзера
def validate_state(bd, message):
    user_id = message.chat.id
    text = message.text
    state = dbworker.get_current_state(user_id)
    s = " "
    markup = markups.hide_markup
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
    else:  # состояние "0" - начало диалога
        s = messages.s_hello
        dbworker.set_state(user_id, States.S_ENTER_NAME.value)
        if len(text) > 6:
            bd.addUser(user_id, text[7:])
        else:
            bd.addUser(user_id, user_id)
    return [s, markup]


# Проверка состояния юзера2
def validate_state2(user_id, states):
    state_user = dbworker.get_current_state(user_id)
    if state_user == states:
        return True
    else:
        return False


# Проверка реферала
def validate_ref(bd, bot, user_id):
    id_invite = int(bd.getid_invite(user_id)[0]['id_invite'])
    if id_invite != user_id:
        gift_giving(bd, bot, user_id, 3)
        gift_giving(bd, bot, id_invite, 2)
    else:
        gift_giving(bd, bot, user_id, 1)


# Возможные состояния пользователя
class States(Enum):

    S_START = "0"  # Начало нового диалога
    S_ENTER_NAME = "1"  # Ввод имени
    S_PHONE = "2"  # Ввод телефона
    S_BIRTHDAY = "3"  # Ввод даты рождения
    S_MENU = "4"  # Основное меню

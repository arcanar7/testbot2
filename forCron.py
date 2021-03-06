import telebot
import config
import messages
import utils
import markups
from dbQuery import Query

bot = telebot.TeleBot(config.token)
db = Query()

listId = db.get_id_user_14_day()
if listId:
    for item in listId:
        bot.send_message(item['id_user'], messages.s_birth_14, reply_markup=markups.keyboardMain)
        utils.gift_giving(db,bot, item['id_user'], 4)

listId = db.get_id_user_7_day()
if listId:
    for item in listId:
        bot.send_message(item['id_user'], messages.s_birth_7, reply_markup=markups.keyboardMain)

listId = db.get_id_user_now_day()
if listId:
    for item in listId:
        bot.send_message(item['id_user'], messages.s_birth_0, reply_markup=markups.keyboardMain)

# bot.send_message(272541442, 'I am are life!')




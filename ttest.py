import telebot
import config
import messages
import utils
from dbQuery import Query

bot = telebot.TeleBot(config.token)
db = Query()

bot.send_message(272541442, 'I am are life!')
import configparser
import os

config = configparser.ConfigParser()
file = os.path.join(os.path.dirname(__file__), 'config.ini')
config.read(file)
token = config["DEFAULT"]["token"]
bot_name = config["DEFAULT"]["bot_name"]
db_file = config["Bot Specific"]["db_file"]
host = config["Bot Specific"]["host"]
user = config["Bot Specific"]["user"]
password = config["Bot Specific"]["password"]
db = config["Bot Specific"]["db"]
charset = config["Bot Specific"]["charset"]

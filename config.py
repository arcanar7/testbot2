import configparser


config = configparser.ConfigParser()
config.read("config.ini")
token = config["DEFAULT"]["token"]
db_file = config["Bot Specific"]["db_file"]
host = config["Bot Specific"]["host"]
user = config["Bot Specific"]["user"]
password = config["Bot Specific"]["password"]
db = config["Bot Specific"]["db"]
charset = config["Bot Specific"]["charset"]

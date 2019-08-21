# from vedis import Vedis
import config
import utils
import shelve
import pickle


# Пытаемся узнать из базы «состояние» пользователя
def get_current_state(user_id):
    # with Vedis(config.db_file) as db:
    #     try:
    #         return db[user_id].decode('utf-8')
    #     except KeyError:  # Если такого ключа почему-то не оказалось
    #         return utils.States.S_START.value  # значение по умолчанию - начало диалога
    with shelve.open(config.db_file) as storage:
        try:
            return storage[str(user_id)]
        except KeyError:
            return utils.States.S_START.value


# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id, value):
    # with Vedis(config.db_file) as db:
    #     try:
    #         db[user_id] = value
    #         return True
    #     except Exception:
    #         print("Ошибка базы состояний")
    #         return False
    with shelve.open(config.db_file) as storage:
        storage[str(user_id)] = value

import config
import utils
import shelve


# Пытаемся узнать из базы «состояние» пользователя
def get_current_state(user_id):
    with shelve.open(config.db_file) as storage:
        try:
            return storage[str(user_id)]
        except KeyError:
            return utils.States.S_START.value


# Сохраняем текущее «состояние» пользователя в нашу базу
def set_state(user_id, value):
    with shelve.open(config.db_file) as storage:
        storage[str(user_id)] = value

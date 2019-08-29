import pymysql.cursors
import config


class Query:
    #
    # получение id_user по дате рождения
    #
    def get_user_by_dt_birth(self, dt_birth):
        sql = f"select id_user from users where date_format(dt_birth, '%d.%m') = date_format('{dt_birth}', '%d.%m')"
        return Query.select_data(self, sql)

    #
    # Добавление юзера в БД
    #
    def add_user(self, id_user, id_invite):
        sql = f"insert into users (id_user, dt_add, id_invite, id_state) values('{id_user}', now(), '{id_invite}', '1')"
        return Query.insert_update_data(self, sql)

    #
    # Добавление имени юзера в БД
    #
    def add_user_name(self, id_user, name):
        sql = f"update users set name = '{name}' where id_user = '{id_user}'"
        return Query.insert_update_data(self, sql)

    #
    # Добавление номера телефона юзера в БД
    #
    def add_user_phone(self, id_user, phone):
        sql = f"update users set phone = '{phone}' where id_user = '{id_user}'"
        return Query.insert_update_data(self, sql)

    #
    # Добавление ДР юзера в БД
    #
    def add_user_birth(self, id_user, birth):
        sql = f"update users set dt_birth = '{birth}' where id_user = '{id_user}'"
        return Query.insert_update_data(self, sql)

    #
    # Добавление состояния юзера в БД
    #
    def add_user_state(self, id_user, state):
        sql = f"update users set id_state = '{state}' where id_user = '{id_user}'"
        return Query.insert_update_data(self, sql)

    #
    # Получение списка подарков у события, Таблица подарков событий EVENTS_GIFT
    #
    def get_event_gifts_by_id_event(self, id_event):
        sql = f"""
            select 
                eg.id_gift, gd.cnt
            from events_gift eg
            left join gift_descript gd on gd.id = eg.id_gift
            where id_event = {id_event}"""
        return Query.select_data(self, sql)

    #
    # Получение id, Таблица подарков событий EVENTS_GIFT
    #
    def get_id_event_gifts(self, id_event, id_gift):
        sql = f"select id from events_gift where id_event = {id_event} and id_gift = {id_gift}"
        return Query.select_data(self, sql)

    #
    # Изменение количества подарков, Таблица подарков GIFT_descript
    #
    def change_count_gift_by_id_gift(self, id_gift):
        sql = f"update gift_descript set cnt = cnt - 1 where id = {id_gift}"
        return Query.insert_update_data(self, sql)

    #
    # Добавить подарок юзеру, Таблица Журнал получения подарков gift_outs
    #
    def add_gift_by_user_id_event_gift(self, id_user, id_event_gift):
        s = 'Ожидает выдачи'
        sql = f"insert into gift_outs (id_user, id_event_gift, status) values('{id_user}', {id_event_gift}, {s})"
        return Query.insert_update_data(self, sql)

    #
    # Получение списка подарков юзера gift_outs
    #
    def get_gift_by_id_user(self, id_user):
        sql = f"""
            select 
                gd.id, gd.name, gd.img, go.status 
            from gift_outs go 
              left join events_gift eg on eg.id = go.id_event_gift 
              left join gift_descript gd on gd.id = eg.id_gift 
            where id_user = '{id_user}'
        """
        return Query.select_data(self, sql)

    #
    # Получение списка подарков юзера gift_outs
    #
    def get_gift_name_by_id(self, id_gift):
        sql = f"""
            select name, img from gift_descript where id = '{id_gift}'
        """
        return Query.select_data(self, sql)

    #
    # Получение id_invite, реферал
    #
    def get_id_invite(self, id_user):
        sql = f"select id_invite from users where id_user = {id_user}"
        return Query.select_data(self, sql)

    #
    # Получение id_state, состояние
    #
    def get_id_state(self, id_user):
        sql = f"select id_state from users where id_user = {id_user}"
        return Query.select_data(self, sql)

    #
    # Получить кучу всего по id события
    #
    def get_descript_gift_events_by_id(self, id_event):
        sql = f"""
            select 
                gf.id id_gift, gf.cnt, gf.name, gf.img, eg.id id_event_gift, ed.descript
            from events_descript ed
                left join events_gift eg on eg.id_event = ed.id
                left join gift_descript gf on gf.id = eg.id_gift
            where
                ed.id = {id_event}
        """
        return Query.select_data(self, sql)

    #
    # Получение всех полей и всех юзеров
    #
    def get_users(self):
        sql = 'select * from users'
        return Query.select_data(self, sql)

    #
    # Для тестирования select-запросов
    #
    def get_my_select(self, sql):
        return Query.select_data(self, sql)

    #
    # Для тестирования select-запросов
    #
    def get_my_update(self, sql):
        return Query.insert_update_data(self, sql)

    #
    # Получить наименование события по id
    #
    def get_event_descript_by_id(self, id_event):
        sql = f"select descript from events_descript where id = {id_event}"
        return Query.select_data(self, sql)

    #
    # вывод списка юзеров, чье др наступит через 14 дней
    #
    def get_id_user_14_day(self):
        sql = """select 
                    id_user 
                 from users 
                 where 
                    date_format(NOW() + interval 14 day, '%d.%m') = date_format(dt_birth, '%d.%m')"""
        return Query.select_data(self, sql)

    #
    # вывод списка юзеров, чье др наступит через 7 дней
    #
    def get_id_user_7_day(self):
        sql = """select 
                    id_user 
                 from users 
                 where 
                    date_format(NOW() + interval 7 day, '%d.%m') = date_format(dt_birth, '%d.%m')"""
        return Query.select_data(self, sql)

    #
    # вывод списка юзеров, чье др today
    #
    def get_id_user_now_day(self):
        sql = "select id_user from users where date_format(NOW(), '%d.%m') = date_format(dt_birth, '%d.%m')"
        return Query.select_data(self, sql)

    # -- внутренние функции класса #

    # def __init__(self):
    #     print("появился")
    #     # self.conn = pymysql.connect(
    #     #     host=config.host,
    #     #     user=config.user,
    #     #     password=config.password,
    #     #     db=config.db,
    #     #     charset=config.charset,
    #     #     cursorclass=pymysql.cursors.DictCursor
    #     # )
    #
    # def __del__(self):
    #     # self.conn.close()
    #     print("отключился")

    # -- универсальный select
    @staticmethod
    def select_data(self, sql):
        conn = pymysql.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            db=config.db,
            charset=config.charset,
            cursorclass=pymysql.cursors.DictCursor
        )
        result = None
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            if not result:
                result = None
            # for row in cursor.fetchall():
            #     result = row
        except Exception:
            print('Ошибка запроса')
            result = None
        finally:
            conn.close()
            return result

    # -- универсальный insert/update
    @staticmethod
    def insert_update_data(self, sql):
        # conn = self.conn
        conn = pymysql.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            db=config.db,
            charset=config.charset,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception:
            print('Ошибка запроса')
        finally:
            conn.close()
            pass


# -- примеры
#
# dbQ = Query()
#
# x = dbQ.getUsers()
# print('test-> ', x)
#
# x = dbQ.getUserByDtBirth('10.10.2000')
# print('test1-> ', x)
#
# # - можно отправлять свои селекты для тестинга
# x = dbQ.getMySelect('show tables')
# print('test2-> ', x)

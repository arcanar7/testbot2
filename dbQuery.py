import pymysql.cursors
import config


class Query:
    #
    # получение id_user по дате рождения
    #
    def getUserByDtBirth(self, dt_birth):
        sql = f"select id_user from users where date_format(dt_birth, '%d.%m') = date_format('{dt_birth}', '%d.%m')"
        return Query.selectData(self, sql)

    #
    # Добавление юзера в БД
    #
    def addUser(self, id_user, id_invite):
        sql = f"insert into users (id_user, dt_add, id_invite) values('{id_user}', now(), '{id_invite}')"
        return Query.insertUpdateData(self, sql)

    #
    # Добавление имени юзера в БД
    #
    def addUserName(self, id_user, name):
        sql = f"update users set name = '{name}' where id_user = '{id_user}'"
        return Query.insertUpdateData(self, sql)

    #
    # Добавление номера телефона юзера в БД
    #
    def addUserPhone(self, id_user, phone):
        sql = f"update users set phone = '{phone}' where id_user = '{id_user}'"
        return Query.insertUpdateData(self, sql)

    #
    # Добавление ДР юзера в БД
    #
    def addUserBirth(self, id_user, birth):
        sql = f"update users set dt_birth = '{birth}' where id_user = '{id_user}'"
        return Query.insertUpdateData(self, sql)

    #
    # Получение списка подарков у события, Таблица подарков событий EVENTS_GIFT
    #
    def getEventGiftsByIdEvent(self, id_event):
        sql = f"""
            select 
                eg.id_gift, gd.cnt
            from events_gift eg
            left join gift_descript gd on gd.id = eg.id_gift
            where id_event = {id_event}"""
        return Query.selectData(self, sql)

    #
    # Получение id, Таблица подарков событий EVENTS_GIFT
    #
    def getidEventGifts(self, id_event, id_gift):
        sql = f"select id from events_gift where id_event = {id_event} and id_gift = {id_gift}"
        return Query.selectData(self, sql)

    #
    # Изменение количества подарков, Таблица подарков GIFT_descript
    #
    def changeCountGiftByIdGift(self, id_gift):
        sql = f"update gift_descript set cnt = cnt - 1 where id = {id_gift}"
        return Query.insertUpdateData(self, sql)

    #
    # Добавить подарок юзеру, Таблица Журнал получения подарков gift_outs
    #
    def addGiftByUserIdEventGift(self, id_user, id_eventGift):
        s = 'Ожидает выдачи'
        sql = f"insert into gift_outs (id_user, id_event_gift, status) values('{id_user}', {id_eventGift}, {s})"
        return Query.insertUpdateData(self, sql)

    #
    # Получение списка подарков юзера gift_outs
    #
    def getGiftByIdUser(self, id_user):
        sql = f"""
            select 
                gd.id, gd.name, gd.img, go.status 
            from gift_outs go 
              left join events_gift eg on eg.id = go.id_event_gift 
              left join gift_descript gd on gd.id = eg.id_gift 
            where id_user = '{id_user}'
        """
        return Query.selectData(self, sql)

    #
    # Получение списка подарков юзера gift_outs
    #
    def getGiftNameById(self, id_gift):
        sql = f"""
            select name, img from gift_descript where id = '{id_gift}'
        """
        return Query.selectData(self, sql)

    #
    # Получение id_invite, реферал
    #
    def getid_invite(self, id_user):
        sql = f"select id_invite from users where id_user = {id_user}"
        return Query.selectData(self, sql)

    #
    # Получить кучу всего по id события
    #
    def getDescriptGiftEventsById(self, id_event):
        sql = f"""
            select 
                gf.id id_gift, gf.cnt, gf.name, gf.img, eg.id id_event_gift, ed.descript
            from events_descript ed
                left join events_gift eg on eg.id_event = ed.id
                left join gift_descript gf on gf.id = eg.id_gift
            where
                ed.id = {id_event}
        """
        return Query.selectData(self, sql)

    #
    # Получение всех полей и всех юзеров
    #
    def getUsers(self):
        sql = 'select * from users'
        return Query.selectData(self, sql)

    #
    # Для тестирования select-запросов
    #
    def getMySelect(self, sql):
        return Query.selectData(self, sql)

    #
    # Получить наименование события по id
    #
    def getEventDescriptById(self, id_event):
        sql = f"select descript from events_descript where id = {id_event}"
        return Query.selectData(self, sql)


    #
    # вывод списка юзеров, чье др наступит через 14 дней
    #
    def getIdUser14Day(self):
        sql = "select id_user from users where date_format(NOW() + interval 14 day, '%d.%m') = date_format(dt_birth, '%d.%m')"
        return Query.selectData(self, sql)

    #
    # вывод списка юзеров, чье др наступит через 7 дней
    #
    def getIdUser7Day(self):
        sql = "select id_user from users where date_format(NOW() + interval 7 day, '%d.%m') = date_format(dt_birth, '%d.%m')"
        return Query.selectData(self, sql)


    #
    # вывод списка юзеров, чье др today
    #
    def getIdUserNowDay(self):
        sql = "select id_user from users where date_format(NOW(), '%d.%m') = date_format(dt_birth, '%d.%m')"
        return Query.selectData(self, sql)

    ###### -- внутренние функции класса #

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
    def selectData(self, sql):
        # conn = self.conn
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
    def insertUpdateData(self, sql):
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

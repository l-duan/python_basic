# -*- coding:utf-8 -*-
__auth__ = 'christian'

from ..utility.sql_helper import MysqlHelper

class Admin(object):

    def __init__(self):
        self.__helper = MysqlHelper()

    def Get_One(self, id):
        sql = "select * from admin where id=%s"
        params = (id,)
        return self.__helper.Get_One(sql, params)

    def CheckValidate(self, username, password):
        sql = "select * from admin where name=%s and password=%s"
        params = (username, password,)
        return self.__helper.Get_One(sql, params)

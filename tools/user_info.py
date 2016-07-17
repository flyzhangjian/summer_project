#!/usr/bin/env python
# coding=utf-8

import python_tools

class user():
    def __init__(self,account_number,password='12'):
        self.account_number = account_number
        self.password = password

    def check_information(self):
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "select user_id,user_name,user_password,time from user_information where user_account_number=%s"
                cursor.execute(sql,(self.account_number))
                result = cursor.fetchall()
            connection.commit()
        finally:
            connection.close()
        if python_tools.check_user_password(self.password,result[0]['user_password']):
            return result
        else:
            return 0

    def check_account_number(self):
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "select user_account_number from user_information"
                cursor.execute(sql)
                result = cursor.fetchall()
            connection.commit()
        finally:
            connection.close()
        for result_temp in result:
            if self.account_number == result_temp['user_account_number']:
                return 1
        return 0

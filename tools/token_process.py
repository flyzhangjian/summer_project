#!/usr/bin/env python
# coding=utf-8

import time
import python_tools

class token():
    def __init__(self,token,user_id):
        self.token = token
        self.user_id = user_id

    def token_check(self):
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT user_token,time FROM user_token WHERE user_id = %s"
                cursor.execute(sql,(self.user_id))
                result = cursor.fetchall()
        finally:
            connection.close()
        if self.token==result[0]['user_token']:
            time_mow = time.time()
            if time_mow - result[0]['time'] <= 7*24*3600:
                return 1
            return 0
        return 0

#!/usr/bin/env python
# coding=utf-8

import python_tools

class user():
    def __init__(self,name,account_number,password,password_again):
        self.name=name
        self.account_number=int(account_number)
        self.password=password
        self.password_again=password_again

    def insert_into(self):
        time=python_tools.get_time()
        password=python_tools.encrypt(self.password)
        connection=python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql="INSERT INTO user_information (user_account_number,user_password,user_name,time) VALUES(%s,%s,%s,%s)"
                cursor.execute(sql,(int(self.account_number),password,self.name,time))
            connection.commit()
        finally:
            connection.close()
    
    def check_password(self):
        if self.password==self.password_again:
            return 1
        else:
            return 0

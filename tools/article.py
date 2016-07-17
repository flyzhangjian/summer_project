#!/usr/bin/env python
# coding=utf-8

import time
import python_tools

class article():

    def __init__(self,user_id,article = 'haha',**article_id):
        self.user_id = int(user_id)
        self.article = article
        self.article_id = article_id

    def insert_article(self):
        time_now = time.time()
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT user_name FROM user_information WHERE user_id = %s"
                cursor.execute(sql,(self.user_id))
                result = cursor.fetchone()
                sql = "INSERT INTO articles(user_id,article,time,user_name) VALUES (%s,%s,%s,%s)"
                cursor.execute(sql,(self.user_id,self.article,time_now,result['user_name']))
            connection.commit()
        finally:
            connection.close()

    def select_article(self):
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM articles"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            connection.close()
            return result

    def insert_transmit(self):
        time_now = int(time.time())
        article_id_now = int(self.article_id['article_id_transmit'])
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT article_id FROM transmit WHERE user_id = %s"
                cursor.execute(sql,(self.user_id))
                result = cursor.fetchall()
                for x in result:
                    if article_id_now == x['article_id']:
                        return 0
                sql = "INSERT INTO transmit(user_id,article_id,time) VALUES (%s,%s,%s)"
                cursor.execute(sql,(self.user_id,article_id_now,time_now))
            connection.commit()
        finally:
            connection.close()
        return 1

    def insert_collect(self):
        time_now = time.time()
        article_id_now = int(self.article_id['article_id_transmit'])
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT article_id FROM collection WHERE user_id = %s"
                cursor.execute(sql,(self.user_id))
                result = cursor.fetchall()
                for x in result:
                    if article_id_now == x['article_id']:
                        return 0
                sql = "INSERT INTO collection(user_id,article_id,time) VALUES(%s,%s,%s)"
                cursor.execute(sql,(self.user_id,article_id_now,time_now))
            connection.commit()
        finally:
            connection.close()
        return 1

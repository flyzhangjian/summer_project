#!/usr/bin/env pytho 
# coding=utf-8
import python_tools
import time

def insert_online_comment(user_id,user_to_id,article_id):
    connection = python_tools.connect_to_database()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO immediate_comment(user_id,user_to_id,article_id) VALUES(%s,%s,%s)"
            cursor.execute(sql,(user_id,user_to_id,article_id))
        connection.commit()
    finally:
        connection.close()

class comment():

    def __init__(self,parent_id,article_id,commen_body = 'ha',comment_from_id = 12,comment_to_id = 12):
        self.parent_id = parent_id
        self.article_id = article_id
        self.comment_body = commen_body
        self.comment_from_id = comment_from_id
        self.comment_to_id = comment_to_id

    def insert_into(self):
        connection = python_tools.connect_to_database()
        time_now = time.time()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO comments(parent_id,article_id,comment_body,coment_from_id,coment_to_id,time) VALUES(%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql,(self.parent_id,self.article_id,self.comment_body,self.comment_from_id,self.comment_to_id,time_now))
            connection.commit()
        finally:
            connection.close()

    def select_child(self):
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM comments WHERE article_id = %s ORDER BY time"
                cursor.execute(sql,(self.article_id))
                result = cursor.fetchall()
        finally:
            connection.close()
        return result

    def select_from_name(self):
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT comments.coment_from_id,user_information.user_name FROM comments INNER JOIN user_information ON user_information.user_id = comments.coment_from_id"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            connection.close()
        return result

    def select_to_name(self):
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT comments.coment_to_id,user_information.user_name FROM comments INNER JOIN user_information ON user_information.user_id = comments.coment_to_id"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            connection.close()
        return result

    def select_user(self):
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT comments.article_id,articles.user_id FROM comments INNER JOIN articles ON comments.article_id = articles.article_id"
                cursor.execute(sql)
                result = cursor.fetchall()
        finally:
            connection.close()
        return result

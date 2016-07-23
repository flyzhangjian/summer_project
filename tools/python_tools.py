#!/usr/bin/env python
# coding=utf-8
import time
import pymysql
import bcrypt

def get_time():
    return time.strftime('%Y-%m-%d-%H-%M',time.localtime())

def connect_to_database():
    connection = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '123456',
        database = 'summer_project',
        charset = 'utf8',
        cursorclass = pymysql.cursors.DictCursor
        )
    return connection

def encrypt(password):
    password = password.encode()
    hashed = bcrypt.hashpw(password,bcrypt.gensalt(10))
    return hashed

def check_user_password(password,hashed):
    password = password.encode()
    hashed = hashed.encode()
    if hashed == bcrypt.hashpw(password,hashed):
        return 1
    else:
        return 0

def get_token(user_infor):
    user_id = str(user_infor[0]['user_id'])
    user_time = user_infor[0]['time']
    result = user_id + user_time
    result = result.encode()
    token = bcrypt.hashpw(result,bcrypt.gensalt())
    return token

def insert_token(user_id,user_token,time):
    connection = connect_to_database()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT user_token FROM user_token WHERE user_id = %s"
            cursor.execute(sql,(user_id))
            result = cursor.fetchall()
            if result:
                sql = "DELETE FROM user_token WHERE user_id = %s"
                cursor.execute(sql,(user_id))
            sql = "INSERT INTO user_token (user_id,user_token,time) VALUES (%s,%s,%s)"
            cursor.execute(sql,(user_id,user_token,time))
        connection.commit()
    finally:
        connection.close()

def insert_focus(focus_fr,focus_t):
    connection = connect_to_database()
    focus_from,focus_to = int(focus_fr),int(focus_t) 
    try:
        with connection.cursor() as cursor:
            sql = "SELECT focus_to FROM focus WHERE focus_from = %s"
            cursor.execute(sql,(focus_from))
            result = cursor.fetchall()
            print(result)
            for x in result:
                if focus_to == x['focus_to']:
                    return 0
            sql = "INSERT INTO focus(focus_from,focus_to) VALUES(%s,%s)"
            cursor.execute(sql,(focus_from,focus_to))
        connection.commit()
    finally:
        connection.close()
    return 1

def check_focus(user_id):
    connection = connect_to_database()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT focus.focus_to,user_information.user_name FROM focus INNER JOIN user_information ON focus.focus_to = user_information.user_id"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
        return result

def check_focus_one(user_id):
    connection = connect_to_database()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT article_id,article,time,user_name FROM articles WHERE user_id = %s"
            cursor.execute(sql,(user_id))
            result = cursor.fetchall()
    finally:
        connection.close()
    for x in result:
        x['user_id'] = user_id
    return result

def sort(response,response_p,response_n,x,y):
    if x >= len(response)-1:
        return response
    else:
        if response_p['comment_id'] == response_n['parent_id']:
            temp = response[y]
            response[y] = response_p
            response[x] = response_n
        else:
            if y < len(response)-1:
                return sort(response,response[x+1],x,y+1)
            else:
                return sort(response,response[x],response[x+1],x+1,x+1)

def check_to(response,response_to_name):
    for x in response:
        for y in response_to_name:
            if x['coment_to_id'] == y['coment_to_id']:
                x['comment_to_name'] = y['user_name']
    return response

def check_from(response,response_from_name):
    for x in response:
        for y in response_from_name:
            if x['coment_from_id'] == y['coment_from_id']:
                x['comment_from_name'] = y['user_name']
    return response

def check_user_article(response,response_p):
    for x in response:
        for y in response_p:
            if x['article_id'] == y['article_id']:
                x['user_article'] = y['user_id']
    return response

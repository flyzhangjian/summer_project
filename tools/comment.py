#!/usr/bin/env python
# coding=utf-8
import python_tools

class comment():

    def __init__(self,parent_id,article_id,commen_body,comment_from_id,comment_to_id):
        self.parent_id = parent_id
        self.article_id = article_id
        self.comment_body = commen_body
        self.comment_from_id = comment_from_id
        self.comment_to_id = comment_to_id

    def insert_into(self):
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO comments(parent_id,article_id,commen_body,comment_from_id,comment_to_id) VALUES(%s,%s,%s,%s%s)"
                cursor.execute(sql,(self.parent_id,self.article_id,self.comment_body,self.comment_from_id,self.comment_to_id))
            connection.commit()
        finally:
            connection.close()

    def select_child(self):
        connection = python_tools.connect_to_database()
        try:
            with connection.cursor() as cursor:
                sql = "WITH COMMENT_CTE(comment_id,parent_id,comment_body,t_level)\
                        AS(\
                        SELECT comment_id,parent_id,comment_body,0 AS t_level FROM comments\
                        WHERE parent_id = %s\
                        UNION ALL\
                        SELECT c.comment_id,c.parent_id,c.comment_body,ce.t_level + 1 FROM comments AS c \
                        INNER JOIN COMMENT_CTE AS ce\
                        ON c.parent_id = ce.comment_id\
)\
                        SELECT * FROM COMMENT_CTE"
                cursor.execute(sql,(self.article_id))
                result = cursor.fetchall()
        finally:
            connection.close()
        return result


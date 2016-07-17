#!/usr/bin/env python
# coding=utf-8

import sys,json,time
sys.path.append('tools')
import python_tools,user_check_insert,user_info,get_data
import token_process,article

def application(environ,start_response):
    user_data = get_data.application(environ,start_response)
    print(user_data)
    if user_data:
        user = user_check_insert.user(user_data['name'],user_data['account_number'],user_data['password'],user_data['confirm_it'])
        result = user.check_password()
        if result == 0:
            start_response('200 OK',[('Content-Type','text/html')])
            return json.dumps({"result":0}).encode()
        else:
            user.insert_into()
            start_response('200 OK',[('Content-Type','text/html')])
            return json.dumps({"result":1}).encode()

def log_in(environ,start_response):
    user_data = get_data.application(environ,start_response)
    if user_data:
        account_number = int(user_data['account_number'])
        password = user_data['password']
        log =  user_info.user(account_number,password)
        if log.check_account_number():
            user_infor = log.check_information()
            if user_infor:
                start_response('200 OK',[('Content-Type','text/html')])
                token = str(python_tools.get_token(user_infor))
                time_o = time.time()
                python_tools.insert_token(user_infor[0]['user_id'],token,time_o)
                return json.dumps({"user_id":user_infor[0]['user_id'],"result":1,"token":token}).encode()
            else:
                start_response('200 OK',[('Content-Type','text/html')])
                return json.dumps({"result":0}).encode()
        else:
            start_response('200 OK',[('Content-Type','text/html')])
            return json.dumps({"result":0}).encode()

def post_my_thoughts(environ,start_response):
    user_data = get_data.application(environ,start_response)
    token_check_result = token_process.token(user_data['token'],user_data['user_id']).token_check()
    if token_check_result:
        article.article(user_data['user_id'],user_data['article']).insert_article()
        start_response('200 OK',[('Content-Type','text/html')])
        return json.dumps({"result":1}).encode()
    start_response('200 OK',[('Content-Type','text/html')])
    return json.dumps({"result":0}).encode()

def get_my_thoughts(environ,start_response):
    user_data = get_data.application(environ,start_response)
    token_check_result = token_process.token(user_data['token'],user_data['user_id']).token_check()
    if token_check_result:
        result = article.article(user_data['user_id']).select_article()
        start_response('200 OK',[('Content-Type','text/html')])
        return json.dumps(result).encode()

def focus(environ,start_response):
    user_data = get_data.application(environ,start_response)
    user_data['user_to'] = user_data['id_to'].split('_')[2]
    x = python_tools.insert_focus(user_data['user_id'],user_data['user_to'])
    if x:
        start_response('200 OK',[('Content-Type','text/html')])
        return json.dumps({"result":1}).encode()
    else:
        start_response('200 OK',[('Content-Type','text/html')])
        return json.dumps({"result":0}).encode()

def transmit(environ,start_response):
    user_data = get_data.application(environ,start_response)
    article_id = user_data['id_to'].split('_')[1]
    token_check_result = token_process.token(user_data['token'],user_data['user_id']).token_check()
    if token_check_result:
        if article.article(user_data['user_id'],article_id_transmit = article_id).insert_transmit():
            start_response('200 OK',[('Content-Type','text/html')])
            return json.dumps({'result':1}).encode()
        else:
            start_response('200 OK',[('Content-Type','text/html')])
            return json.dumps({'result':0}).encode()
    else:
        start_response('200 OK',[('Content-Type','text/html')])
        return json.dumps({'result':0}).encode()

def collect(environ,start_response):
    user_data = get_data.application(environ,start_response)
    article_id = user_data['id_to'].split('_')[1]
    token_check_result = token_process.token(user_data['token'],user_data['user_id']).token_check()
    if token_check_result:
        if article.article(user_data['user_id'],article_id_transmit = article_id).insert_collect():
            start_response('200 OK',[('Content-Type','text/html')])
            return json.dumps({'result':1}).encode()
        else:
            start_response('200 OK',[('Content-Type','text/html')])
            return json.dumps({'result':0}).encode()
    else:
        start_response('200 OK',[('Content-Type','text/html')])
        return json.dumps({'result':0}).encode()

def check_focus(environ,start_response):
    user_data = get_data.application(environ,start_response)
    token_check_result = token_process.token(user_data['token'],user_data['user_id']).token_check()
    if token_check_result:
        response = python_tools.check_focus(user_data['user_id'])
        start_response('200 OK',[('Content-Type','text/html')])
        return json.dumps(response).encode()
    else:
        start_response('200 OK',[('Content-Type','text/html')])
        return json.dumps({}).encode()

#!/usr/bin/env python
# coding=utf-8
import main

def application(environ,start_response):
    path = environ['PATH_INFO']
    if path == '/set/set_account_number':
        return main.application(environ,start_response)
    elif path == '/log_in':
        start_response('200 OK', [('Content-Type', 'text/html')])
        return main.log_in(environ,start_response)
    elif path == '/my_thoughts':
        return main.post_my_thoughts(environ,start_response)
    elif path == '/get_my_thoughts':
        return main.get_my_thoughts(environ,start_response)
    elif path == '/focus':
        return main.focus(environ,start_response)
    elif path == '/transmit':
        return main.transmit(environ,start_response)
    elif path == '/collect':
        return main.collect(environ,start_response)
    elif path == '/check_focus':
        return main.check_focus(environ,start_response)

#!/usr/bin/env python
# coding=utf-8


def application(environ,start_response):
    status='200 ok'
    output='hello world'
    response_headers = [('Content-type', 'text/html')]
    post_date = {}
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH',0))
    except:
        request_body_size = 0
    if request_body_size != 0:
        request_body=environ['wsgi.input'].read(request_body_size).decode().split('&')
        for request_body_temp in request_body:
            post_dates = request_body_temp.split('=')
            post_date[post_dates[0]] = post_dates[1]
    return post_date

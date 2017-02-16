#!/usr/bin/env python
#coding:utf8

import sys, os
import bottle

from bottle import route, run, template

@route('/login')
def login():
	return 'login showinfo {0}'.format(os.uname())

run(host='192.168.50.127', port=8000)

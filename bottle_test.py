#!/usr/bin/env python
#coding:utf8

import sys, os
import bottle

from bottle import route, run, template, request, static_file, post

'''
	<form method="POST" action="/login">
	用户名:<input name="username" type="text"/><br>
	密码:  <input name="password" type="password"/><br>
	<input value="登录" type="submit"/>
	</form>
'''

@route('/login', method="GET")
def login():
	'''login page'''
	return template('login', message='')

#@route('/login', method='POST')
@post('/login')
def login_submit():
	'''check login'''
	name = request.forms.get("username")
	pwd  = request.forms.get("password")
	print("name={0},pwd={1}".format(name, pwd))
	if not name or pwd != '10086':
		m = u"密码输入错误"
		return bottle.template('login', message=m)

	return template('login_success', username=name, password=pwd)

@route('/static/<filename>')
def do_download(filename):
	return static_file(filename, root=r'D:\\')

@route('/<filename>', method='POST')
def do_upload(filename):
	upload = request.files.get('filename')
	save_path = os.path.join(r'D:\\', filename)
	upload.save(save_path)
	return 'upload ok'

def main():
	run(port=8000, debug=True)


if __name__ == '__main__':
	sys.exit(main())
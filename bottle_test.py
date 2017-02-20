#!/usr/bin/env python
#coding:utf8

import sys, os
import bottle

from bottle import route, run, template, request, static_file, post

@route('/login')
def login():
	#return 'login showinfo {0}'.format(os.name)
	return '''
	<form method="POST" action="/login">
	用户名:<input name="username" type="text"/><br>
	密码:  <input name="password" type="password"/><br>
	<input value="登录" type="submit"/>
	</form>'''

#@route('/login', method='POST')
@post('/login')
def login_submit():
	name = request.forms.get("username")
	pwd  = request.forms.get("password")
	if pwd != '10086':
		return "密码输入错误"

	return '<p>用户名:{0}</p> <p>密码:{1}</p>'.format(name, pwd)

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
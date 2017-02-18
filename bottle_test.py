#!/usr/bin/env python
#coding:utf8

import sys, os
import bottle

from bottle import route, run, template, request, static_file

@route('/login')
def login():
	return 'login showinfo {0}'.format(os.uname())

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
	run(host='192.168.50.127', port=8000)


if __name__ == '__main__':
	sys.exit(main())
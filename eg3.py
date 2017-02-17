#!/usr/bin/env python
#coding:utf-8

import functools
import sys, time

def log(func):
	'''log decorator'''
	def decorator(*args, **kwargs):
		print('log decorator {0}'.format(func.__name__))
		return func(*args, **kwargs)
	return decorator

def log1(func):
	'''log1 decorator'''
	def decorator(*args, **kwargs):
		print('log1 decorator {0}'.format(func.__name__))
		return func(*args, **kwargs)
	decorator.__name__   = func.__name__
	decorator.__doc__    = func.__doc__
	decorator.__module__ = func.__module__
	return decorator

@log
def name():
	'''name log decorator'''
	print('name showinfo {0}'.format(time.asctime()))

@log1
def name1():
	'''name log decorator'''
	print('name1 showinfo {0}'.format(time.asctime()))


if __name__ == '__main__':
	print('log and log1 name is <{0}><{1}>'.format(log.__name__, log1.__name__))
	print('log and log1 doc  is <{0}><{1}>'.format(log.__doc__, log1.__doc__))

	print('name and name1 name is <{0}><{1}>'.format(name.__name__, name1.__name__))
	print('name and name1 doc  is <{0}><{1}>'.format(name.__doc__, name1.__doc__))

	name()
	name1()

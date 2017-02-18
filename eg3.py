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

def log2(func):
	'''log2 decorator'''
	@functools.wraps(func)
	def decorator(*args, **kwargs):
		print('log decorator {0}'.format(func.__name__))
		return func(*args, **kwargs)
	return decorator

@log
def name():
	'''name log decorator'''
	print('name showinfo {0}'.format(time.asctime()))

@log1
def name1():
	'''name1 log1 decorator'''
	print('name1 showinfo {0}'.format(time.asctime()))

@log2
def name2():
	'''name2 functools log decorator'''
	print('name2 showinfo {0}'.format(time.asctime()))


if __name__ == '__main__':
	print('log and log1 name is <{0}><{1}>'.format(log.__name__, log1.__name__))
	print('log and log1 doc  is <{0}><{1}>'.format(log.__doc__, log1.__doc__))

	print('name and name1 name is <{0}><{1}>'.format(name.__name__, name1.__name__))
	print('name and name1 doc  is <{0}><{1}>'.format(name.__doc__, name1.__doc__))
	print('name2 doc and name is <{0}><{1}>'.format(name2.__doc__, name2.__name__))

	name()
	name1()
	name2()


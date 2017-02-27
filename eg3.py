#!/usr/bin/env python
#coding:utf-8

import functools
import inspect
import sys, time, os

class my_property(object):
	def __init__(self, func):
		self.__doc__ = getattr(func, '__doc__')
		self.func = func

	def __get__(self, instance, owner):
		print instance
		if instance is None: return self

		res = instance.__dict__[self.func.__name__] = self.func(instance)
		return res


class Score(object):
	def __init__(self):
		self._score = 0

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if value < 0 or value > 99:
			raise ValueError('invalid score!')
		self._score = value

	@my_property
	def age(self):
		print '{0} age'.format('my_property')
		return self._score + 5

	@property
	def bage(self):
		print '{0} bage'.format('property')
		return self._score + 4


def is_admin(fun):
	@functools.wraps(fun)
	def check(*arg, **karg):
		fargs = inspect.getcallargs(fun, *arg, **karg)
		#print(fargs)
		if fargs.get('username') != 'admin':
			raise Exception('username not admin')
		return fun(*arg, **karg)
	return check

@is_admin
def login(username, pwd = '000'):
	print('user is {0}, pwd is {1}{2}'.format(username, pwd, os.linesep))

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
	login('admin')

	st = Score()
	print st.age
	print st.age

	print st.bage
	print st.bage





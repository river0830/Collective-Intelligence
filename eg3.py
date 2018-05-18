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
		print(instance)
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
		print('{0} age'.format('my_property'))
		return self._score + 5

	@property
	def bage(self):
		print('{0} bage'.format('property'))
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

#https://blog.csdn.net/jsc723/article/details/64439422?winzoom=1
def deepcopy_naive(sth):
	if isinstance(sth, list):
		return [deepcopy_naive(e) for e in sth]
	return sth

def deepcopy(sth):
	dic = {}
	def helper(th):
		if isinstance(th, list):
			if id(th) in dic.keys():
				return dic[id(th)]
			tmp = []
			dic[id(th)] = tmp
			for e in th:
				tmp.append(helper(e))
			return tmp
		return th
	return helper(sth)

def plat(ch,n):return''if ~n else ' '*(n-1)+ ch+ch[::-1][1:]+'\n'+plat(ch+chr(ord(ch[-1])+1),n-1)

def f(n):[ ([print('{}*{}={}'.format(x,y,x*y),end = ' ')for x in range(1,y+1)])for y in range(1,n+1)]
def f1(n,k=1): k==n+1 or (print(' '.join('{}*{}={}'.format(x,k,x*k) for x in range(1,k+1))),f1(n,k+1))

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
	print(st.age)
	print(st.age)

	print(st.bage)
	print(st.bage)

	a = [1, 0]
	a[1] = a
	b = deepcopy(a)
	print(a)
	print(b)

	print ('\n'.join([''.join(['--love'[(x-y)%6] if (x*0.04)**2+((y*0.1) - ((x*0.04)**2)**(1/3))**2 < 1 else ' ' for x in range(-30,30,1) ]) for y in range(15,-15,-1)]))
	f(9)
	f1(9)





#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

class show1(object):
	def __init__(self):
		self.x = np.linspace(0, 10, 200)

	def draw(self):
		y = np.sin(self.x)
		z = np.cos(self.x)
		z2 = np.cos(self.x ** 2)

		plt.figure(figsize=(12, 8))
		plt.plot(self.x, y,  color='red',   label=r'$sin(x)$')
		plt.plot(self.x, z,  color='green', label=r'$cos(x)$')
		plt.plot(self.x, z2, 'b--',  label=r'$cos(x^2)$')

		plt.title(u'大唐科技', fontproperties=font)
		plt.xlabel(u'时间', fontproperties=font)
		plt.ylabel(u'值', fontproperties=font)

		plt.ylim(-1.5, 1.5)
		plt.legend()
		plt.show()

if __name__ == '__main__':
	show1().draw()
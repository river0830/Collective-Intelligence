#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#import matplotlib.pylab  as pl

class PlotE2(object):
	def __init__(self):

		self.x = np.linspace(-np.pi, np.pi, 256)
		self.c = np.cos(self.x)
		self.s = np.sin(self.x)
		self.font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

	def draw(self):
		plt.figure(figsize=(10,6), dpi=80)
		plt.subplot(1, 1, 1)

		plt.plot(self.x, self.c, color='blue', linewidth=1.0, linestyle='--')
		plt.plot(self.x, self.s, color='green',  linewidth=1.0, linestyle='-')
		plt.xlim(-4.0, 4.0)
		plt.xticks(np.linspace(-4, 4, 9))
		plt.ylim(-1.0, 1.0)
		plt.yticks(np.linspace(-1, 1, 5))

		plt.title(u'PlotE2 学习', fontproperties=self.font)
		plt.xlabel(u'x轴', fontproperties=self.font)
		plt.ylabel(u'y轴', fontproperties=self.font)
		plt.show()


if __name__ == '__main__':
	PlotE2().draw()
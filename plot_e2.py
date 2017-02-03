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
		ax = plt.subplot(1, 1, 1)

		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')

		ax.xaxis.set_ticks_position('bottom')
		ax.spines['bottom'].set_position(('data', 0))

		ax.yaxis.set_ticks_position('left')
		ax.spines['left'].set_position(('data', 0))

		plt.plot(self.x, self.c, color='blue', linewidth=1.0, linestyle='--',
		         label='cos')
		plt.plot(self.x, self.s, color='green',  linewidth=1.0, linestyle='-',
		         label='sin')

		xmax, xmin = self.x.max(), self.x.min()
		ymax, ymin = self.c.max(), self.c.min()
		dx = (xmax - xmin)*0.1
		dy = (ymax - ymin)*0.1

		plt.xlim(xmin - dx, xmax + dx)
		plt.xticks(np.linspace(-np.pi, np.pi, 5), [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
		plt.ylim(ymin - dy, ymax + dy)
		plt.yticks(np.linspace(-1, 1, 5))

		plt.title(u'PlotE2 学习', fontproperties=self.font)
		#plt.xlabel(u'x轴', fontproperties=self.font)
		#plt.ylabel(u'y轴', fontproperties=self.font)

		plt.legend(loc='upper left')
		plt.show()


if __name__ == '__main__':
	PlotE2().draw()
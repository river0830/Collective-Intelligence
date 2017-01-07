#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

class show1(object):
	def __init__(self):
		self.x = np.linspace(0, 10, 200)

	def draw(self):
		y = np.sin(self.x)
		z = np.cos(self.x)
		z2 = np.cos(self.x ** 2)

		plt.figure(figsize=(12, 8))
		plt.plot(self.x, y,  color='red',   label='$sin(x)$')
		plt.plot(self.x, z,  color='green', label='$cos(x)$')
		plt.plot(self.x, z2, 'b--',  label='$cos(x^2)$')

		plt.title('river')
		plt.xlabel('times')
		plt.ylabel('value')

		plt.ylim(-1.5, 1.5)
		plt.legend()
		plt.show()

if __name__ == '__main__':
	show1().draw()
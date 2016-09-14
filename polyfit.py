import numpy as nu
import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [0.66, 1, 0.24, 2, 1.66]


for d in range(1,4):
	v,p = nu.polyfit(x, y, deg = d, cov=True)

	P = nu.poly1d(v)
	t = nu.arange(1, 5, 0.01)

	plt.plot(x, y, "b", t, P(t), 'r')
	plt.text(2, 1.5, "deg = "+str(d))
	plt.show()
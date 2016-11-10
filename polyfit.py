import numpy as nu
import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = nu.random.rand(5)
y =nu.sin(x)

for d in range(1,4):
    v,p = nu.polyfit(x, y, deg = d, cov = True)
    P = nu.poly1d(v)
    t = nu.arange(1, 5, 0.01)
    plt.errorbar(x, y, 0.1, 0.05, "k")
    plt.plot(1, 1.1, t, P(t), 'r')
    plt.text(2.5, 1.1, "deg = "+str(d))
    plt.show()

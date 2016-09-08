import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-2,2.01,0.001);


n = 500
a = 3
b = 0.5

def veier(x):
    s = 0.
    for i in range(n):
        s += b**i * np.cos(a**i * np.pi * x)
    return s

plt.plot(x,veier(x))
plt.grid(True)
plt.text(-0.4,2.3,r'$\sum_{n=0}^{\infty}\ 0.5^n\ \cos(3^i\pi\cdot x)$')
plt.axis([-2, 2,-4,4])
plt.show()
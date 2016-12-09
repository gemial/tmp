import matplotlib.pyplot as plt
import numpy as np

def distanse(x1,y1,x2,y2):
	return (((x1-x2)**2+(y1-y2)**2)**0.5)

def onclick(event):
	global press, nn, n
	press = True
	if n < 3:
		x[n:] = [event.xdata]*(3-n)
		y[n:] = [event.ydata]*(3-n)
		nn = n
		n += 1
	else:
		d = 5
		for i in range(3):
			if d > distanse(event.xdata,event.ydata,x[i], y[i]):
				d = distanse(event.xdata,event.ydata,x[i], y[i])
				nn = i
		x[nn] = event.xdata
		y[nn] = event.ydata

	onmotion(event)

def onrelease(event):
	global press
	press = False

def onmotion(event):
	global press
	if not press:
		return
	global nn
	ax.clear()
	
	x[nn] = event.xdata
	y[nn] = event.ydata

	ax.plot(x[:2],y[:2], color="#000080")
	ax.plot(x[1:],y[1:], color="#000080")
	ax.plot(x[::2],y[::2], color="#000080")
	ax.text(x[0],y[0], 'A', fontsize=14, color="#000000")
	ax.text(x[1],y[1], 'B', fontsize=14, color="#000000")
	ax.text(x[2],y[2], 'C', fontsize=14, color="#000000")

	ax.axis([-1, 1,-1, 1])
	plt.draw_all()


fig = plt.figure()
ax = fig.add_subplot(111)
n = 0;
nn = 0;
press = False
x = [0,0,0]
y = [0,0,0]

ax.plot([-1,-1,1,1],[-1,1,1,-1], color="#000080")

pressid = fig.canvas.mpl_connect('button_press_event', onclick)
moveid = fig.canvas.mpl_connect('motion_notify_event', onmotion)
releaseid = fig.canvas.mpl_connect('button_release_event', onrelease)
plt.show()
print('end')
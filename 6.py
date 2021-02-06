import random
import matplotlib.pyplot as plt
import numpy

random.seed(version=2)

def get_percentile(values, bucket_number):
	a = [0.0]
	for i in range(1,bucket_number):
		a.append(numpy.percentile(values, (100 * i)//bucket_number))
	return a

def get_percentile_number(value, percentiles):
	n = 0
	while ((n < len(percentiles)) and (percentiles[n]<=value)):
		n += 1
	return n

def value_equalization(value, percentiles, add_random = False):
	idx = get_percentile_number(value, percentiles)
	step = 1/len(percentiles)
	if add_random:
		return idx*step + random.random()*step
	return idx*step

def values_equalization(values, percentiles, add_random=False):
	b = []
	for a in values:
		b.append(value_equalization(a,percentiles,add_random))
	return b

f = open("img.txt","r")
q = 0
data = [0]*200
for i in range(200):
	data[i] = [0]*267
	b = list(map(float,f.readline().split(' ')))
	for j in range(267):
		data[i][j] = b[j]
		q +=1

data = numpy.array(data)
percentiles = get_percentile(data, 10)
print(percentiles)
datanew = numpy.array(values_equalization(data.flatten(),percentiles,False))
print(q,len(datanew),200*267)
plt.imshow(datanew.reshape((200,267)), cmap = plt.get_cmap('gray')) 
plt.show()

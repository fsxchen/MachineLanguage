#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

dots = np.array([[1,6], [2,5], [3,7], [4,10]])

plt.plot([i[0] for i in dots], 
    [i[1] for i in dots], 'ro')

plt.axis([0, 6, 0, 12])


def nihezhixian(k, x, b):
    return k*x + b

sumxy = sum([a[0]*a[1] for a in dots])

#print sumxy

sumxx = sum([a[0] ** 2 for a in dots])
print sumxx

sumx = sum([a[0] for a in dots])
print sumx

sumy = sum([a[1] for a in dots])

#a0 = （∑Yi) / n - a1（∑Xi) / n （式1-8)
#a1 = [n∑Xi Yi - （∑Xi ∑Yi)] / [n∑Xi2 - （∑Xi)2 )] （式1-9)

# print dir(dots)
n = dots.shape[0]

k = float(n*sumxy - sumx*sumy)/float(n*sumxx - sumx*sumx)
# print a1 
b = float(sumy)/n - float(k * sumx) / n

plt.plot([i[0] for i in dots], 
    [nihezhixian(k, i[0], b) for i in dots])

plt.show()
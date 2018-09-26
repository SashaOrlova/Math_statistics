import random
import math
import matplotlib as mpl 
import matplotlib.pyplot as plt 
from functools import reduce


def fact(k):
	if (k == 1):
		return 1
	else:
		return k*fact(k-1)

def unif_rand(n, k, theta):
	random_values = [random.uniform(0, theta) for i in range(0, n)]
	sum = reduce((lambda x, y: x + y**k), random_values)
	return ((k+1)/n*sum)**(1/k)

def exp_rand(n, k, lambd):
	random_values = [random.expovariate(lambd) for i in range(0, n)]
	sum = reduce((lambda x, y: x + y**k), random_values)
	return (fact(k)*n/(sum))**(1/k)


def count_diff(theta, new_theta, n):
	sum = reduce((lambda x, y: x + y), [(theta - new_theta[i])**2 for i in range(0,n)])
	return math.sqrt(1/n*sum)

def count_all_uni(k):
	theta = 5
	n = 50
	new_theta = [unif_rand(n, k, theta) for i in range(0, n)]
	return count_diff(theta, new_theta, n)

def count_all_exp(k):
	theta = 5
	n = 50
	new_theta = [exp_rand(n, k, theta) for i in range(0, n)]
	return count_diff(theta, new_theta, n)

def generate_plot():
	dpi = 80
	fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
	mpl.rcParams.update({'font.size': 10})

	plt.axis([0, 20, 0, 6])

	plt.title('unif & exp')
	plt.xlabel('k')
	plt.ylabel('отклонение')

	xs = []
	uni_vals = []
	exp_vals = []

	x = 1 
	while x < 20:
		uni_vals += [count_all_uni(x)]
		exp_vals += [count_all_exp(x)]
		xs += [x] 
		x += 1 

	plt.plot(xs, uni_vals, color = 'blue', linestyle = 'solid',
	label = 'uniform')
	plt.plot(xs, exp_vals, color = 'red', linestyle = 'dashed',
		label = 'exp')

	plt.legend(loc = 'upper right')
	fig.savefig('ans.png')

generate_plot()
import random
import math

def G(y, a, c):
	if -math.log(-y/c) > a :
		return -math.log(-y/c)
	elif math.log(y/c) < -a:
		return math.log(y/c)
	else:
		return y/c

def expDist(y, a):
	return -math.log(y)/a

def decompose(x, a, c):
	if y < -a or y > a:
		1/2*(1-2*a*c)*expDistp(random.random(), a)
	else
		(2*a*c)*random.uniform(-a, a)

def methodInverseFunctions(a):
	return G(random.random(), a)

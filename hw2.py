from scipy.stats import chi2
from scipy.stats import norm
import matplotlib as mpl 
import matplotlib.pyplot as plt 

def getForN(n, gamma):
	return 1/chi2.ppf((1-gamma)/2, n) - 1/chi2.ppf((1+gamma)/2, n)


def getForNB(n, gamma):
	return n * 1/(norm.ppf((3-gamma)/4, n)**2) - 1/(norm.ppf((3+gamma)/4, n)**2)

def makePlot():
	dpi = 80
	fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
	mpl.rcParams.update({'font.size': 10})

	plt.axis([0, 1000, 0, 0.1])

	plt.title('Зависимость интервала')
	plt.xlabel('n')
	plt.ylabel('Длинна интервала')

	xs = []
	a_vals = []
	b_vals = []

	x = 10
	while x < 1000:
		a_vals += [getForN(x, 0.9)]
		b_vals += [getForNB(x, 0.9)]
		xs += [x] 
		x += 10 

	plt.plot(xs, a_vals, color = 'blue', linestyle = 'solid',
	label = 'a part')
	plt.plot(xs, b_vals, color = 'red', linestyle = 'solid',
	label = 'b part')

	plt.legend(loc = 'upper right')
	fig.savefig('ans.png')


makePlot()
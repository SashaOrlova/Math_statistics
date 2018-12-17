from scipy.stats import chi

def ege():
	percent_2017 = [7.92, 36.16, 25.09, 27.49, 3,34]
	percent_2018 = [3.85, 31.13, 32.96, 29.92, 2.13]
	count = 3.9 * 10**5

	nu_2017 = [x*count/100 for x in percent_2017]
	nu_2018 = [x*count/100 for x in percent_2018]

	nu_all = [x + y for (x, y) in zip(nu_2017, nu_2018)]

	sum = 0;
	for i in range(5):
		sum += ((nu_2017[i] - count*nu_all[i]/(2*count))**2)/(count*nu_all[i]/(2*count))
		sum += ((nu_2018[i] - count*nu_all[i]/(2*count))**2)/(count*nu_all[i]/(2*count))

	alpha = 0.05

	print(sum)
	print(chi.ppf(1 - alpha, 4))
	if (sum <= chi.ppf(1 - alpha, 4	)):
		print("ЕГЭ честное")
	else:
		print("Не очень честное")

def XiTheta(male, female, sumarry, theta):
	return (male - theta*theta*sumarry)**2/(sumarry*theta*theta) + (female - theta*theta*sumarry)**2/(sumarry*theta*theta)

def maleInFamily():
	male = 527
	female = 476
	sumarry = 2020
	if (XiTheta(male, female, sumarry, 0.5) < 3.84145):
		print("+")
	else:
		print("-")

ege()
maleInFamily()

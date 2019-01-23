
def nb_year(p0, percent, aug, p):
	population = p0
	temp = 0
	number_of_years = 0
	percent = percent/100
	print("p0: " + str(p0) + "\npercent: " + str(percent) + "\naug: " + str(aug) + "\np: " + str(p))
	while(True):
		if(number_of_years == 0):
			population = int(p0 + p0 * percent + aug)
			number_of_years += 1
			temp = population
			population = 0
		else:	
			population = int(temp + (temp * percent) + aug)
			temp = population
			population = 0
			number_of_years += 1
			if(temp >= p):
				break
	return number_of_years

print(nb_year(10823097,0.0885,54115,11472477))
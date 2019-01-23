"""
In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and 
moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its 
population greater or equal to p = 1200 inhabitants?

At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (number of inhabitants is an integer)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.
More generally given parameters:

p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)

the function nb_year should return n number of entire years needed to get a population greater or equal to p.

aug is an integer, percent a positive or null number, p0 and p are positive integers (> 0)

Examples:
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10
Note: Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 
2 you have to convert it to 0.02.
"""

def nb_year(p0, percent, aug, p):
	population = p0
	temp = 0
	number_of_years = 0
	percent = percent/100
	#print("p0: " + str(p0) + "\npercent: " + str(percent) + "\naug: " + str(aug) + "\np: " + str(p))
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

print(nb_year(1000, 2, 50, 1200))
print(nb_year(1500, 5, 100, 5000))
print(nb_year(1500000, 2.5, 10000, 2000000))
print(nb_year(1500000, 0.25, 1000, 2000000))

#tests
#print(nb_year(12858332,0.0479,64291,13436951))
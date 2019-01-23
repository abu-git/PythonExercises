def nb_year(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100. + aug
        year += 1
    return year


print(nb_year(1000, 2, 50, 1200))
print(nb_year(1500, 5, 100, 5000))
print(nb_year(1500000, 2.5, 10000, 2000000))
print(nb_year(1500000, 0.25, 1000, 2000000))

#tests
print(nb_year(12858332,0.0479,64291,13436951))
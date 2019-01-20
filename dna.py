"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for 
the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. 
DNA strand is never empty or there is no DNA at all (again, except for Haskell).
"""

def DNA_strand(dna):
	dnaList = list(dna)
	compList = []
	result = ""
	for symbol in dnaList:
		if(symbol == 'A'):
			compList.append('T')
		elif(symbol == 'T'):
			compList.append('A')
		elif(symbol == 'C'):
			compList.append('G')
		elif(symbol == 'G'):
			compList.append('C')
	for charac in compList:
		result = result + charac
	return result

print(DNA_strand("ATTGC"))
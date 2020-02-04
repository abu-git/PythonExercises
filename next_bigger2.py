"""
You have to create a function that takes a positive integer number and returns the next bigger 
number formed by the same digits:

	12 ==> 21
	513 ==> 531
	2017 ==> 2071

If no bigger number can be composed using those digits, return -1:

	9 ==> -1
	111 ==> -1
	531 ==> -1
"""

from itertools import permutations as permute

def next_bigger(n):
	string_n = str(n)
	result = list(map(''.join, permute(string_n)))
	result = list(dict.fromkeys(result))
	result.sort()
	#print(result)
	output = 0
	for i in result:
		if(int(i) > n):
			output = int(i)
			break
	if(output < n):
		return -1
	return output
	

	


#print(next_bigger(12))
#print(next_bigger(513))
#print(next_bigger(2017))
#print(next_bigger(414))
#print(next_bigger(144))
print(next_bigger(9123456780))
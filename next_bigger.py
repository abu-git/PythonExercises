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

def next_bigger(n):
	stringify = [int(i) for i in str(n)]
	result = 0
	string_result = ""
	if(len(stringify) == 1):
		return -1
	if(len(stringify) > 1):
		i = -1
		
		while(result < n):
			last_digit = stringify[i]
			before_last = stringify[i - 1]
			stringify[i] = before_last
			stringify[i - 1] = last_digit

			for c in stringify:
				string_result = string_result + str(c)
			result = int(string_result)
			i = i - 1
			if(result > n):
				break					
	if(result > n):
		return result
	

	


print(next_bigger(12))
print(next_bigger(513))
print(next_bigger(2017))
print(next_bigger(414))
#print(next_bigger(144))
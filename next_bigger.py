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
	i = len(stringify) - 1
	str_result = ""
	result = 0
	while(i != -1):
		last = stringify[i]
		before = stringify[i - 1]
		stringify[i] = before
		stringify[i - 1] = last
		for num in stringify:
			str_result = str_result + str(num)
		result = int(str_result)
		if(result > n):
			break
		else:
			str_result = ""
			stringify = [int(i) for i in str(n)]
		i-=1
	if(result <= n):
		return -1
	return result
	

	


print(next_bigger(12))
print(next_bigger(513))
print(next_bigger(2017))
print(next_bigger(414))
print(next_bigger(144))
print(next_bigger(1234567890))
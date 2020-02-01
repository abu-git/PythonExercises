"""
You are given an array (which will have a length of at least 3, but could be very large) containing 
integers. The array is either entirely comprised of odd integers or entirely comprised of even 
integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.

Examples:

	[2, 4, 0, 100, 4, 11, 2602, 36]
	Should return: 11 (the only odd number)

	[160, 3, 1719, 19, 11, 13, -21]
	Should return: 160 (the only even number)
"""

def find_outlier(integers):
	checker = []
	even = 0
	odd = 0
	for integer in integers:
		if(integer % 2 == 0):
			checker.append(0)
			even = even + 1
		if(integer % 2 != 0):
			checker.append(1)
			odd = odd + 1
	if(even > odd):
		return integers[checker.index(1)]
	if(odd > even):
		return integers[checker.index(0)]



print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
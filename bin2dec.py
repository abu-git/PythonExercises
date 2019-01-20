"""
Given an array of one's and zero's convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
"""
def binary_array_to_number(arr):
	arrLen = len(arr)
	result = 0
	for digit in arr:
		arrLen = arrLen - 1
		result = result + (digit * (2 ** arrLen))
	return result
print(binary_array_to_number([0,0,0,1]))
"""
Write a function called that takes a string of parentheses, and determines if the order of 
the parentheses is valid. The function should return true if the string is valid, and false 
if it's invalid.

Examples:
	"()"              =>  true
	")(()))"          =>  false
	"("               =>  false
	"(())((()())())"  =>  true

Constraints:
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. 
Furthermore, the input string may be empty and/or not contain any parentheses at all. 
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""

def valid_parentheses(string):
	checker = 0
	checkList = []
	checkBool = False
	if(len(string) == 0):
		return True
	for char in string:
		if(char == '('):
			checkList.append('(')
		elif(char == ')'):
			if(len(checkList) == 0):
				return False
			elif(len(checkList) != 0):
				checkList.pop()
				checkBool = True
		else:
			continue
	if(len(checkList) > 0):
		checkBool = False
	return checkBool


print(valid_parentheses("     ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))

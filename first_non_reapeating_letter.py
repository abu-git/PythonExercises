"""
Write a function named first_non_repeating_letter that takes a string input, and returns the first 
character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only 
occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the 
function should return the correct case for the initial letter. For example, the input 'sTreSS' 
should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see 
sample tests.
"""

def first_non_repeating_letter(string):
	index = 0
	result = ""
	prev = []
	for char in string:
		if(prev.count(char.lower()) >= 1):
			index = index + 1
			continue
		if(string[index + 1:].lower().find(char.lower()) == -1):
			result = char
			break
		index = index + 1
		prev.append(char.lower())
	return result


print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('a'))
print(first_non_repeating_letter('moonmen'))
print(first_non_repeating_letter(''))
print(first_non_repeating_letter('sTreSS'))
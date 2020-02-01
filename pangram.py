"""
A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it 
uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
Ignore numbers and punctuation.
"""

import string

def is_pangram(s):
	alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
	checker = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	string_format = s.strip('.!"0123456789')
	string_format = string_format.replace(",", "")
	string_format = string_format.lower()
	#print(string_format)
	for i in string_format:
		if(i == " "):
			continue
		for c in alphabets:
			if(i == c):
				checker[alphabets.index(i)] = 1
	boolean = False
	value = 0
	#print(checker)
	for number in checker:
		value = value + number
	if(value == 26):
		boolean = True	
	return boolean


pangram = "The quick, brown fox jumps over the lazy dog!"
pangram2 = "Cwm fjord bank glyphs vext quiz"
print(is_pangram(pangram2))
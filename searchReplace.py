def get_Input():
	original_string = input("Please enter a string: ")
	the_substring = input("Please enter the substring you wish to find: ")
	replacer = input("Please enter a string to replace the given substring: ")

	return search_Replace(original_string, replacer, the_substring)

#search and the substring with the replacer
def search_Replace(string, replacer, substring):
	if(string == ""):
		return ""
	elif(string[:len(substring)] == substring):
		return replacer + search_Replace(string[len(substring):], replacer, substring)
	else:
		return string[0] + search_Replace(string[1:], replacer, substring)

print(get_Input())
"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

	It must start with a hashtag (#).
	All words must have their first letter capitalized.
	If the final result is longer than 140 chars it must return false.
	If the input or the result is an empty string it must return false.

Examples:

	" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
	"    Hello     World   "                  =>  "#HelloWorld"
	""                                        =>  false
"""

def generate_hashtag(s):
	striped = s.strip()
	stripedList = striped.split(" ")
	result = "#"
	if(len(s) >= 139):
		return False
	if(s == ""):
		return False
	for word in stripedList:
		if(word != ""):
			result = result + word[0].upper()
			result = result + word[1:].lower()
	return result

print(generate_hashtag("    banana    "))
print(generate_hashtag("    banana is nice    "))
print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag(""))
print(generate_hashtag('Codewars'))
print(generate_hashtag('Codewars      '))
print(generate_hashtag('Codewars Is Nice'))
print(generate_hashtag('codewars is nice'))
print(generate_hashtag('CodeWars is nice'))
print(generate_hashtag('c i n'))
print(generate_hashtag('codewars  is  nice''Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))
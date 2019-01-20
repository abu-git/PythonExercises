#this code removes the vowels in a string

def disemvowel(string):
    string = string.replace('a', '')
    string = string.replace('e', '')
    string = string.replace('i', '')
    string = string.replace('o', '')
    string = string.replace('u', '')
    return string



print(disemvowel("This website is for losers LOL!"))
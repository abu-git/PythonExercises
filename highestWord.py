"""Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""

def high(x):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    sentenceArray = x.split(" ")
    resultArray = []
    theSum = 0
    for word in sentenceArray:
    	for i in range(len(word)):
    		theSum += alphabet.index(word[i])
    		theSum += 1
    	resultArray.append(theSum)
    	theSum = 0
    return(sentenceArray[resultArray.index(max(resultArray))])


print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))
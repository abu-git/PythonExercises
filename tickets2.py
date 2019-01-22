"""
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. 
Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the 
order people follow in the line?

Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

Examples:
tickets([25, 25, 50]) # => YES 
tickets([25, 100]) # => NO. Vasya will not have enough money to give change to 100 dollars
tickets([25, 25, 50, 50, 100]) # => NO. Vasya will not have the right bills to give 75 dollars of change 
(you can't make two bills of 25 from one of 50)
"""

def tickets(people):
	print(people)
	vasya_wallet = [0,0,0]
	vasya_response = "NO"
	for cash in people:
		if(cash == 25):
			vasya_wallet[0] += 25
			vasya_response = "YES"
		elif(cash == 50):
			if(vasya_wallet[0] < 25):
				vasya_response = "NO"
				break
			elif(vasya_wallet[0] >= 25):
				vasya_wallet[0] -= 25
				vasya_wallet[1] += 50
				vasya_response = "YES"
		elif(cash == 100):
			if(vasya_wallet[0] < 25 or vasya_wallet[1] < 50):
				if(vasya_wallet[0] >= 75):
					vasya_wallet[0] -= 75
					vasya_wallet[2] += 100
					vasya_response = "YES"
				else:
					vasya_response = "NO"
					break
			elif(vasya_wallet[0] >= 75 and vasya_wallet[1] == 0):
				vasya_wallet[0] -= 75
				vasya_wallet[2] += 100
				vasya_response = "YES"
			elif(vasya_wallet[0] >= 25 and vasya_wallet[1] >= 50):
				vasya_wallet[0] -= 25
				vasya_wallet[1] -= 50
				vasya_wallet[2] += 100
				vasya_response = "YES"
	return vasya_response


print(tickets([25,25,50]))
print(tickets([25,100]))
print(tickets([25, 25, 50, 50, 100]))
print(tickets([25,25,25,100]))
print(tickets([25, 25, 25, 25, 50, 100, 50]))
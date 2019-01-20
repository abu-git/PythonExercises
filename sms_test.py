#An SMS Simulation
class SMSMessage(object):

	hasBeenRead = False
	messageText = ''
	fromNmber = 0

	def __init__(self, fromNmber):
		self.hasBeenRead = False
		self.fromNmber = fromNmber

	def MarkAsRead(self):
		hasBeenRead = True

#class TheInbox(SMSMessage):

	SMSStore = []

	def add_sms(self, text, number):
		sms_object = SMSMessage(number)
		sms_object.messageText = text
		SMSStore.append(sms_object)

	def get_count(self):
		count = len(SMSStore)
		return count

	def get_message(self, index):
		sms_object = SMSStore[index]
		sms_object.MarkAsRead()
		return sms_object.messageText

	def get_unread_messages(self):
		unread = []
		for sms in SMSStore:
			if(sms.hasBeenRead == False):
				unread.append(sms)
		return unread

	def remove(self):
		SMSStore.pop(0)


text1 = "Hey Didi!\nHow are you?"
text2 = "Please call me"


userChoice = ""

while userChoice != "quit":
    userChoice = input("What would you like to do - read/send/quit?")
    if userChoice == "read":
        #Place your logic here
        pass
    elif userChoice == "send":
        #Place your logic here
        pass
    elif userChoice == "quit":
        print ("Goodbye")
    else:
        print ("Oops - incorrect input")
        
                
            

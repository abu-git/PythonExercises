def increment_string(strng):
    stringLength =  len(strng)
    if strng[stringLength - 1].isdigit():
        stringList = list(strng)
        index= -1
        endOflist = []
        frontOfstrng = []
        for charac in stringList:
            index = index + 1
            if charac.isdigit():
                endOflist = stringList[index:]
                print("End of list" + str(endOflist))
                break
        number = ""
        for digit in endOflist:
            number = number + "" + digit
        print(number)
        if endOflist[0] == '0':
            #beginning zeroes
            pass
        else:
            number = int(number)
            number+=1
            frontOfstrng = strng[0:index]
            print("Front of list : " + str(frontOfstrng))
            strng = frontOfstrng + str(number)

    else:
    	strng = strng + '1'
    	print(strng)
    return strng

print(increment_string("foo1"))
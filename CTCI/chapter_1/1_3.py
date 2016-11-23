#URLify

def Urlify(inputString,numChars):
	charList = []
	for i in range(0,numChars):
		if inputString[i] == " ":
			charList.append("%20")
		else:
			charList.append(inputString[i])
	return "".join(charList)

print(Urlify('hello world    ',11))
# Given a string pattern of 0s, 1s, and ?s (wildcards), generate all 0-1 strings that match this pattern. 
# e.g. 1?00?101 -> [10000101, 10001101, 11000101, 11001101]. 
# You can generate the strings in any order that suits you.

def generatePattern(n):
	if len(n) == 1:
		if (n == "?"):
			return ["0","1"]
		else:
			return [n]

	generatedArrays = generatePattern(n[1:])

	returnArray = []
	if n[0] == "?":
		for i in generatedArrays:
			tempString1 = "0" + i
			tempString2 = "1" + i
			returnArray.append(tempString1)
			returnArray.append(tempString2)
	else:
		for i in generatedArrays:
			tempString = n[0] + i
			returnArray.append(tempString)
	
	print("n is equal to: ", n)			
	print ("we are returning", returnArray)
	return returnArray



print(generatePattern("1?00010?"))
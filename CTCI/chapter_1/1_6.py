def stringCompression(x):
	newStr = ""
	i = 0
	j = 1
	while(not j > len(x)):
		if (not j >= len(x) and x[i] == x[j]):
			j+=1
		else:
			newStr += x[i] + str(j-i)
			i = j
			j+=1
	return newStr if len(newStr) < len(x) else x

print(stringCompression("ssssssssddddddssss"))
print(stringCompression("abcdefghij"))

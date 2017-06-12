def palindromeCheck(str):
	letters = {}
	for i in str:
		if i != " ":
			letters[i] = letters.get(i,0) + 1

	singleOdd = False
	for i in letters:
		if letters[i] % 2!= 0:
			if not singleOdd:
				singleOdd = True
			else:
				return False

	return True
print(palindromeCheck("yoy"))
print(palindromeCheck("yo"))
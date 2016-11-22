#given two strings write a method to decide is one is a permutation of the other

def checkPermutation(string1,string2):
	
	#initialize a hashtable for the letters and the amount in each string
	letters = {}

	#add the letters to the hash table and increment
	for i in string1:
		if i not in letters:
			letters[i] = 1
		else:
			letters[i] += 1

	#decrement for each letter in the string as well to
	#check there are no more or less letters in the second string than the first
	for i in string2:
		if i not in letters:
			return False
		else:
			letters[i] -= 1
			if letters[i] < 0:
				return False

	return True

def checkPermutation2(string1,string2):
	if (sorted(string1) == sorted(string2)):
		return True
	else:
		return False
	
print(checkPermutation("test", "etst"))
print(checkPermutation("apple", "banana"))
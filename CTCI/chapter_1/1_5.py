def oneAway(str1, str2):
	len1 = len(str1)
	len2 = len(str2)
	if (abs(len1-len2)>1):
		return False

	first = str1 if len1 < len2 else str2
	second = str2 if len1 < len2 else str1

	i = 0 #shorter pointer
	j = 0 #longer pointer
	foundDiff = False
	while (i<len1 and j < len2):
		if 
		
print(oneAway("yoy", "you"))
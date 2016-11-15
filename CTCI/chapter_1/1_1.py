def uniqueString(x):
	s = set()
	for i in x:
		if i in s:
			return False
		else:
			s.add(i)
	return True

print(uniqueString("test"))
print(uniqueString("true"))
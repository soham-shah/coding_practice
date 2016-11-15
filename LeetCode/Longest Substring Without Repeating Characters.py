def LLS(s):
    ht = {}
    maxLength = 0
    tempLength = 0
    start = 0
    for (index, value) in enumerate(s):
        if value not in ht:
            ht[value]=index
            tempLength+=1
        #the value is in the hash table so check the max length
        else:
            if(maxLength < index-start+1):
                maxLength = index-start
                print(s[start:index])
            start = index
            ht = {}
            tempLength=0
    if(tempLength>maxLength):
        maxLength = tempLength
    return maxLength

print(LLS("abcabcbb"))
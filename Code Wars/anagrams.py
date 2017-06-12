

def anagrams(word, words):
    #your code here
    anagrams = []
    letters = {}
    for i in word:
        letters[i] = letters.get(i,0) +1
    
    for i in words:
        tempCount={}
        for j in i:
            tempCount[j] = tempCount.get(j,0) + 1
        
        for j in letters:
             if j in tempCount:
                 tempCount[j] -= letters[j]
        
        isAngram = True
        for j in tempCount:
            if tempCount[j] != 0:
                isAngram = False
        if isAngram:
            anagrams += i

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa']
# Test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])

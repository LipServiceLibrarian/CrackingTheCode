def pangram(s):
    alphabet = []
    s = s.lower()
    for c in s: 
        if c not in alphabet:    
            alphabet.append(c)
    if len(alphabet)>=26:
       return 'pangram'
    else:
        return 'not pangram'

s = raw_input().strip()
s = s.replace(" ", "")
res2 = pangram(s)
print res2

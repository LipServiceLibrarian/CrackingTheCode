# Implement a function which reverses a character string
# Judith Gammie
# 2nd April 2015

def reversestring(s):
    # more readable method
    charlist = [x for x in s]
    reverse = ''
    for i in range(len(s)-1, -1, -1):
        reverse+=s[i]
    print reverse
   
def lazyreversestring(s):

    print s[::-1]    


reversestring('welcome')
lazyreversestring('welcome')

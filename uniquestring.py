# Implement an algorithm to determine if a string has all unique characters
def uniquestring(s):
    uniquechars = []
    for i in s:
        if i in uniquechars:
            break
        else:
           uniquechars.append(i)

    if len(uniquechars) == len(s):
            print 'All characters in', s, 'are unique'
    else: 
        print 'Not all characters in', s, 'are unique'

# What if you cannot use additional data structures?
def betteruniquestring(s):
    if len(set(s)) == len(s):
        print 'All characters in', s, 'are unique'
    else:
        print 'All chacaters in', s, 'are not unique'

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

def betteruniquestring(s):
    if len(set(s)) == len(s):
        print 'All characters in', s, 'are unique'
    else:
        print 'All chacaters in', s, 'are not unique'

#uniquestring('cat')
#uniquestring('dad')
betteruniquestring('cat')
betteruniquestring('dad')

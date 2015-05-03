# Given two integers, L and R, find the maximum value of A xor B 
# where 1 <= L <= A <= B <= R <= 10^3
#
# Judith Gammie
# 3 May 2015

#!/usr/bin/python

def max_xor(l, r):
    max_val = 0
    temp = 0
    for i in range (l, r+1):
        for j in range (l, r+1):
           temp = i ^ j
           if (i < j) and (temp > max_val):
               max_val = temp
    return max_val

print max_xor(10, 15)


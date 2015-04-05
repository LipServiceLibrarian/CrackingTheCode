# Given two strings, write a method to determine if one is a permutation of the other
# Judith Gammie
# 5th April 2015

def string_permutation(s1, s2):  
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
        
def simple_string_permutation(s1, s2):
    if sorted(s1) == sorted(s2):
        return True

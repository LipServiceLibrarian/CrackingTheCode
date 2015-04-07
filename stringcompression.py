# Write a method to perform basic string cimpression using the counts of 
# repeated characters e.g. 'aabcccccaaa' would become 'a2b1c5a3'.
# If the compressed string would not be smaller than the original string
# then method returns the original string
#
# Judith Gammie
# 7th April 2015

def string_compression(s):
    compressed = ''
    current_char = ''
    current_char_count = 0
    for i in range (0, len(s)):
        if current_char == '':
            current_char = s[i]
            current_char_count += 1
        elif current_char == s[i]:
            current_char_count += 1
        elif current_char != s[i]:
            compressed += str(current_char)
            compressed += str(current_char_count)
            current_char = s[i]
            current_char_count = 1
    compressed += str(current_char)
    compressed += str(current_char_count)
    
    if len(compressed) < len(s):
        return compressed
    else:
        return s

print string_compression('aabcccccaaa')

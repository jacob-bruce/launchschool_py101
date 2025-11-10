# Write a function that takes two strings as arguments, 
# determines the length of the two strings, and then returns 
# the result of concatenating the shorter string, the longer string,
# and the shorter string once again. You may assume that the strings 
# are of different lengths.

def short_long_short(string1, string2):
    len_s1 = len(string1)
    len_s2 = len(string2)

    if len_s1 > len_s2:
        return string2 + string1 + string2
    else:
        return string1 + string2 + string1
    
print(short_long_short('abc', 'defg'))

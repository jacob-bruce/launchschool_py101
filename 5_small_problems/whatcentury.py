"""
Write a function that takes a year as input and returns the century. 
The return value should be a string that begins with the century number, 
and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

New centuries begin in years that end with 01. 
So, the years 1901 - 2000 comprise the 20th century.

P:
- Get a year, return a centry

E:
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True

D:
- input: int
- output: string

A:
- Convert int to string
- Find the length
- if length == 1 or 2 return 1st century
- else slice length minus 2

"""
def ordinal_num_ending(int_s):
    int_string_length = len(int_s)

    # Teens
    if int_string_length > 1 and int_s[-2] == '1': 
        return 'th'
    elif int_s[-1] == '1':
        return 'st'
    elif int_s[-1] == '2':
        return 'nd'
    elif int_s[-1] == '3':
        return 'rd'
    else:
        return 'th'

print(ordinal_num_ending('113'))

def century(year):
    # Coerce int into string
    year_string = str(year)

    # Save number of digits in year
    year_length = len(year_string)
    
    # Save number of digits in the century from year (1901 --> 2 (19))
    century_s_lenth = year_length - 2

    # Blank variable for result
    result = ''

    # Centuries with 1 or 2 digits are corner case
    if year_length == 1 or year_length == 2:
        return '1st'

    # Another corner case is years ending in 00
    if year_string[-2:] == '00':
        result = year_string[0:century_s_lenth]
    else:
        # Convert to int to add one and then back to string
        result = str(int(year_string[0:century_s_lenth]) + 1)
            
    cardinal_ending = ordinal_num_ending(result)
    result += cardinal_ending
    return result

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True

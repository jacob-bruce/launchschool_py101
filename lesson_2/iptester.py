def is_an_ip_number(test_str):
    if test_str.isdigit():
        number = int(test_str)
        return 0 <= number <= 255
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        print("IP address should have four components.")
        return False

    for string in dot_separated_words:
        if not is_an_ip_number(string):
            print("Invalid IP numbers.")
            return False
    
    print("Valid IP address.") 
    return True 


test_ip = input()
is_dot_separated_ip_address(test_ip)
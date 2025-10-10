famous_words = "seven years ago..."

# Method 1: '+'
def full_quote_maker(quote):
    full_quote = "Four score and " + quote
    print(full_quote)

full_quote_maker(famous_words)

# Method 2: f'-string
new_string = f'Four score and {famous_words}'
print(new_string)
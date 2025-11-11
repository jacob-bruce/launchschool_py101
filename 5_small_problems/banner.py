"""
Write a function that takes a short line of text and prints it within a box.

P:
- Take a string
- Create a banner big enough for the string
- Print the string within a banner

Ex:
print_in_box('To boldly go where no one has gone before.')
+--------------------------------------------+
|                                            |
| To boldly go where no one has gone before. |
|                                            |
+--------------------------------------------+


"""

def print_in_box(text):
    text_length = len(text)
    banner_length = text_length + 2

    bannerized_text = (f'+{'-' * banner_length}+\n'
                       f'|{' ' * banner_length}|\n'
                       f'| {text} |\n'
                       f'|{' ' * banner_length}|\n'
                       f'+{'-' * banner_length}+')
    return bannerized_text

print(print_in_box('To boldly go where no one has gone before.'))
print(print_in_box('Kaitlyn I love you'))
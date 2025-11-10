# Back in the stone age (before CSS), we used spaces to align things on the screen. 
# If we have a 40-character wide table of Flintstone family members, how can we 
# center the following title above the table with spaces?

family_table_length = 40
title = "Flintstone Family Members"
title_length = len(title)
required_spaces = family_table_length - title_length
each_side = required_spaces // 2
centered_title = " " * each_side + title + " " * each_side
print(centered_title)

# Easier Way
centered_title2 = title.center(40)
print(centered_title2)
# Build a program that asks the user 
# to enter the length and width of a room, 
# in meters, then prints the room's area 
# in both square meters and square feet.

FEET_PER_METER = 3.28084

def calculate_square_meters(length_m, width_m):
    return length_m * width_m

def calculate_square_footage(length_m, width_m):
    length_f = length_m * FEET_PER_METER
    width_f = width_m * FEET_PER_METER
    return length_f * width_f

user_length = int(input('==> What is the length of the room in meters? '))
user_width = int(input('==> What is the width of the room in meters? '))

user_square_meter = calculate_square_meters(user_length, user_width)
user_square_footage = calculate_square_footage(user_length, user_width)

print(f'The room is {user_square_meter} square meters.')
print(f'The room is {round(user_square_footage, 2)} square feet.')
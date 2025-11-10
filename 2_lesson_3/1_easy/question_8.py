# How can we add multiple items to our list (e.g., 'Dino' and 'Hoppy')? 
# Replace the call to append with another method invocation.

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
pets = ["Dino", "Hoppy"]
flintstones.extend(pets)
print(flintstones)

input_string = input("Enter a string: ")

num_vowels = 0
num_consonants = 0
num_spaces = 0
num_other = 0
vowels = "aeiouAEIOU"

for char in input_string:
    if char in vowels:
        num_vowels += 1
    elif char.isalpha():
        num_consonants += 1
    elif char.isspace():
        num_spaces += 1
    else:
        num_other += 1
        
print("Inputted String: ", input_string)
print("Vowels: ", num_vowels)
print("Consonants: ", num_consonants)
print("Spaces: ", num_spaces)
print("Other Characters ", num_other)
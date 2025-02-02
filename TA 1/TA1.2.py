total = 0
input_string = input("Input a string containing digits: ")

for char in input_string:
    if char.isdigit():
        total += int(char)
print("the sum is: ", total)
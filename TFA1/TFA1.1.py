firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
age = input("Enter your age: ")

fullname = firstname + " " + lastname
print(" ")
print("Full Name:", fullname)
print("Sliced Name: ", fullname[0:3])
sliced = fullname[0:3]
greeting = "Greeting Message: Hello, {}! Welcome. You are {} years old."
print(greeting.format(sliced, age))

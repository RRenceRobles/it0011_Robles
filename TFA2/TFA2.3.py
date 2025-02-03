lastname = input("Enter last name: ")
firstname = input("Enter first name: ")
age = input("Enter age: ")
number = input("Enter contact number: ")
course = input("Enter course: ")

f = open("TFA2\\student.txt", "a")
f.write("Last Name: " + lastname + "\n")
f.write("First Name: " + firstname + "\n")
f.write("Age: " + age + "\n")
f.write("Contact Number: " + number +"\n")
f.write("Course: " + course + "\n")

print("Student information has been saved to 'students.txt'")

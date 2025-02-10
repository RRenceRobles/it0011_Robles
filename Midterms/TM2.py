date_input = input("Enter the date (mm/dd/yyyy): ")
month, day, year = date_input.split('/')
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

output_format = "Date Output: {} {}, {}"
print(output_format.format(months[int(month)-1], int(day), year))

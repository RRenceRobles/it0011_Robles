import os
from tkinter import *
from tkinter import messagebox

# File where user data will be stored
FILE_NAME = "users.txt"

# Function to load user data from the file
def load_data():
    users = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 5:
                    users.append({
                        "first_name": parts[0],
                        "middle_name": parts[1],
                        "last_name": parts[2],
                        "birthday": parts[3],
                        "gender": parts[4]
                    })
    return users

# Function to save user data to the file
def save_data(users):
    with open(FILE_NAME, "w") as file:
        for user in users:
            file.write(f"{user['first_name']} | {user['middle_name']} | {user['last_name']} | {user['birthday']} | {user['gender']}\n")

# Function to handle user signup
def signup():
    try:
        users = load_data()
        user = {
            "first_name": entry_fname.get(),
            "middle_name": entry_mname.get(),
            "last_name": entry_lname.get(),
            "birthday": entry_bday.get(),
            "gender": gender_var.get()
        }
        users.append(user)
        save_data(users)
        messagebox.showinfo("Success", "User signed up successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to display all user records
def view_records():
    try:
        users = load_data()
        records_window = Toplevel()
        records_window.title("All Users")
        
        Label(records_window, text="First Name | Middle Name | Last Name | Birthday | Gender").pack(anchor='w')
        for user in users:
            Label(records_window, text=f"{user['first_name']} | {user['middle_name']} | {user['last_name']} | {user['birthday']} | {user['gender']}").pack(anchor='w')
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to search for a user by first or last name
def search_record():
    try:
        users = load_data()
        search_window = Toplevel()
        search_window.title("Search Results")
        
        found_users = [user for user in users if user['first_name'] == search_entry.get() or user['last_name'] == search_entry.get()]
        
        if found_users:
            for user in found_users:
                Label(search_window, text=f"{user['first_name']} | {user['middle_name']} | {user['last_name']} | {user['birthday']} | {user['gender']}").pack(anchor='w')
        else:
            Label(search_window, text="No record found").pack(anchor='w')
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main Tkinter window setup
root = Tk()
root.title("User Management System")
root.geometry("400x400")

frame = Frame(root)
frame.pack(padx=10, pady=10, anchor='w')

# Labels and input fields for user details
Label(frame, text="First Name:").grid(row=0, column=0, sticky='w')
entry_fname = Entry(frame)
entry_fname.grid(row=0, column=1)

Label(frame, text="Middle Name:").grid(row=1, column=0, sticky='w')
entry_mname = Entry(frame)
entry_mname.grid(row=1, column=1)

Label(frame, text="Last Name:").grid(row=2, column=0, sticky='w')
entry_lname = Entry(frame)
entry_lname.grid(row=2, column=1)

Label(frame, text="Birthday (YYYY-MM-DD):").grid(row=3, column=0, sticky='w')
entry_bday = Entry(frame)
entry_bday.grid(row=3, column=1)

# Gender selection
Label(frame, text="Gender:").grid(row=4, column=0, sticky='w')
gender_var = StringVar(value="Male")
Radiobutton(frame, text="Male", variable=gender_var, value="Male").grid(row=4, column=1, sticky='w')
Radiobutton(frame, text="Female", variable=gender_var, value="Female").grid(row=5, column=1, sticky='w')
Radiobutton(frame, text="Other", variable=gender_var, value="Other").grid(row=6, column=1, sticky='w')

# Buttons for user actions
Button(frame, text="Sign Up", command=signup).grid(row=7, column=0, columnspan=2, pady=5, sticky='w')
Button(frame, text="View All Records", command=view_records).grid(row=8, column=0, columnspan=2, pady=5, sticky='w')

# Search functionality
Label(frame, text="Search by First/Last Name:").grid(row=10, column=0, sticky='w')
search_entry = Entry(frame)
search_entry.grid(row=10, column=1)
Button(frame, text="Search", command=search_record).grid(row=11, column=0, columnspan=2, pady=5, sticky='w')

root.mainloop()

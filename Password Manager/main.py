from tkinter import *
from tkinter import messagebox
import string
import random

CAPS = string.ascii_uppercase
NUMBERS = '1234567890'
SPECIAL_CHARS = '!@#$%^&*-_=+.'

#PASSWORD GENERATOR
def generate_password():
    characters = string.ascii_uppercase+string.ascii_lowercase+SPECIAL_CHARS
    password = random.choice(string.ascii_uppercase)+random.choice(NUMBERS)
    for i in range(11):
        password+=random.choice(characters)
    password_form.delete(0, END)
    password_form.insert(0, password)    

#VALIDATE PASSWORD
def is_password_valid():
    if not any(char in SPECIAL_CHARS for char in password_form.get()):
        return False
    elif not any(i in CAPS for i in password_form.get()):
        return False
    elif not any(i in NUMBERS for i in password_form.get()):
        return False
    else: 
        return True 
    
#SAVE PASSWORD
def export_login():
    if not is_password_valid():
        messagebox.showinfo("Error", "Password should include a capital letter, number, and special character.")
    elif len(website_form.get()) < 1:
        messagebox.showinfo("Error", "Please enter a website name.")
    elif len(password_form.get()) < 6:
        messagebox.showinfo("Error", "Password should be at least six digits.")
    elif len(email_form.get()) < 1:
        messagebox.showinfo("Error", "Please enter an email address.")
    else:
        login = f'{website_form.get()} | {email_form.get()} | {password_form.get()}'
        file_name = "passwords.txt"
        with open(file_name, "a") as file:
            file.write(login + "\n")
        website_form.delete(0, END)
        password_form.delete(0, END)
        messagebox.showinfo("Success", "Your login has been saved!")

#USER INTERFACE
window = Tk()
window.title('Password Manager')
window.minsize(450, 300)
window.config(padx=20, pady=20)

#CANVAS
canvas = Canvas(width=150, height=170)
pic = PhotoImage(file="logo.png")
canvas.create_image(95, 80, image=pic)
canvas.grid(row=1, column=2)

#WEBSITE FORM
website = Label(text="Website:")
website.grid(row=2, column=0)
website_form = Entry(width=45)
website_form.grid(row=2, column=2, columnspan=2)
website_form.focus()

#EMAIL/USERNAME FORM
email = Label(text="Email/Username:")
email.grid(row=3, column=0)
email_form = Entry(width=45)
email_form.grid(row=3, column=2, columnspan=2)

#PASSWORD FORM
password = Label(text="Password:")
password.grid(row=4, column=0)
password_form = Entry(width=26)
password_form.grid(row=4, column=2)

#PASSWORD BUTTON
pw_button = Button(text="Generate Password", width=14, command=generate_password)
pw_button.grid(row=4, column=3)  

#ADD BUTTON
add = Button(text="Add", width=38, command=export_login)
add.grid(row=5, column=2, columnspan=2)
add.config(bg='white')







window.mainloop()
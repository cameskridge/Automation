from tkinter import *
import string
import random

#PASSWORD GENERATOR
def generate_password():
    characters = string.ascii_uppercase+string.ascii_lowercase+'!@#$%^&*-_=+.'
    password = random.choice(string.ascii_uppercase)+random.choice('1234567890')
    for i in range(11):
        password+=random.choice(characters)
    password_form.delete(0, END)
    password_form.insert(0, password)    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def export_login():
    login = f'{website_form.get()} | {email_form.get()} | {password_form.get()}'
    file_name = "passwords.txt"
    with open(file_name, "a") as file:
        file.write(login + "\n")

    
# ---------------------------- UI SETUP ------------------------------- #
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
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    generate_password = password_letters + password_symbols + password_numbers
    shuffle(generate_password)

    password = "".join(generate_password)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {

            "email": email,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(message="Please fill the empty field!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                messagebox.showinfo(message="Updated!")
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    if len(website) == 0 :
        messagebox.showinfo(message="Please fill the website field!")

    with open("data.json") as data_file:
        data = json.load(data_file)

        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        elif website not in data and len(website) != 0:
            messagebox.showinfo(title="Error", message=f" No password for {website} exist")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
generator_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=generator_image)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text="Website:", fg="Black")
website_label.grid(row=1, column=0)
email_label = Label(text="Email or Username:", fg="Black")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", fg="Black")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
search_button = Button(text="Search", width=10, fg="Black", command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", fg="Black", command=password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", fg="Black", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

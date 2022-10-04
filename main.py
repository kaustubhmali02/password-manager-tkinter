import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

DATA_FILE = "data.json"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = "".join(password_list)

    # Clear the password field for adding the newly generated random password
    password_text.delete(0, END)
    password_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH FUNCTION ------------------------------- #
def search():
    website = website_text.get()

    if len(website) == 0:
        messagebox.showerror(title="Error", message="Website is Empty")
    else:
        try:
            with open(file=DATA_FILE, mode="r", encoding='utf-8-sig') as data_file:
                data = json.load(data_file)
            if website in data.keys():
                email_key = "email"
                password_key = "password"
                messagebox.showinfo(title="Info", message=f"Below are saved details:"
                                                          f"\nEmail: {data[website][email_key]}"
                                                          f"\nPassword: {data[website][password_key]}")
            else:
                raise KeyError
        except FileNotFoundError:
            messagebox.showerror(title="Info", message="No Data File Found.")
        except KeyError:
            messagebox.showinfo(title="Info", message=f"{website} password is not saved yet!")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Error", message="Website or Password is empty.")
    else:
        try:
            with open(file=DATA_FILE, mode="r", encoding='utf-8-sig') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            # Creating a new data.json if not present
            with open(file=DATA_FILE, mode="w", encoding='utf-8-sig') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating the data with the new data
            data.update(new_data)

            with open(file=DATA_FILE, mode="w", encoding='utf-8-sig') as data_file:
                # Saving updated json
                json.dump(data, data_file, indent=4)
        finally:
            website_text.delete(0, END)
            password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
image = PhotoImage(file="logo.png")
logo_canvas = Canvas(width=200, height=200)
logo_canvas.create_image(100, 100, image=image)
logo_canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_text = Entry(width=32)
website_text.grid(column=1, row=1)
website_text.focus()
email_text = Entry(width=51)
email_text.grid(column=1, row=2, columnspan=2)
email_text.insert(0, "kaustubh@gmail.com")
password_text = Entry(width=32)
password_text.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_pass)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)

window.mainloop()

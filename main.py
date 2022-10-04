from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()

    if len(website) or len(password) != 0:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open(file="data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_text.delete(0, END)
                password_text.delete(0, END)
    else:
        messagebox.showerror("Error", message="Website or Password is empty.")


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
website_text = Entry(width=51)
website_text.grid(column=1, row=1, columnspan=2)
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

window.mainloop()

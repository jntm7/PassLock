import random
import string
import tkinter as tk
from tkinter import messagebox
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

def generate_password(length, num_uppercase, num_lowercase, num_digits, num_special, exclude_similar):

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation
    similar_chars = "O0I1l"

    if exclude_similar:
        uppercase = ''.join([c for c in uppercase if c not in similar_chars])
        lowercase = ''.join([c for c in lowercase if c not in similar_chars])
        digits = ''.join([c for c in digits if c not in similar_chars])
        special = ''.join([c for c in special if c not in similar_chars])

    if num_uppercase > length:
        raise ValueError("The number of uppercase letters exceeds the password length.")
    if num_uppercase + num_lowercase > length:
        raise ValueError("The number of uppercase and lowercase letters combined exceeds the password length.")
    if num_uppercase + num_lowercase + num_digits > length:
        raise ValueError("The number of uppercase, lowercase letters, and digits combined exceeds the password length.")
    if num_uppercase + num_lowercase + num_digits + num_special > length:
        raise ValueError("The total number of specified characters exceeds the password length.")

    password_chars = []
    password_chars.extend(random.choices(uppercase, k=num_uppercase))
    password_chars.extend(random.choices(lowercase, k=num_lowercase))
    password_chars.extend(random.choices(digits, k=num_digits))
    password_chars.extend(random.choices(special, k=num_special))

    all_chars = uppercase + lowercase + digits + special
    remaining_length = length - (num_uppercase + num_lowercase + num_digits + num_special)
    password_chars.extend(random.choices(all_chars, k=remaining_length))

    random.shuffle(password_chars)

    password = ''.join(password_chars)
    return password

def validate_integer_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                raise ValueError
            return value
        except ValueError:
            print(f"Please enter a valid integer between {min_value} and {max_value}.")

def validate_yes_no_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        else:
            print("Please enter 'y' or 'n'.")

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    strength = "Weak"
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        strength = "Very Strong"
    elif length >= 12 and has_upper and has_lower and has_digit:
        strength = "Strong"
    elif length >= 10 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif length >= 10 and has_upper and has_lower and has_digit:
        strength = "Moderate"
    elif length >= 8 and has_upper and has_lower and has_digit and has_special:
        strength = "Moderate"
    return strength

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        num_uppercase = int(uppercase_entry.get())
        num_lowercase = int(lowercase_entry.get())
        num_digits = int(digits_entry.get())
        num_special = int(special_entry.get())
        exclude_similar = exclude_similar_var.get()

        password = generate_password(length, num_uppercase, num_lowercase, num_digits, num_special, exclude_similar)
        strength = password_strength(password)

        password_label.config(text=f"Generated password: {password}")
        strength_label.config(text=f"Password strength: {strength}")

        if save_password_var.get():
            with open("generated_passwords.txt", "a") as file:
                file.write(password + "\n")
            messagebox.showinfo("Success", "Password saved to generated_passwords.txt")

    except ValueError as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Password Generator")

tk.Label(app, text="Enter the desired password length:").grid(row=0, column=0, sticky=tk.W)
length_entry = tk.Entry(app)
length_entry.grid(row=0, column=1)

tk.Label(app, text="Enter the number of uppercase letters:").grid(row=1, column=0, sticky=tk.W)
uppercase_entry = tk.Entry(app)
uppercase_entry.grid(row=1, column=1)

tk.Label(app, text="Enter the number of lowercase letters:").grid(row=2, column=0, sticky=tk.W)
lowercase_entry = tk.Entry(app)
lowercase_entry.grid(row=2, column=1)

tk.Label(app, text="Enter the number of digits:").grid(row=3, column=0, sticky=tk.W)
digits_entry = tk.Entry(app)
digits_entry.grid(row=3, column=1)

tk.Label(app, text="Enter the number of special characters:").grid(row=4, column=0, sticky=tk.W)
special_entry = tk.Entry(app)
special_entry.grid(row=4, column=1)

exclude_similar_var = tk.BooleanVar()
tk.Checkbutton(app, text="Exclude similar characters (O, 0, I, 1, l)", variable=exclude_similar_var).grid(row=5, columnspan=2, sticky=tk.W)

save_password_var = tk.BooleanVar()
tk.Checkbutton(app, text="Save password to file", variable=save_password_var).grid(row=6, columnspan=2, sticky=tk.W)

tk.Button(app, text="Generate Password", command=generate_and_display_password).grid(row=7, columnspan=2)

password_label = tk.Label(app, text="Generated password: ")
password_label.grid(row=8, columnspan=2)

strength_label = tk.Label(app, text="Password strength: ")
strength_label.grid(row=9, columnspan=2)

app.mainloop()
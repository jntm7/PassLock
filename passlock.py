import random
import string
import tkinter as tk
import pyperclip
import os
import sys
import subprocess
import json
from tkinter import filedialog, messagebox, Menu, font as tkfont
from ctypes import windll

# BASE PATH
if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

# ICON PATH
icon_path = os.path.join(base_path, "icon.ico")

# THEME PATH
themes_path = os.path.join(base_path, "themes.json")

# LOAD THEMES
with open(themes_path, "r") as file:
    themes = json.load(file)

# DEFAULT THEME
current_theme = "Default"

# DEFAULT SETTINGS
windll.shcore.SetProcessDpiAwareness(1)
is_dark_mode = False
def reset_to_default():
    global current_font_size, current_opacity
    current_font_size = 10
    current_opacity = 1.0
    change_font_size(current_font_size)
    change_opacity(current_opacity)
    change_window_size(500, 600)
    if is_dark_mode:
        toggle_dark_mode()

# RESET ENTRY FIELDS
def reset_form():

    length_entry.delete(0, tk.END)
    uppercase_entry.delete(0, tk.END)
    lowercase_entry.delete(0, tk.END)
    digits_entry.delete(0, tk.END)
    special_entry.delete(0, tk.END)
    
    password_output.config(text="")
    strength_label.config(text="")
    
    exclude_similar_var.set(False)
    save_password_var.set(False)

# EXIT APPLICATION
def exit_app():
    app.quit()

# PASSWORD GENERATION
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
    if length >= 15 and has_upper and has_lower and has_digit and has_special:
        strength = "Very Strong"
    elif length >= 15 and has_upper and has_lower and has_digit:
        strength = "Strong"
    elif length >= 12 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
    elif length >= 12 and has_upper and has_lower and has_digit:
        strength = "Moderate"
    elif length >= 10 and has_upper and has_lower and has_digit and has_special:
        strength = "Moderate"
    return strength

def generate_and_display_password():

    try:
        length = int(length_entry.get())
        num_uppercase = int(uppercase_entry.get())
        num_lowercase = int(lowercase_entry.get())
        num_digits = int(digits_entry.get())
        num_special = int(special_entry.get())
        
        if length <= 0:
            raise ValueError("Password length must be positive")
        if num_uppercase < 0 or num_lowercase < 0 or num_digits < 0 or num_special < 0:
            raise ValueError("Character counts cannot be negative")
        if num_uppercase + num_lowercase + num_digits + num_special > length:
            raise ValueError("Sum of character types exceeds password length")

        exclude_similar = exclude_similar_var.get()

        password = generate_password(length, num_uppercase, num_lowercase, num_digits, num_special, exclude_similar)
        strength = password_strength(password)

        password_output.config(text=password)
        strength_label.config(text=strength)

        if save_password_var.get():
            with open("generated_passwords.txt", "a") as file:
                file.write(password + "\n")
            messagebox.showinfo("Success", "Password saved to generated_passwords.txt")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


# SAVE PASSWORD
current_file_path = None

def save_password():
    global current_file_path
    if current_file_path:
        with open(current_file_path, "a") as file:
            file.write(password_output.cget("text") + "\n")
        messagebox.showinfo("Success", f"Password saved to {current_file_path}")
    else:
        save_password_as()

def save_password_as():
    global current_file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        current_file_path = file_path
        save_password()


def copy_to_clipboard():
    password = password_output.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first!")

def show_saved_passwords():
    file_path = "generated_passwords.txt"
    if os.path.exists(file_path):
        # Windows
        if os.name == 'nt':
            os.startfile(file_path)
        # MacOS
        elif platform.system() == 'Darwin':
            subprocess.Popen(['open', file_path])
        # Linux
        elif os.name == 'posix':
            subprocess.call(('xdg-open', file_path))
    else:
        messagebox.showinfo("No Saved Passwords", "No passwords have been saved yet!")

# LIGHT / DARK MODE
def toggle_dark_mode():
    global is_dark_mode
    if current_theme != "Default":
        messagebox.showinfo("Theme Conflict", "Dark mode is only available in the Default theme.")
        return

    is_dark_mode = not is_dark_mode

    if is_dark_mode:
        bg_color = "black"
        fg_color = "white"
        entry_bg = "gray15"
        button_bg = "gray20"
        button_fg = "white"
    else:
        bg_color = "SystemButtonFace"
        fg_color = "black"
        entry_bg = "white"
        button_bg = "SystemButtonFace"
        button_fg = "black"

    app.config(bg=bg_color)
    main_frame.config(bg=bg_color)
    
    for widget in main_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(bg=bg_color, fg=fg_color)
        elif isinstance(widget, tk.Entry):
            widget.config(bg=entry_bg, fg=fg_color)
        elif isinstance(widget, tk.Button):
            widget.config(bg=button_bg, fg=button_fg)
        elif isinstance(widget, tk.Checkbutton):
            widget.config(bg=bg_color, fg=fg_color)

    password_output.config(bg=bg_color, fg=fg_color)
    strength_label.config(bg=bg_color, fg=fg_color)

    menubar.config(bg=bg_color, fg=fg_color)
    for menu in (file_menu, password_menu, options_menu, font_size_menu, window_size_menu, opacity_menu, theme_menu, presets_menu):
        menu.config(bg=bg_color, fg=fg_color)

    for window in app.winfo_children():
        if isinstance(window, tk.Toplevel) and hasattr(window, 'update_theme'):
            window.update_theme()

def update_theme(theme_name):
    global current_theme, is_dark_mode
    if theme_name not in themes:
        return
    
    is_dark_mode = False

    current_theme = theme_name
    theme = themes[theme_name]

    app.config(bg=theme["bg"])
    main_frame.config(bg=theme["bg"])

    for widget in main_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(bg=theme["bg"], fg=theme["fg"])
        elif isinstance(widget, tk.Entry):
            widget.config(bg=theme["entry_bg"], fg=theme["fg"])
        elif isinstance(widget, tk.Button):
            widget.config(bg=theme["button_bg"], fg=theme["button_fg"])
        elif isinstance(widget, tk.Checkbutton):
            widget.config(bg=theme["bg"], fg=theme["fg"])
    
    password_output.config(bg=theme["bg"], fg=theme["fg"])
    strength_label.config(bg=theme["bg"], fg=theme["fg"])

    menubar.config(bg=theme["bg"], fg=theme["fg"])
    for menu in (file_menu, password_menu, options_menu, font_size_menu, window_size_menu, opacity_menu, theme_menu, tools_menu, presets_menu):
        menu.config(bg=theme["bg"], fg=theme["fg"])

    for window in app.winfo_children():
        if isinstance(window, tk.Toplevel) and hasattr(window, 'update_theme'):
            window.update_theme(theme_name)

def reset_dark_mode_to_default():
    global is_dark_mode
    is_dark_mode = False
    toggle_dark_mode()

def update_password_labels():
    bg_color = "black" if is_dark_mode.get() else "SystemButtonFace"
    fg_color = "white" if is_dark_mode.get() else "black"
    
    password_label.config(bg=bg_color, fg=fg_color)
    password_output.config(bg=bg_color, fg=fg_color)
    strength_label_text.config(bg=bg_color, fg=fg_color)
    strength_label.config(bg=bg_color, fg=fg_color)

# FONT SIZE
def change_font_size(size):
    global current_font_size
    current_font_size = size
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=current_font_size)
    text_font = tkfont.nametofont("TkTextFont")
    text_font.configure(size=current_font_size)
    app.update()

# WINDOW OPACITY
def change_opacity(opacity):
    global current_opacity
    current_opacity = opacity
    app.attributes('-alpha', current_opacity)

# WINDOW RESIZER
def change_window_size(width, height):
    app.geometry(f"{width}x{height}")

################################################################

# PASSWORD STRENGTH CHECKER

def open_password_checker():
    checker_window = tk.Toplevel(app)
    checker_window.title("Password Strength Checker")
    checker_window.geometry("300x250")
    checker_window.resizable(False, False)

    try:
        checker_window.iconbitmap(icon_path)
    except tk.TclError:
        print(f"Warning: Could not load icon from {icon_path}")

    tk.Label(checker_window, text="Enter a password to check:").pack(pady=10)
    password_entry = tk.Entry(checker_window, show="*", width=30)
    password_entry.pack(pady=5)

    result_label = tk.Label(checker_window, text="")
    result_label.pack(pady=10)

    canvas = tk.Canvas(checker_window, width=200, height=20, highlightthickness=0)
    canvas.pack(pady=10)

    def update_checker_theme(new_theme=None):
        if new_theme:
            theme = themes[new_theme]
        else:
            theme = themes[current_theme]
        
        if is_dark_mode:
            bg_color = "black"
            fg_color = "white"
            entry_bg = "gray15"
            button_bg = "gray20"
            button_fg = "white"
        else:
            bg_color = theme["bg"]
            fg_color = theme["fg"]
            entry_bg = theme["entry_bg"]
            button_bg = theme["button_bg"]
            button_fg = theme["button_fg"]

        checker_window.config(bg=bg_color)
        for widget in checker_window.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(bg=bg_color, fg=fg_color)
            elif isinstance(widget, tk.Entry):
                widget.config(bg=entry_bg, fg=fg_color)
            elif isinstance(widget, tk.Button):
                widget.config(bg=button_bg, fg=button_fg)
        canvas.config(bg=bg_color)

    update_checker_theme(current_theme)

    def check_strength():
        password = password_entry.get()
        strength = password_strength(password)
        result_label.config(text=f"Password Strength: {strength}")

        strength_colors = {"Weak": "red", "Moderate": "yellow", "Strong": "light green", "Very Strong": "dark green"}
        strength_values = {"Weak": 50, "Moderate": 100, "Strong": 150, "Very Strong": 200}

        canvas.delete("all")
        canvas.create_rectangle(0, 0, strength_values[strength], 20, fill=strength_colors[strength], outline="")

    check_button = tk.Button(checker_window, text="Check Strength", command=check_strength)
    check_button.pack(pady=20)

    checker_window.update_theme = update_checker_theme

# APP GUI
app = tk.Tk()
app.title("PassLock Password Generator")
app.geometry("500x600")
app.resizable(False, False)

script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "icon.ico")
try:
    app.iconbitmap(icon_path)
except tk.TclError:
    print(f"Warning: Could not load icon from {icon_path}")

app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.rowconfigure(7, weight=1)
app.rowconfigure(8, weight=1)
app.rowconfigure(9, weight=1)

################################################################

## MENU BAR

menubar = Menu(app)
app.config(menu=menubar)

# FILE

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Reset", command=reset_form)
file_menu.add_command(label="Save", command=save_password)
file_menu.add_command(label="Save As", command=save_password_as)
file_menu.add_command(label="Exit", command=exit_app)

# OPTIONS

options_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Options", menu=options_menu)

font_size_menu = Menu(options_menu, tearoff=0)
options_menu.add_cascade(label="Font Size", menu=font_size_menu)
font_size_menu.add_command(label="Small", command=lambda: change_font_size(8))
font_size_menu.add_command(label="Medium", command=lambda: change_font_size(10))
font_size_menu.add_command(label="Large", command=lambda: change_font_size(14))

window_size_menu = Menu(options_menu, tearoff=0)
options_menu.add_cascade(label="Window Size", menu=window_size_menu)
window_size_menu.add_command(label="Small", command=lambda: change_window_size(350, 420))
window_size_menu.add_command(label="Medium", command=lambda: change_window_size(500, 600))
window_size_menu.add_command(label="Large", command=lambda: change_window_size(800, 960))

opacity_menu = Menu(options_menu, tearoff=0)
options_menu.add_cascade(label="Window Opacity", menu=opacity_menu)
opacity_menu.add_command(label="25%", command=lambda: change_opacity(0.25))
opacity_menu.add_command(label="50%", command=lambda: change_opacity(0.50))
opacity_menu.add_command(label="65%", command=lambda: change_opacity(0.65))
opacity_menu.add_command(label="75%", command=lambda: change_opacity(0.75))
opacity_menu.add_command(label="85%", command=lambda: change_opacity(0.85))
opacity_menu.add_command(label="100%", command=lambda: change_opacity(1.0))
options_menu.add_separator()

presets_menu = Menu(options_menu, tearoff=0)
options_menu.add_cascade(label="Presets", menu=presets_menu)
presets_menu.add_command(label="Small", command=lambda: (change_font_size(8), change_window_size(350, 420)))
presets_menu.add_command(label="Medium", command=lambda: (change_font_size(10), change_window_size(500, 600)))
presets_menu.add_command(label="Large", command=lambda: (change_font_size(14), change_window_size(800, 960)))
options_menu.add_command(label="Reset to Default", command=reset_to_default)

# THEME

theme_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Themes", menu=theme_menu)
theme_menu.add_command(label="Arctic", command=lambda: update_theme("Arctic"))
theme_menu.add_command(label="Bamboo", command=lambda: update_theme("Bamboo"))
theme_menu.add_command(label="Chocolate", command=lambda: update_theme("Chocolate"))
theme_menu.add_command(label="Forest", command=lambda: update_theme("Forest"))
theme_menu.add_command(label="Lavender", command=lambda: update_theme("Lavender"))
theme_menu.add_command(label="Mint", command=lambda: update_theme("Mint"))
theme_menu.add_command(label="Ocean", command=lambda: update_theme("Ocean"))
theme_menu.add_command(label="Peach", command=lambda: update_theme("Peach"))
theme_menu.add_command(label="Slate", command=lambda: update_theme("Slate"))
theme_menu.add_command(label="Sunset", command=lambda: update_theme("Sunset"))
theme_menu.add_separator()
theme_menu.add_command(label="Default", command=lambda: update_theme("Default"))
theme_menu.add_command(label="Dark Mode (On/Off)", command=toggle_dark_mode)

# PASSWORD

password_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Password", menu=password_menu)
password_menu.add_command(label="Copy Password", command=copy_to_clipboard)
password_menu.add_command(label="Open Passwords", command=show_saved_passwords)

# TOOLS

tools_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Password Strength Checker", command=open_password_checker)

################################################################

# MAIN FRAME

main_frame = tk.Frame(app, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

for i in range(14):
    main_frame.grid_rowconfigure(i, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)

separator = tk.Frame(main_frame, height=2, bd=1, relief=tk.SUNKEN)
separator.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(15, 15))

tk.Label(main_frame, text="Enter the desired password length:").grid(row=1, column=0, sticky=tk.W)
length_entry = tk.Entry(main_frame, width=10)
length_entry.grid(row=1, column=1, sticky=tk.E, padx=10, pady=5)

tk.Label(main_frame, text="Enter the number of uppercase letters:").grid(row=2, column=0, sticky=tk.W)
uppercase_entry = tk.Entry(main_frame, width=10)
uppercase_entry.grid(row=2, column=1, sticky=tk.E, padx=10, pady=5)

tk.Label(main_frame, text="Enter the number of lowercase letters:").grid(row=3, column=0, sticky=tk.W)
lowercase_entry = tk.Entry(main_frame, width=10)
lowercase_entry.grid(row=3, column=1, sticky=tk.E, padx=10, pady=5)

tk.Label(main_frame, text="Enter the number of digits:").grid(row=4, column=0, sticky=tk.W)
digits_entry = tk.Entry(main_frame, width=10)
digits_entry.grid(row=4, column=1, sticky=tk.E, padx=10, pady=5)

tk.Label(main_frame, text="Enter the number of special characters:").grid(row=5, column=0, sticky=tk.W)
special_entry = tk.Entry(main_frame, width=10)
special_entry.grid(row=5, column=1, sticky=tk.E, padx=10, pady=5)

separator = tk.Frame(main_frame, height=2, bd=1, relief=tk.SUNKEN)
separator.grid(row=6, column=0, columnspan=2, sticky="ew", padx=10, pady=(15, 15))

exclude_similar_var = tk.BooleanVar()
exclude_similar_checkbutton = tk.Checkbutton(main_frame, text="Exclude similar characters (O, 0, I, 1, l)", variable=exclude_similar_var)
exclude_similar_checkbutton.grid(row=7, columnspan=2, sticky=tk.W)

save_password_var = tk.BooleanVar()
save_password_checkbutton = tk.Checkbutton(main_frame, text="Save password to file", variable=save_password_var)
save_password_checkbutton.grid(row=8, columnspan=2, sticky=tk.W)

generate_button = tk.Button(main_frame, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=9, column=0, columnspan=2, pady=10, sticky=tk.EW)

password_label = tk.Label(main_frame, text="Generated Password:")
password_label.grid(row=10, column=0, sticky=tk.W)
password_output = tk.Label(main_frame, text="")
password_output.grid(row=10, column=1, sticky=tk.E)

strength_label_text = tk.Label(main_frame, text="Password Strength:")
strength_label_text.grid(row=11, column=0, sticky=tk.W)
strength_label = tk.Label(main_frame, text="")
strength_label.grid(row=11, column=1, sticky=tk.E)

copy_button = tk.Button(main_frame, text="Copy Password to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=12, column=0, columnspan=2, pady=10, sticky=tk.EW)

show_passwords_button = tk.Button(main_frame, text="Show Saved Passwords", command=show_saved_passwords)
show_passwords_button.grid(row=13, column=0, columnspan=2, pady=10, sticky=tk.EW)

app.mainloop()
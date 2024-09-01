# PassLock

<img src="https://github.com/jntm7/PassLock/assets/108718802/737c5d25-b073-48dd-98cb-767bdc9b4a38.png" width=5% height=5%> A simple GUI that generates and saves customizable passwords.

## 📢 Features

### Customizable Password Generation

Generate passwords of desired length by specifying the number of:
  - uppercase letters: `A-Z`
  - lowercase letters: `a-z`
  - digits: `0-9`
  - special characters: ``!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~``
  - include/exclude similar characters: `O, 0, I, 1, l`

### Password Strength Checker

- Evaluate the strength of a provided password
- Evaluates the strength of the generated password:
`Weak - Moderate - Strong - Very Strong`

### Copy, Save & View Passwords

- Hide generated password by toggling password visibility
- Copy generated password to clipboard
- Save generated passwords to file: `generated_passwords.txt`
- Open `generated_passwords.txt` directly from the program

### Window Customization

- Select from three preset window configurations
- Change font size
- Change window size
- Change window opacity
- Toggle between light mode (default) and dark mode
- Select from 10 themes: "Arctic", "Bamboo", "Chocolate", "Forest", "Lavender", "Mint", "Ocean", "Peach", "Slate", "Sunset"

![showcase](https://github.com/user-attachments/assets/b6159c10-85b8-4f73-92ab-57aba4fddb67)

### Intuitive Interface

- Supports keyboard shortcuts:
    - Ctrl+G: Generate Password
    - Ctrl+C: Copy Password
    - Ctrl+S: Save Password
    - Ctrl+V: Toggle Password Visibility
    - Ctrl+O: Open Saved Passwords
    - Ctrl+B: Open Batch Generator
    - Ctrl+H: Open Password Strength Checker
    - Ctrl+D: Toggle Dark Mode
    - Ctrl+T: Change Theme
    - Ctrl+E: Exit Application
    - F1: View Keyboard Shortcuts
    - F2: Open Documentation

- Menu bar navigation makes all settings and tools easily accessible.

## ⚙️ Example Usage:

![passlock-demo](https://github.com/user-attachments/assets/d39247b2-a3f7-4735-aec6-11463955abd1)

## 🛠️ How To Use

Ensure that you have Python 3.6 or newer.

You can download it from the [Python Official Website](https://www.python.org/downloads/).

Tkinter should be included with most Python installations.

### Clone the Repository

```
git clone https://github.com/jntm7/PassLock.git
cd passlock
```

or [download the latest release](https://github.com/jntm7/PassLock/archive/refs/tags/v1.0.zip).

### Install & Run

- Install required packages:

```
pip install pyperclip
```

- Run the application:

```
py passlock.py
```

OR 

- Run the executable:

Simply open `passlock.exe` to launch the application.

### Enter Custom Parameters
- Enter the desired password length.
- Enter the number of each type of character.
- Specify whether to exclude similar characters.
- Specify whether to save the generated password to a file.

### Password Generation
- Click `Generate Password`, to display the generated password and its password strength, based on the parameters chosen.
- Click `Copy to Clipboard`, to copy the generated password, to be pasted somewhere of your convenience.
- Click `Show Saved Passwords`, to open `generated_passwords.txt` and view your saved passwords.

To generate multiple passwords in one instance using the same criteria, go to `Tools > Batch Generator`.

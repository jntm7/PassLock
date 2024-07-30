# PassLock

<img src="https://github.com/jntm7/PassLock/assets/108718802/737c5d25-b073-48dd-98cb-767bdc9b4a38.png" width=5% height=5%> A simple GUI that generates and saves customizable passwords.

## 📢 Features

### Customizable Password Generation

Generate passwords of desired length by specifying the number of:
  - uppercase letters: `A-Z`
  - lowercase letters: `a-z`
  - digits: `0-9`
  - special characters: ``!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~``

And specifying whether to include/exclude similar characters: `O, 0, I, 1, l`

### Password Strength Indicator

- Evaluates the strength of the generated password:
`Weak - Moderate - Strong - Very Strong`

### Save & View Passwords

- Option to save generated passwords to a file: `generated_passwords.txt`
- Option to open `generated_passwords.txt` directly from the program.

### Window Customization

- Option to toggle between light mode (default) and dark mode
- Option to change font size: small, medium (default), large
- Option to change window size: small, medium (default), large
- Option to change window opacity: 25%, 50%, 65%, 75%, 85%, 100% (default)

#### Themes

- Option to select from 10 different themes: "Arctic", "Bamboo", "Chocolate", "Forest", "Lavender", "Mint", "Ocean", "Peach", "Slate", "Sunset".


## ⚙️ Example Usage:

![showcase](https://github.com/user-attachments/assets/b6159c10-85b8-4f73-92ab-57aba4fddb67)

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

# PassLock

<img src="https://github.com/jntm7/PassLock/assets/108718802/737c5d25-b073-48dd-98cb-767bdc9b4a38.png" width=5% height=5%> A simple GUI that generates and saves customizable passwords.

## 📢 Features

### Customizable Password Generation

- Generate passwords of desired length.
- Specify the number of:

  - uppercase letters `A-Z`
  - lowercase letters `a-z`
  - digits `0-9`
  - special characters ``!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~``
 
- Include/exclude similar characters `O, 0, I, 1, l`


### Password Strength Indicator

- Evaluates the strength of the generated password:
`[Weak - Moderate - Strong - Very Strong]`

### Save & View Passwords

- Option to save generated passwords to a file (`generated_passwords.txt`).
- Option to open `generated_passwords.txt` directly from the program.

### Dark Mode

- Option to toggle between Light (default) and Dark mode.

## ⚙️ Example Usage:

![showcase](https://github.com/jntm7/PassLock/assets/108718802/fa678a4e-750e-4ac3-99db-e8ff9d6267b9)


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

### Enter Custom Parameters
- Enter the desired password length.
- Enter the number of each type of character.
- Specify whether to exclude similar characters.
- Specify whether to save the generated password to a file.

### Password Generation
- Click `Generate Password`, to display the generated password and its password strength, based on the parameters chosen.
- Click `Copy to Clipboard`, to copy the generated password, to be pasted somewhere of your convenience.
- Click `Show Saved Passwords`, to open `generated_passwords.txt` and view your saved passwords.



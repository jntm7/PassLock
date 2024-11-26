<h1 align="center"><img src="https://github.com/jntm7/PassLock/assets/108718802/737c5d25-b073-48dd-98cb-767bdc9b4a38.png" width="5%" height="5%"></img>&nbsp;&nbsp;PassLock</h1>
<h3 align="center">Generate, Manage and Store Your Custom Passwords!</h3>
<hr>

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

### Password Encryption

- Built-in encryption option when generating passwords
- Encryption key is automatically copied to clipboard
- Encrypted passwords are stored separated from regular generated passwords

### Copy, Save & View Passwords

- Hide generated password by toggling password visibility
- Copy generated password to clipboard
- Save generated passwords to file: `generated_passwords.txt`
- Open `generated_passwords.txt` directly from the program

### Customization

- Preset window configurations
- Change font size
- Change window size
- Change window opacity
- Toggle between light mode (default) and dark mode
- Change colour theme

![showcase](https://github.com/user-attachments/assets/b6159c10-85b8-4f73-92ab-57aba4fddb67)

### Accessibility

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
    - F3: Sync to Cloud (Google Drive)

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

or [download the latest release](https://github.com/jntm7/PassLock/archive/refs/tags/v1.2.zip).

### Install & Run

- Install required packages:

```
pip install -r requirements.txt
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
- Click `Toggle Password Visibility`, to toggle visibility for enhanced privacy.
- Click `Copy Password to Clipboard`, to copy the generated password, to be pasted somewhere of your convenience.
- Click `Open Saved Passwords`, to open `generated_passwords.txt` and view your saved passwords.

#### Batch Generation
- Navigate to `Tools > Batch Generator`, to generate multiple passwords in one instance using the same criteria.

#### Password Encryption
- Click `Save as Encrypted Password`, to generate an encryption key and save to `encrypted_passwords.txt`.
- Click `Open Encrypted Passwords`, to open `encrypted_passwords.txt`.
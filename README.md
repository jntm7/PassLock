# PassLock
A simple GUI that generates customizable passwords.

## Features

### Customizable Password Generation

- Generate passwords of desired length.
- Specify the number of uppercase letters, lowercase letters, digits, and special characters.
- Option to exclude similar characters (O, 0, I, 1, l).

### Password Strength Indicator

- Evaluates the strength of the generated password (Weak, Moderate, Strong, Very Strong).

### Save Passwords

- Option to save generated passwords to a file ([generated_passwords.txt](generated_passwords.txt)).

### Dark Mode

- Option to toggle between Light (default) and Dark mode.

### Resizable Window

- Resize the window to your desired size.

## How To Use

Ensure that you have Python 3.6 or newer. You can download it from the [Python Official Website](https://www.python.org/downloads/).

Tkinter should be included with most Python installations.

### 1. Clone the Repository

```
git clone https://github.com/jntm7/PassLock.git
cd passlock
```

or [download the source files](https://github.com/jntm7/PassLock/archive/refs/heads/main.zip).

### 2: Install & Run

- Install required packages:

```
pip install pyperclip
```

- Run the application:

```
py passlock.py
```

### 3. Enter Custom Parameters
- Enter the desired password length.
- Enter the number of each type of character.
- Specify whether to exclude similar characters.
- Specify whether to save the generated password to a file.

### 4. Password Generation
- Click 'Generate Password', which will display the generated password and its password strength, based on the parameters chosen.
- Click 'Copy to Clipboard', which will copy the generated password, to be pasted somewhere of your convenience.

## Example Usage:

```
--------------------------------------------------------------
Enter the desired password length:                          15
Enter the number of uppercase letters:                      5
Enter the number of lowercase letters:                      5
Enter the number of digits:                                 3
Enter the number of special characters:                     2
--------------------------------------------------------------
[✓] Exclude similar characters (O, 0, I, 1, l)
--------------------------------------------------------------
[✓] Save password to file                                       
--------------------------------------------------------------
                    Generate Password
--------------------------------------------------------------
Generated password:                            hF#ic3r4uNV!2KZ
--------------------------------------------------------------
Password strength:                                 Very Strong
--------------------------------------------------------------
                Copy Password to Clipboard
--------------------------------------------------------------                    
```                 

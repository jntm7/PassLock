# PassLock
a simple console-based password generator built on Python.

## Features

### Customizable Password Generation:

- Generate passwords of desired length.
- Specify the number of uppercase letters, lowercase letters, digits, and special characters.
- Option to exclude similar characters (O, 0, I, 1, l).

### Password Strength Indicator:

- Evaluates the strength of the generated password (Weak, Moderate, Strong).

### Save Passwords:

- Option to save generated passwords to a file ([generated_passwords.txt](generated_passwords.txt)).


## How To Use

### 1. **Run the Application**:
- Clone or [download](https://github.com/jntm7/PassLock/archive/refs/heads/main.zip) the project and navigate to it.
- Execute the Python script in your terminal or command prompt:

```
py password.py
```

### 2. **Customize the Parameters**:
- Enter the desired password length.
- Enter the number of each type of character.
- Specify whether to exclude similar characters.
- Specify whether to save the generated password to a file.

### 3. **Password Generation**:
- The generated password and its password strength will be displayed.

## Example Usage:

```
Please answer the following questions:
--------------------------------------------------------------
Enter the desired password length:                          15
Enter the number of uppercase letters:                      6
Enter the number of lowercase letters:                      6
Enter the number of digits:                                 2
Enter the number of special characters:                     1
Exclude similar characters (O, 0, I, 1, l)? (y/n):          y
--------------------------------------------------------------
Generated password: 2J8cXDdZjpa\CwR
--------------------------------------------------------------
Password strength: Very Strong
--------------------------------------------------------------
Would you like to save this password to a file? (y/n):      y
--------------------------------------------------------------
Password was successfully saved to generated_passwords.txt
--------------------------------------------------------------
```

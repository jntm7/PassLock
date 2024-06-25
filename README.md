PassLock is a simple console-based password generator built on Python.

## Features

### Customizable Password Generation:

- Generate passwords of desired length.
- Specify the number of uppercase letters, lowercase letters, digits, and special characters.
- Option to exclude similar characters (O, 0, I, 1, l).

### Password Strength Indicator:

- Evaluates the strength of the generated password (Weak, Moderate, Strong).

### Save Passwords:

- Option to save generated passwords to a file (generated_passwords.txt).

### Example Usage:

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
import random
import string

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

    total_specified_chars = num_uppercase + num_lowercase + num_digits + num_special
    if total_specified_chars > length:
        raise ValueError("The total number of specified characters exceeds the password length.")

    password_chars = []
    password_chars.extend(random.choices(uppercase, k=num_uppercase))
    password_chars.extend(random.choices(lowercase, k=num_lowercase))
    password_chars.extend(random.choices(digits, k=num_digits))
    password_chars.extend(random.choices(special, k=num_special))

    all_chars = uppercase + lowercase + digits + special
    remaining_length = length - total_specified_chars
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

def main():
    print("==============================================================")
    print(" " * ((60 - len("Welcome to the Password Generator!")) // 2) + "Welcome to the Password Generator!")
    print("==============================================================")
    print()
    print("Please answer the following questions:")
    print("--------------------------------------------------------------")

    try:
        length = validate_integer_input("Enter the desired password length: ".ljust(60), min_value=1)
        num_uppercase = validate_integer_input("Enter the number of uppercase letters: ".ljust(60), min_value=0, max_value=length)
        num_lowercase = validate_integer_input("Enter the number of lowercase letters: ".ljust(60), min_value=0, max_value=length - num_uppercase)
        num_digits = validate_integer_input("Enter the number of digits: ".ljust(60), min_value=0, max_value=length - num_uppercase - num_lowercase)
        num_special = validate_integer_input("Enter the number of special characters: ".ljust(60), min_value=0, max_value=length - num_uppercase - num_lowercase - num_digits)
        exclude_similar = validate_yes_no_input("Exclude similar characters (O, 0, I, 1, l)? (y/n): ".ljust(60))

        password = generate_password(length, num_uppercase, num_lowercase, num_digits, num_special, exclude_similar)
        print("--------------------------------------------------------------")
        print(f"Generated password: {password}")
        print("--------------------------------------------------------------")
        print(f"Password strength: {password_strength(password)}")
        print("--------------------------------------------------------------")

        save_password = validate_yes_no_input("Would you like to save this password to a file? (y/n): ".ljust(60))
        if save_password:
            with open("generated_passwords.txt", "a") as file:
                file.write(password + "\n")
            print("--------------------------------------------------------------")
            print("Password successfully saved to generated_passwords.txt")
            print("--------------------------------------------------------------")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
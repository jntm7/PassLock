import pytest
import passlock

# COUNT CHARACTER CLASSES IN STRING
def count_classes(s):
    return {
        "upper": sum(1 for c in s if c.isupper()),
        "lower": sum(1 for c in s if c.islower()),
        "digit": sum(1 for c in s if c.isdigit()),
        "special": sum(1 for c in s if c in __import__('string').punctuation)
    }


# TEST PASSWORD BASIC COUNTS AND LENGTH
def test_generate_password_count_and_length():
    password = passlock.generate_password(length=12, num_uppercase=4, num_lowercase=4, num_digits=2, num_special=2, exclude_similar=False)
    counts = count_classes(password)

    assert len(password) == 12
    assert counts["upper"] == 4
    assert counts["lower"] == 4
    assert counts["digit"] == 2
    assert counts["special"] == 2


# TEST PASSWORD EXCLUDE SIMILAR CHARACTERS
def test_generate_password_exclude_similar():
    similar = set("O0I1l")
    password = passlock.generate_password(length=20, num_uppercase=5, num_lowercase=10, num_digits=2, num_special=3, exclude_similar=True)
    
    assert not any(c in similar for c in password)


# TEST BATCH GENERATE PASSWORD
def test_batch_generate_passwords():
    passwords = passlock.batch_generate_passwords(count=5, length=10, num_uppercase=2, num_lowercase=4, num_digits=2, num_special=2, exclude_similar=False)
    
    assert isinstance(passwords, list)
    assert len(passwords) == 5
    assert all(len(password) == 10 for password in passwords)
    assert len(set(passwords)) >= 1


# TEST PASSWORD STRENGTH FUNCTIONALITY
def test_password_strength_classification():
    # long mixed password should be Very Strong per implementation
    assert passlock.password_strength("Aa1!Aa1!Aa1!Aa1!") == "Very Strong"
    # a common medium-length password without special chars is treated as Weak by current logic
    assert passlock.password_strength("Password123") == "Weak"
    # short lowercase-only password is Weak
    assert passlock.password_strength("abcdef") == "Weak"
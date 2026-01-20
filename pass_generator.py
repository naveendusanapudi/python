import random
import string

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    all_chars = lowercase + uppercase + digits + special_chars
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars),
    ]
    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password) 

    return ''.join(password)

try:
    length = int(input("Enter password length: "))
    if length < 8:
        print("Password length should be at least 8")
    else:
        pwd = generate_password(length)
        print("Generated Password:", pwd)
except ValueError:
    print("Please enter a valid number")

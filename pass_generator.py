import random
import string
def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    all_chars = lowercase + uppercase + digits + special_chars
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password
try:
    length = int(input("Enter password length: "))
    if length < 8:
        print("Password length should be at least 8")
    else:
        pwd = generate_password(length)
        print("Generated Password:", pwd)
except ValueError:
    print("Please enter a valid number")

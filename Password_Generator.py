# Project 2: Automated Password Generator
# Created by: Aditya Rathore

import random
import string

print("=== Welcome to the Automated Password Generator ===")

# 1. Get the desired password length from the user
try:
    password_length = int(input("Enter the desired length of your password (minimum 6 characters): "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

# 2. Enforce a minimum safety length
if password_length < 6:
    print("Security Alert: Passwords shorter than 6 characters are too weak! Setting length to 6.")
    password_length = 6

# 3. Define the character pools using Python's built-in string module
lowercase_chars = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
uppercase_chars = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
number_chars = string.digits              # 0123456789
special_chars = string.punctuation         # !@#$%^&*()_+...

# 4. Combine all character sets into one pool
all_characters = lowercase_chars + uppercase_chars + number_chars + special_chars

# 5. Generate a secure, random password using a loop
generated_password = ""
for _ in range(password_length):
    random_character = random.choice(all_characters)
    generated_password += random_character

# 6. Display the final secure password
print("\n================ SECURE CRYPTO OUTPUT ================")
print(f"Password Length  : {password_length} characters")
print(f"Your Safe Password: {generated_password}")
print("======================================================")
print("Tip: Never share your passwords with anyone!")


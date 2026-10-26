import random
import string

def generate_password():
    while True:
        password_length = input("Enter password length: ").strip()
        if not password_length.isdigit():
            print("Invalid length")
        elif int(password_length) < 6:
            print("Password length must be at least 6")
        else:
            password_length = int(password_length)
            break
    is_uppercase = input("Include upper letters? (yess/no): ").strip().lower()
    is_specialchar = input("Include special characters? (yess/no): ").strip().lower()
    is_digits = input("Include digits? (yess/no): ").strip().lower()

    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase if is_uppercase == "yes" else ""
    special_char = string.punctuation if is_specialchar == "yes" else ""
    digits = string.digits if is_digits == "yes" else ""

    all_char = lower_letters + upper_letters + special_char + digits

    required_characters = []
    if is_uppercase == "yes":
        required_characters.append(random.choice(upper_letters))
    if is_specialchar == "yes":
        required_characters.append(random.choice(special_char))
    if is_digits == "yes":
        required_characters.append(random.choice(digits))

    remaining_length = password_length - len(required_characters)
    password = required_characters

    for _ in range(remaining_length):
        character = random.choice(all_char)
        password.append(character)

    random.shuffle(password)
    str_password = "".join(password)

    return str_password

password = generate_password()
print(password)

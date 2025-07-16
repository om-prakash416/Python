import random
import string

def generate_password(length,use_uppercase=True,use_numbers=True,use_special_chars=True):
    lowercase_letters =string.ascii_lowercase
    uppercase_letters =string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special_chars else ""
    
    all_chars = lowercase_letters + uppercase_letters + numbers + special_chars
    
    if not all_chars:
        raise ValueError("At least one character set must be enabled")
    
    
    password =[]
    if use_uppercase:
        password.append(random.choice(uppercase_letters))

    if use_numbers:
        password.append(random.choice(numbers))
    if use_special_chars:
        password.append(random.choice(special_chars))
        
    remaining_length = length - len(password)

    password.extend(random.choices(all_chars, k=remaining_length))

    random.shuffle(password)

    return ''.join(password)

try:
    length =int(input("Enter the desired password length (minimum 6): "))
    if length < 6:
        raise ValueError("Password length must be at least 6 characters")
    

    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print(f"Generated Password: {password}")
    
except ValueError as e:
    print(f"Error: {e}")
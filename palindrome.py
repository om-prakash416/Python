def is_palindrome(n):
    original_str = str(n)
    reversed_str = original_str[::-1]
    return original_str == reversed_str

number = int(input("Enter a number: "))

if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
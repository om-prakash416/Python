#Write a Program to print letters of string “Silver Oak University
#except e and s.

input_string = "Silver Oak University"

exclude_chars = ['e','s']

for char in input_string:
    if char.lower() not in exclude_chars:
        print(char,end="")
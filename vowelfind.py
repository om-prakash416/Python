# Write a Python Program to Find Vowels From a String.

import string


def get_vowels(String):
    
   return [each for each in String if each.lower() in "aeiou"]
# get_string1 = "hello"
# get_string2 = "pythone is fun"
# get_string3 = "coding compiler"
# get_string4 = "12345xyz"

# print("the vowels are: ",get_vowels(get_string1 ))
# print("the vowels are: ",get_vowels(get_string2))
# print("the vowels are: ",get_vowels(get_string3 ))
# print("the vowels are: ",get_vowels(get_string4))

String = input("Enter the string to check/find vowels in it: ")

print("The vowels in the word or sentence '{0}' are: {1}".format(String, get_vowels(String)))
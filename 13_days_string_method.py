# strings are immutable

a = "!! omprakash!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("om", "John"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("a"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))
# print(str1.index("ishh"))


str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str2 = "hello world"
print(str2.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "  # using Spacer
print(str1.isspace())
str2 = "  "  # using Tab
print(str2.isspace())


str1 = "World Health Organization"
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())


str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())


str1 = "His name is Dan. Dan is an honest man."
print(str1.title())
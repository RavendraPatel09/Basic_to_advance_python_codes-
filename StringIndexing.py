#Once a string is created, it cannot be changed. However, you can create new strings based on existing ones using indexing and slicing.
#string is immutable
#we can access individual characters in a string using indexing. In Python, string indices start at 0.
#we can access or print using [index] within square brackets.
#if we change the index it always gives a new string
#we can also use negative indexing to access characters from the end of the string. The last
s="Hello, World!"
print(s[0])        # H
print(s[7])        # W
print(s[-1])       # !
print(s[-5])       # o
print(s[0:13])# Hello, World! entire string
print(s[-13:-1])# Hello, World without last character
print(s[-13:])# Hello, World! entire string
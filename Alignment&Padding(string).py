# Alignment and Padding
s = 'hello'#This is used to add more characters to a string to make it a certain length.
ljust=s.ljust(10, '*')  # Left align with padding
print(ljust)  # Output: 'hello*****'
print(type(ljust))#<class 'str'>
print(id(ljust))#id of the new string
print(id(s))#id of the original string
s1='samarth'
rjust1=s1.rjust(18)# Right align with default space padding
print(rjust1)  # Output: '          samarth'
center1=s1.center(20,'-')# Center align with '-' padding
print(center1)  # Output: '------samarth-------'
# Demonstrating that original strings remain unchanged
print(s1)  # Output: 'samarth'  
#this helps us to format strings in a more readable way, especially when displaying tabular data or aligning text in console outputs.
# The original strings remain unchanged, as strings in Python are immutable.
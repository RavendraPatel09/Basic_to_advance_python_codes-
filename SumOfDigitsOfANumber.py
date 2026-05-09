n = int(input("Enter a number: "))
sum = 0
while n > 0:
    r = n % 10
    sum = sum + r# this will store the total sum of the num
    n= n //10
print("Sum of digits:", sum)
#with the help of while loop we can calculate the sum of digits of a number by extracting each digit using modulus operator and adding it to a sum variable, then removing the last digit by integer division until the number becomes 0.
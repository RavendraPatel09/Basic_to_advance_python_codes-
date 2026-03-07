n = int(input("Enter a positive integer: "))
i=0#initializing i to 0
sum=0#initializing sum to 0
while i<=n:#this loop will run until i is less than or equal to n
    sum = sum + i#adding i to sum
    i=i+1
print("The sum of first", n, "numbers is:", sum)#printing the sum
# This code calculates the sum of the first N natural numbers. It prompts the user to enter a positive integer N, then uses a while loop to iterate from 0 to N, adding each number to a cumulative sum. Finally, it prints the result.
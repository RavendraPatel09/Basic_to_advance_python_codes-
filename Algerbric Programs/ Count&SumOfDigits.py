num = 12345
count = 0
total = 0
while num > 0:
    digit = num % 10
    total += digit
    count += 1
    num //= 10
print("Count:", count)
print("Sum:", total)
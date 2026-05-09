import random

secret_number = random.randint(1, 10)
attempts = 0

print("I'm thinking of a number between 1 and 10.")

while True:
    guess = int(input("Take a guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You found it in {attempts} tries.")
        break
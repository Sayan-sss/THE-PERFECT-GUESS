# The Perfect Guess Game
import random

number = random.randint(1, 100)
attempt = 1
guess = int(input("Guess a number between 1 and 100: "))

while(True):
    if guess > number:
        guess = int(input("Your guess is too high. Try again: "))
        attempt += 1
    elif guess < number:
        guess = int(input("Your guess is too low. Try again: "))
        attempt += 1
    else:
        print(f"You got it! You guessed it in {attempt} attempts. The number was -", number)
        break

#Joriel Fairbanks
#9/24/2026
import random
number = random.randint(1,100)
guess = int(input("what is the number im thinking of 1-100"))
guesses = 0
guesses += 1
while guess > number or guess < number:
    if guess > number:
        print("Its lower")
        guess = int(input("what is the number im thinking of"))
        guesses += 1
    elif guess < number:
        print("Its higher")
        guess = int(input("what is the number im thinking of"))
        guesses += 1

print("Correct")
print("Your guessed",guesses,"times")
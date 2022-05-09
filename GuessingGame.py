import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
while chances<5:
    guess=int(input("Guess a number between 1 & 9:"))
    if guess==number:
        print("Congratulations You WON!")
        break
    elif guess < number:
        print("Guess a number greater than ", guess)
    else:
        print("Guess a number less than ", guess)
    chances+=1

if not chances<5:
    print("You Lose! The number is ", number )
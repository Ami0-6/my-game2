import random
secret=random.randint(1,10)
print("computer is guessing a number between 1 and 10 \n you have 5 attempts to guess")
n=0
while True:
    user_guess=int(input("enter your guess"))
    n+=1
    if user_guess > secret:
        print("your guess is too high try again")
    elif user_guess < secret:
        print("your guess is too low try again")
    elif user_guess==secret:
        print("your guess is correct you won!")
        break
    if n==5:
        print("you have attempted all 5 chances game over")
        break
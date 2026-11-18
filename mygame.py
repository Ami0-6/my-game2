# number guessing game, computer guesses a number user needs to guess it
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

# rock,paper,scissor game
import random
options=("rock","paper","scissior")
player=None
playing=True
while playing:
    player=input("enter your choice")
    computer=random.choice(options)
    print(f"computer choice {computer}")
    while player not in options:
        player=input("enter your choice (rock,paper,scissor)")
    if player==computer:
              print("its a tie")
    elif player=="rock" and computer=="scissior":
           print("you won")
    elif player=="paper" and computer=="rock":
            print("you won!")
    elif player=="scissor" and computer=="paper":
            print("you won")
    else:
            print("you lose")
    again=input("play again(y/n)").lower()
    if again!="y":
           playing=False
print("thanks for playing")

# dice rolling game
import random
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") unicode characters for ASCII art
# ● ┌ ─ ┐ │ └ ┘
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"
dice_art={
     1:("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2:(  "┌─────────┐",
         "│         │",
         "│         │",
         "│      ●  │",
         "└─────────┘"),
    3:(  "┌─────────┐",
         "│ ●       │",
         "│    ●    │",
         "│      ●  │",
         "└─────────┘"),
    4:(  "┌─────────┐",
         "│  ●    ● │",
         "│         │",
         "│  ●    ● │",
         "└─────────┘"),
    5:(  "┌─────────┐",
         "│ ●     ● │",
         "│    ●    │",
         "│  ●    ● │",
         "└─────────┘"),
    6:(  "┌─────────┐",
         "│ ●     ● │",
         "│ ●     ● │",
         "│ ●     ● │",
         "└─────────┘")
    
}
dice=[]
total=0
num_of_dice=int(input("how many dice?"))
for die in range(num_of_dice):
    dice.append(random.randint(1,6))
print(dice)
# for die in range(num_of_dice):             # these commented lines of code print the ASCII arts vertically
#     for line in dice_art.get(dice[die]):    # to get it horizontally i typed out the second line of code 
#         print(line)
for line in range(5):
  for die in dice:
      print(dice_art.get(die)[line],end="") 
  print()
for die in dice:
    total+=die
print(f"total {total}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Welcome to Rock, Paper and Scissors!")
Userchoice = int(
  input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("Your choice:")
if Userchoice == 0:
  print(rock)
elif Userchoice == 1:
  print(paper)
else:
  print(scissors)

import random

Choices = [rock, paper, scissors]

Computerchoice = random.choice(Choices)

print(f"Computer choice:\n {Computerchoice}")

if Userchoice == 0 and Computerchoice == scissors:
  print("You won!")
elif Userchoice == 0 and Computerchoice == paper:
  print("You lose!")
elif Userchoice == 1 and Computerchoice == rock:
  print("You won!")
elif Userchoice == 1 and Computerchoice == scissors:
  print("You lose!")
elif Userchoice == 2 and Computerchoice == rock:
  print("You lose!")
elif Userchoice == 2 and Computerchoice == paper:
  print("You won!")
else:
  print("Its a draw!")

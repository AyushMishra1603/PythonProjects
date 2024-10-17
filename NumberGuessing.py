import random
from Numberguessinglogo import logo

number = random.randint(1, 100)


def numberguessing():
  print("Welcome to the Number Guessing Game!")
  print(logo)
  print("I'm thinking of a number between 1 and 100.")
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return 10
  elif level == "hard":
    return 5
  else:
    print("You selected incorrect level")


def Levels(level):
  count = level
  for i in range(level):
    guess = int(input("Make a guess: "))
    count -= 1
    if guess < number:
      print("You guessed too low.")
      print(f"You have {count} attempts remaining to guess the number.")
    elif guess > number:
      print("You guessed too high")
      print(f"You have {count} attempts remaining to guess the number.")
    elif guess == number:
      print("You guessed it! You win")
      break


Levels(numberguessing())

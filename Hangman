import random
from Hangman_words import word_list
import Hangman_art
from Hangman_art import stages
from Hangman_art import logo
# import Hangman_art
print(logo)
print("Welcome to the Hangman Game!")
# Randomly choosing a word using Hangman_words module
chosen_word = random.choice(word_list)
#Create a empty list
display = []
#For each letter in the chosen_word, add a "_" to the list 'display'
for dash in range(len(chosen_word)):
  display += "_"
print(display)

#Create a variable to track the mistakes created by user
lives = 6
#Create a variable to print the stages using module Hangman_arts.stages
countOfStages = 6
#Using while loop to check the user has made enough incorrect number of guesses.
while not lives == 0:

  #Take User's input and keep it in lower case
  guess = input("Guess a letter: ").lower()
  #Run a loop
  if guess in display:
    print(f"You have already guessed {guess}")
  for position in range(len(chosen_word)):
    #Assign the each element of the string "chosen_word" to the letter
    letter = chosen_word[position]
    #check if the user's guess and assigned value is equal
    if letter == guess:
      #Replace if the user guessed correct letter
      display[position] = letter

  print(display)
  print("--------------------------------")
  #Check if "_" is not present in display
  if "_" not in display:
    print("You win!")
#If the user did not guess the correct letter then reduce the life by one and print the stages of life
  if guess not in display:

    print(f"You guessed {guess}, that's not in  the word.You lost a life!")
    lives -= 1
    print(stages[countOfStages])
    countOfStages -= 1
    print("-------------------------------")
#If user made sufficient errors then print They have lost!
  if lives == 0:
    print("You lose.")
    print(stages[0])
print(f"Correct word is {chosen_word}")

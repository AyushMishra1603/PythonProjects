import random
from HigherLowerlogo import logo, vs
from HigherLowergamedata import data

#Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
def format_data(account):
  """Format the account data into printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

#Use if statement to check if user is correct.
def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and return a message."""""
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'
#Make the game repeatable
while game_should_continue:
  #Generate a random account from the game data.
  #Making account at position B because the next account at position A.
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Compare B: {format_data(account_b)}")
  
  #Ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  #Check if the guess is correct.
  ##Get  follower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  #Clear the screen between rounds.
  #Give user feedback on their guess.
  #Score keeping
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
    
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. final score: {score}.")

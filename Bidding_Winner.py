from replit import clear
#HINT: You can call clear() to clear the output in the console.
from DictArt import logo
print(logo)

bids = {}

def Winner(biddingRecords):
  highest_bid = 0
  for bidder in biddingRecords:
    bid_amount = biddingRecords[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      print(f"The winner is {bidder} with a bid of ${highest_bid}, Congratulations!")
Others = True
while Others == True:
  name = input("Enter your name: ")
  price = int(input("Enter you bidding price: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
  if should_continue == "no":
    Others = False
    clear()
    Winner(biddingRecords = bids)
  elif should_continue == "yes":
    clear()












print("Welcome to Pizza Store!")
size = input("What size of pizza would you like to order? S, M, L\n")
bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25

Pepperoni = input("Do you want Pepperoni to be added? Y or N\n")
if Pepperoni == "Y":
  if size == "S":
    bill += 2
  if size == "M" or "L":
    bill += 3

ExtraCheese = input("Do you want extra cheese? Y or N\n")
if ExtraCheese == "Y":
  bill += 1

print(f"Your total bill is ${bill}")

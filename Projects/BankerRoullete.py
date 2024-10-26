import random

#Enter the names of your friends!
Name = input("Please enter the name of your friends!\n")

#Placing the names into indexes of List
Name_List = Name.split(",")
ListLength = len(Name_List)
#Pick a random index number and store it in a variable
Randomchoice = random.randint(0, ListLength - 1)
#Assign random name into new variable
Billpayer = Name_List[Randomchoice]

print(Billpayer + " is going to pay the bills!")

#Second way to do the same thing:
import random

Name = input("Please enter the name of your friends!\n")
Name_List = Name.split(",")
Billpayer = random.choice(Name_List)
print(Billpayer + " is going to pay the bills!")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first_choice = input("Your are at a crossroad. Please type LEFT or RIGHT. \n")
if first_choice.lower() == "left":
  second_choice = (input("Good choice, you made it to a lake! There is an island in the middle, choose to WAIT or instead SWIM to go for it. \n"))

  if second_choice.lower() == "wait":
    third_choice = input("Yes! You made it to the island unharmed. There is a castle with 3 colored doors, pick one to find the treasure : RED, YELLOW or BLUE.\n")
    
    if third_choice.lower() == "yellow":
      forth_choice = ("You won a treasure!")
      print(forth_choice)
    elif third_choice.lower() == "red":
      print("Game over, you got burnt by fire.")
    elif third_choice.lower() == "blue":
      print("Game over, you got eaten by a lion!")
    else:
      print("No treasure here, game over!")
  else:
    print(input("Game over, you got attacked by a trout."))
else:
  print("Game over, you fell into a hole.")



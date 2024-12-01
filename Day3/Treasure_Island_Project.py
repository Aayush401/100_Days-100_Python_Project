from random import choice

print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
choice1=input('You\'re at a crossroad,where do you want to go ? Type "left" or "right"').lower()
if choice1=="left":
    choice2=input('You\'ve come to a lake.There is an island in the middle of the lake.Type"wait" to wait for a boat otherwise Type"swim" to swim across.').lower()
    if choice2=="wait":
        choice3=input("you arrive at the island unharmed.There is house with 3 doors. one is red second one is blue and third one is pink which one you choose").lower()
        if choice3=="red":
            print("it is a room of fire and you are cooked game over!")
        elif choice3=="pink":
            print("congretulation you win the treasure!!")
        elif choice3=="blue":
            print("it is a room of fire and you are cooked game over!")
        else:
            print("choose right door ")


    else:
        print("you fell in to a hell . Enjoy !!")


else:
    print("you fell in to a hell . Enjoy !!")

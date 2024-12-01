import random
from urllib.parse import uses_relative

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
img=[rock,paper,scissors]

user_choice=int(input("what do you choose? type 0 for rock,1 for paper or 2 for scissors\n"))
if user_choice>=0 and user_choice<=2:
    print(img[user_choice])
computer_choice=random.randint(0,2)
print(f"computer choice:")
print(img[computer_choice])

if user_choice==0 and computer_choice==2:
    print("you wins!")
elif computer_choice==0 and user_choice==2:
    print("you lose!")
elif computer_choice>user_choice:
    print("you lose!")
elif computer_choice==user_choice:
    print("draw")
elif user_choice>=3 and user_choice<=0:
    print("you typed invalid number you lose!!!")

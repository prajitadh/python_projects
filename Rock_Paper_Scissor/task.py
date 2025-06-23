import random

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
print("Lets play --> rock, paper, scissors")
user_input = int(input("Enter 0 for 'rock', 1 for 'paper' and 2 for 'scissors'\n"))
if user_input == 0:
    print(rock)
if user_input == 1:
    print(paper)
if user_input ==2:
    print(scissors)

computer_input = random.randint(0,2)
if computer_input == 0:
    print(rock)
if computer_input == 1:
    print(paper)
if computer_input ==2:
    print(scissors)
    #rules of game
if user_input == computer_input:
    print("Draw.")
elif user_input == 0 and computer_input == 1:
    print("You lose.")
elif user_input == 1 and computer_input == 0 :
    print("You win")
elif user_input == 0 and computer_input == 2:
    print ("You win")
elif user_input == 2 and computer_input == 0:
    print ("You lose")
elif user_input == 1 and computer_input == 2:
    print ("You lose")
elif user_input == 2 and computer_input == 1:
    print ("You win")
else:
    print("Invalid number")
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
option_names = ["Rock", "Paper", "Scissors"]
option_pics = [rock, paper, scissors]

print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Hi! Let's play Rock Paper Scissors.
------------------------------------------------------------------------------------------------------''')
user_choice = int(input("What's your choice? Type '0' for Rock, '1' for Paper or '2' for Scissors.\n"))
comp_choice = random.randint(0,2)
print("......................................................................................................")
if user_choice > 2 or user_choice < 0 :
    print("\nInvalid Input. You lose!")
else:
    user_choice_name = option_names[user_choice]
    comp_choice_name = option_names[comp_choice]
    user_choice_pic = option_pics[user_choice]
    comp_choice_pic = option_pics[comp_choice]
    print(f"\nYou chose : \n{user_choice_name}", user_choice_pic)
    print(f"\nComputer chose : \n{comp_choice_name}", comp_choice_pic)

    if user_choice == comp_choice:
        print(f"\nYou both chose {user_choice_name}.\nIt's a tie!")
    elif user_choice == 0 and comp_choice == 2:
        print(f"{user_choice_name} beats {comp_choice_name}.\nYou win!")
    elif user_choice == 1 and comp_choice == 0:
        print(f"{user_choice_name} beats {comp_choice_name}.\nYou win!")
    elif user_choice == 2 and comp_choice == 1:
        print(f"{user_choice_name} beats {comp_choice_name}.\nYou win!")
    else:
        print(f"{comp_choice_name} beats {user_choice_name}.\nYou lose!")
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


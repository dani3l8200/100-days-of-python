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
list_game = [rock, paper, scissors]
length_of_list = len(list_game) - 1
random_number_of_game = random.randint(0, length_of_list)

print('Welcome to Project 4 - Game Rock Pape Scissors')
choice = int(input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print(list_game[choice])
print(f'Computer choise:\n{list_game[random_number_of_game]}')
if choice == random_number_of_game:
    print('Is Empat!')
elif (choice == 0 and random_number_of_game == 1) or (choice == 2 and random_number_of_game == 0) or (choice == 1 and random_number_of_game == 2):
    print('You Lose!')
elif (choice == 1 and random_number_of_game == 0) or (choice == 0 and random_number_of_game == 2) or (choice == 2 and random_number_of_game == 1):
    print('You Win!')


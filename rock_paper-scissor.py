import random
# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice = int(input("Enter your choice: (0: Rock  1: Paper   2: Scissor)"))
choice_map = {0 : 'rock', 1: 'paper', 2:'scissors'}
figure_map = {0 : rock, 1: paper, 2:scissors}
print(f'You chose: {choice_map[choice]}\n {figure_map[choice]}')
cpu_choice = random.choice([0,1,2])
print(f'CPU chose: {choice_map[cpu_choice]}\n {figure_map[cpu_choice]}')
user_score = 0
if cpu_choice > choice:
    if cpu_choice == 2 and choice == 0:
        user_score = 1
elif cpu_choice == choice:
    user_score = -1
else:
    user_score = 1
if user_score > 0:
    print('You Win !!!')
elif user_score < 0:
    print('Game Draw')
else:
    print('CPU wins :(')

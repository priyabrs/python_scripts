from logging.config import valid_ident
from random import choice

class MenuException(Exception):
    pass

class Menu():
    def __init__(self) -> None:
        self.coffee_machine_image = '''
          ______________________
         (___________           |
           [XXXXX]   |          |
      __  /~~~~~~~\  |          |
     /  \|@@@@@@@@@\ |          |
     \   |@@@@@@@@@@||          |
         \@@@@@@@@@@||  ______  |
          \@@@@@@@@/ | |on|off| |
         __\@@@@@@/__|  ~~~~~~  |
        (____________|__________|
        |_______________________|
              '''

    def validate_user_choice(self, user_choice) -> str:
        try:
            if user_choice.lower() not in  ['espresso','latte','cappuccino', 'report', '2', '3' , 'turn off']:
                raise MenuException(f'Invalid choice {user_choice}. Please try again!!')
            else:
                return user_choice
        except Exception as menuEx:
            print(menuEx)

    def display_menu(self) -> str:
        print(self.coffee_machine_image)
        print('Welcome to CCD. Please choose your options:\n 1. Coffee(espresso/latte/cappuccino)\n 2. Report\n 3 Turn off')
        user_choice = input('Enter your choice: ')
        return self.validate_user_choice(user_choice)
    


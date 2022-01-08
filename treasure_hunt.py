import random
from turtle import color
# ASCII_treasure = '''
#                     ____...------------...____
#                _.-"` /o/__ ____ __ __  __ \o\_`"-._
#              .'     / /                    \ \     '.
#              |=====/o/======================\o\=====|
#              |____/_/________..____..________\_\____|
#              /   _/ \_     <_o#\__/#o_>     _/ \_   |
#              \_________\####/_________/
#               |===\!/========================\!/===|
#               |   |=|          .---.         |=|   |
#               |===|o|=========/     \========|o|===|
#               |   | |         \() ()/        | |   |
#               |===|o|======{'-.) A (.-'}=====|o|===|
#               | __/ \__     '-.\uuu/.-'    __/ \__ |
#               |==== .'.'^'.'.====|
#               |  _\o/   __  {.' __  '.} _   _\o/  _|
#               `""""-""""""""""""""""""""""""""-""""`
# '''

ASCII_font = '''
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888 
'''
direction = ['left', 'right']
action = ['swim', 'wait']
colour = ['red', 'blue']
print(ASCII_font)
print("\n\n Welcome to Treasure Island\n Your Mission is to find the treasure")
u_choice = input('Left or Right: ').lower()
if u_choice == random.choice(direction):
    u_choice = input('swim or wait: ').lower()
    if u_choice == random.choice(action):
        u_choice = input('Which door: (red or blue): ').lower()
        if u_choice == random.choice(colour):
            print('Game Over !!!')
        else:
            print('You Win!!!')
    else:
        print('Game Over !!!')
else:
    print('Game Over !!!')

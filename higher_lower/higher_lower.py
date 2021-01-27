from itertools import count
from game_data import data
import random
from asset import logo, vs
from replit import clear
import copy
import time

def get_random_user(list_obj = None):
    new_data = copy.deepcopy(data)
    if list_obj:
        new_data.remove(list_obj)
    return random.choice(new_data)

def check_user_data(user_data1, user_data2, higher_lower):
    if higher_lower.lower() == 'higher':
        if user_data1['follower_count'] > user_data2['follower_count']:
            return user_data1
        else:
            return user_data2
    else:
        if user_data1['follower_count'] < user_data2['follower_count']:
            return user_data1
        else:
            return user_data2


def main():
    correct_count = 0
    user_data1 = {}
    while True:
        clear()
        if not user_data1:
            user_data1 = get_random_user()
        user_data2 = get_random_user(user_data1)
        user_choice = input(f"Guess the follower count between {user_data1['name']} vs {user_data2['name']} : ")
        higher_lower = input('higher or lower: ')

        try:
            hl_count_user = check_user_data(user_data1, user_data2, higher_lower)
            if hl_count_user['name'].lower() != user_choice.lower():
                print(f'Wrong pick!!. Your win streak is : {correct_count}')
                break
            else:
                print('Correct Answer')
                time.sleep(1)
                correct_count += 1
                user_data1 = hl_count_user
        except Exception as ex:
            print(f'Wrong input {ex}')

if __name__ == '__main__':
    main()
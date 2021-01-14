import random
tries_map = {'easy':10, 'hard':10}

def cpu_number():
    return random.choice(range(1,101))

def match_num(cpu_num, user_num):
    if cpu_num > user_num:
        print('Too low')
        return False
    elif user_num > cpu_num:
        print('Too high')
        return False
    if cpu_num == user_num:
        return True
    

def main():
    level = input('Choose your level (hard/easy): ')
    try:
        tries = tries_map[level.lower()]
        cpu_num = cpu_number()
        while tries > 0:
            user_num = int(input('Guess the number: '))
            matched = match_num(cpu_num, user_num)
            if matched:
                print(f'Guessed correctly. The number is {user_num}')
                break
            if tries == 1:
                print('This is your last try. Please choose wisely.')
            tries -= 1

    except Exception as ex:
        print(f'Incorrect choice {ex}')

if __name__ == '__main__':
    main()

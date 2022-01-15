from pprint import pprint
from resource import MENU, resources, coffee_machine_image
from replit import clear

class InsufficientResourceException(Exception):
    pass
# import resource
cash_balance = 0

def amt_counter():
    denomination_map = {1:0, 2:0, 5:0, 10:0}
    print('Enter the number of coins for each denomination: ')
    for key in denomination_map.keys():
        denomination_map[key] = input(f'{key} Rupee: ')
    total_amt = 0
    for key,val in denomination_map.items():
        total_amt += int(key)*int(val)
    return total_amt

def coffee_maker(coffee_type):
    usr_amt = amt_counter()
    if usr_amt < MENU[coffee_type]['cost']:
        print(f'The amount provided is not enough. Returning amount: {usr_amt} Rupees')
    else:
        global cash_balance
        cash_balance += usr_amt
        try:
            resource_previous = dict(resources)
            for resource in resources.keys():
                resources[resource] -= MENU[coffee_type]['ingredients'][resource] 
                if resources[resource] < 0:
                    raise InsufficientResourceException(f'Insufficient resource to make {coffee_type}')
            change = usr_amt - MENU[coffee_type]['cost']
            print(f'Your {coffee_type} is ready. here is your change: {change} Rupees')
        except InsufficientResourceException as InEx:
            print(InEx)
            print('Current Inventory: ')
            for k,v in resource_previous.items():
                formatted_display(k,v)
            print('\nRequired Inventory: ')
            for k,v in MENU[coffee_type]['ingredients'].items():
                formatted_display(k,v)
            print(f'Returning amount: {usr_amt} Rupees')


def display_user_menu():
    print(coffee_machine_image)
    print('Welcome to CCD. Please choose your options:\n 1. Coffee(espresso/latte/cappuccino)\n 2. Report\n 3. Turn off')

def formatted_display(str1, str2, new_line = False):
    formatted_str = "{:<15} {:<15}".format(str1, str2)
    if new_line:
        formatted_str = '\n'+formatted_str
    print(formatted_str)

def display_report(resource_dict):
    formatted_display('Inventory', 'Quantity')
    formatted_display('---------', '--------')
    for key, val in resource_dict.items():
        formatted_display(key, val)
    formatted_display('Cash Balance', cash_balance, True)

def main():
    choice = 'y'
    while choice == 'y':
        clear()
        display_user_menu()
        user_choice = input('Enter your choice: ')
        if user_choice.lower() in ['espresso', 'latte', 'cappuccino']:
            coffee_maker(user_choice.lower())
        elif user_choice.lower() == 'report' or int(user_choice) == 2 :
            display_report(resources)
        else:
            break
        choice = input('Do you want to use again:(y/n) ').lower()
    
if __name__ == '__main__':
    main()
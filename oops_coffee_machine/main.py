from coffee import Coffee
from menu import Menu
from resource import Resource
from moneymachine import Moneymachine
from replit import clear

def create_coffee_types():
    espresso = Coffee('espresso', {"water": 50,"milk": 0,"coffee": 18}, 20)
    latte = Coffee('latte', {"water": 200,"milk": 150,"coffee": 24}, 30)
    cappuccino = Coffee('cappuccino', {"water": 250,"milk": 100,"coffee": 24}, 40)
    return {'espresso': espresso, 'latte':latte, 'cappuccino':cappuccino}

def get_denomination_map():
    denomination_map = {1:0, 2:0, 5:0, 10:0}
    print('Enter the number of coins for each denomination: ')
    for key in denomination_map.keys():
        denomination_map[key] = input(f'{key} Rupee: ')
    return denomination_map

def formatted_display(str1, str2, new_line = False):
    formatted_str = "{:<15} {:<15}".format(str1, str2)
    if new_line:
        formatted_str = '\n'+formatted_str
    print(formatted_str)

def coffee_maker(coffee, coffee_resource, user_money):
    denomination_map = get_denomination_map()
    user_money.denomination_map = denomination_map
    user_amt = user_money.count_total_amt()
    if user_amt < coffee.cost:
        print(f'The amount provided is not enough. Returning amount: {user_amt} Rupees')
    else:
        if coffee_resource.check_resource(coffee.ingredients):
            change = user_money.return_change(coffee.cost)
            user_money.update_cash_balance(coffee.cost)
            coffee_resource.update_resource(coffee.ingredients)
            print(f'Your coffee is ready!!. Here is your change {change} Rupees')
        else:
            print(f'Insufficient resource to make {coffee.name}')
            print('Current Inventory: ')
            for k,v in coffee_resource.__dict__.items():
                formatted_display(k,v)
            print('\nRequired Inventory: ')
            for k,v in coffee.ingredients.items():
                formatted_display(k,v)
            print(f'Returning amount: {user_amt} Rupees')

def create_report(coffee_resource, user_money):
    formatted_display('Inventory', 'Quantity')
    formatted_display('---------', '--------')
    for key, val in coffee_resource.__dict__.items():
        formatted_display(key, val)
    formatted_display('Cash Balance', str(user_money.cash_balance), True)

def redirect_menu(user_choice, coffee_types, coffee_resource, money_machine):
    if user_choice in ['espresso','latte','cappuccino']:
        coffee_maker(coffee_types[user_choice], coffee_resource, money_machine)
    elif user_choice in ['report', '2']:
        create_report(coffee_resource, money_machine)
    # elif user_choice in ['refill', '3']:
    #     coffee_resource = Resource()
    else:
        exit


def main():
    choice = True
    coffee_resource = Resource()
    coffee_types = create_coffee_types()
    money_machine = Moneymachine({})
    while choice:
        clear()
        main_menu =  Menu()
        user_choice =  main_menu.display_menu()
        redirect_menu(user_choice, coffee_types, coffee_resource, money_machine)
        user_choice = input('Do you want to continue(y/n)?: ')
        if user_choice.lower() == 'n':
            choice = False


if __name__ == '__main__':
    main()

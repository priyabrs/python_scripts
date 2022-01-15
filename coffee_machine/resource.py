MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

resources = {
    "water": 500,
    "milk": 400,
    "coffee": 300,
}

coffee_machine_image = '''
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
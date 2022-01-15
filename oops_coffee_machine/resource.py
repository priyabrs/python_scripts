from inspect import walktree
from logging.handlers import WatchedFileHandler
from xmlrpc.client import boolean

class ResourceException(Exception):
    pass


class Resource():
    def __init__(self, water = 400, milk = 300, coffee = 100) -> None:
        self.water = water
        self.milk = milk
        self.coffee = coffee

    def check_resource(self, req_resource_dict) -> bool:
        if self.water < req_resource_dict['water'] or self.milk < req_resource_dict['milk'] or self.coffee < req_resource_dict['coffee']:
            return False
        else:
            return True

    def update_resource(self, coffee_dict) -> None:
        self.water -= coffee_dict['water']
        self.milk -= coffee_dict['milk']
        self.coffee -= coffee_dict['coffee']

# if __name__ == '__main__':
#     r=Resource(20,30,40)
#     print([attr for attr in dir(r) if not attr.startswith('__')])
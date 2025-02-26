'''
You have been tasked with parsing menus from a large restaurant group. Each menu is streamed to clients via a provided interface. You must design object(s) that represents a menu and can be instantiated with data from the provided interface. Your design should contain an appropriate class structure to contain the parsed data, as well as a function or set of functions to perform the parsing.

Consumers will use your object(s) to access a complete representation of the data sent by the menu stream after it has finished loading. Your objects should provide easy access to the full representation of the menu. It should be possible to reconstruct the menu stream from your object.

The menu stream represents a list of menu items. Each line in the stream is a property of a menu item, and each item will be separated by an empty string. The attributes of each item are as follows:

  Line 0: The ID of the item
  Line 1: The item type, either CATEGORY, DISH or OPTION
  Line 2: The name of the item
  Line 3: The price of the item for DISH and OPTION. Not present for CATEGORY items.
  Any other line: A list of item IDs that are linked to the current item. OPTIONs do not have any linked items.

Example Menu:

4
DISH
Spaghetti
10.95
2
3

1
CATEGORY
Pasta
4
5

2
OPTION
Meatballs
1.00

3
OPTION
Chicken
2.00

5
DISH
Lasagna
12.00

6
DISH
Caesar Salad
9.75
3

'''

class Option():
    id = None
    name = None
    price = None

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Category():
    id = None
    name = None
    linked = []

    def __init__(self, id, name, linked):
        self.id = id
        self.name = name
        self.linked = linked

class Dish():
    id = None
    name = None
    price = None
    linked = []

    def __init__(self, id, name, price, linked):
        self.id = id
        self.name = name
        self.price = price
        self.linked = linked

from abc import ABC, abstractmethod

class MenuStream(ABC):
    @abstractmethod
    def next_line(self) -> str:
        pass 

class MenuStreamImplementation(MenuStream):
    def __init__(self):
        self._stream = ['4', 'DISH', 'Spaghetti', '10.95', '2', '3', '', '1', 'CATEGORY', 'Pasta', '4', '5', '', '2', 'OPTION', 'Meatballs', '1.00', '', '3', 'OPTION', 'Chicken', '2.00', '', '5', 'DISH', 'Lasagna', '12.00', '', '6', 'DISH', 'Caesar Salad', '9.75', '3', '']
    
    def next_line(self):
        return self._stream.pop(0) if self._stream else None

class Menu():

    # Has Dishes, Categories, Options
    categories = {}
    dishes = {}
    options = {}

    def __init__(self):
        pass

    def parse_stream(self, menu_stream: MenuStream):

        next = menu_stream.next_line()

        while next:
            id = next
            item_type = menu_stream.next_line()
            if item_type == "CATEGORY":
                name = menu_stream.next_line()
                linked = []
                linked_item = menu_stream.next_line()
                while linked_item != '':
                    linked.append(linked_item)
                    linked_item = menu_stream.next_line()
                self.categories[id] = Category(id, name, linked)
            elif item_type == "OPTION":
                name = menu_stream.next_line()
                price = menu_stream.next_line()
                self.options[id] = Option(id, name, price)
                _ = menu_stream.next_line()
            elif item_type == "DISH":
                name = menu_stream.next_line()
                price = menu_stream.next_line()
                linked = []
                linked_item = menu_stream.next_line()
                while linked_item != '':
                    linked.append(linked_item)
                    linked_item = menu_stream.next_line()
                self.dishes[id] = Dish(id, name, price, linked)
            else:
                print("Error")

            next = menu_stream.next_line()

    def print_basic(self):
        print("--- Categories ---")
        for id, category in self.categories.items():
            print(f"Name: {category.name}")
            print(f"Linked: {category.linked}")

        print("--- Dishes ---")
        for id, dish in self.dishes.items():
            print(f"Name: {dish.name}")
            print(f"Price: {dish.price}")
            print(f"Options:")

            for linked_option_id in dish.linked:
                linked_option = self.options[linked_option_id]
                print(f"{linked_option.name} - Price: {linked_option.price}")

        print("--- Options ---")
        for id, option in self.options.items():
            print(f"Name: {option.name}")

menu_stream = MenuStreamImplementation()
menu = Menu()
menu.parse_stream(menu_stream)
menu.print_basic()
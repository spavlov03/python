class Restaurant:
    def __init__(self, name, address, menu, employees):
        self.name = name
        self.address = address
        self.menu = menu
        self.drinks = {"alcohol": [], "soda": [], "hot_drinks": []}
        self.employees = employees
        self.is_open = False

    def open_close(self):
        if not self.is_open:
            self.is_open = True
        else:
            self.is_open = False

        # def add_drinks_to_menu(self, drink_type):
        #     if type(drink_type) is list:
        #         for i in range(len(drink_type)):
        #             self.drinks.append(drink_type[i])
        #         print(self.drinks)
        #     elif type(drink_type) is str:
        #         self.drinks.append(drink_type)

    def add_drinks_to_menu(self, drink_type, drink_name):
        if type(drink_name) is list:
            self.drinks[drink_type].extend(drink_name)
            print(self.drinks)
        else:
            self.drinks[drink_type].append(drink_name)
            print(self.drinks)


# person.update({"age": "10"})

jessy_restaurant = Restaurant(
    "Jessy restaurant", "535 Tijuana Street Cancun, Mexico", ["taco", "arroz", "rellenos", "birria"], []
)
jessy_restaurant.open_close()
jessy_restaurant.add_drinks_to_menu("alcohol", "Mojito")
print(jessy_restaurant.is_open)
print(jessy_restaurant.menu)
jessy_restaurant.add_drinks_to_menu("alcohol", ["Tequila", "Margarita", "Champagne"])


class Restaurant:
    def __init__(self, name, address, menu, employees):
        self.name = name
        self.address = address
        self.menu = menu
        # self.drinks = []
        self.employees = employees
        self.is_open = False

    def open_close(self):
        if not self.is_open:
            self.is_open = True
        else:
            self.is_open = False

    def add_drinks_to_menu(self, drink):
        self.menu.append(drink)


jessy_restaurant = Restaurant(
    "Jessy restaurant", "535 Tijuana Street Cancun, Mexico", ["taco", "arroz", "rellenos", "birria"], []
)
jessy_restaurant.open_close()
jessy_restaurant.add_drinks_to_menu("Mojito")
print(jessy_restaurant.is_open)
print(jessy_restaurant.menu)

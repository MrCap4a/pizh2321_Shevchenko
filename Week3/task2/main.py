class Pizza:
    def __init__(self, name: str, dough: str, sauce: str, components: list, price: float):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.components = components
        self.price = price

    def __str__(self):
        return f"Название: {self.name}\nТесто: {self.dough}\nСоус: {self.sauce}\nКомпоненты: {self.components}\nЦена: {self.price}"

    def __prepare(self):
        return "Подготовилась"

    def _cook(self):
        return "Пожарилась"

    def __slice(self):
        return "Порезалась"

    def __pack(self):
        return "Запаковалась"

class PizzaPepperoni(Pizza):
    def __init__(self):
        self.name = "Пепперони"
        self.dough = "Вкусное"
        self.sauce = "Томатный"
        self.components = ["колбаски пепперони", "моцарелла"]
        self.price = "690 рублей"

class PizzaBBQ(Pizza):
    def __init__(self):
        self.name = "Барбекю"
        self.dough = "Вкусное"
        self.sauce = "Барбекю"
        self.components = ["курочка", "лук", "шампиньоны", "баклажаны", "томаты", "моцарелла"]
        self.price = "820 рублей"

class PizzaSeafood(Pizza):
    def __init__(self):
        self.name = "Дары моря"
        self.dough = "Вкусное"
        self.sauce = "Чесночный"
        self.components = ["сыр фета и моцарелла", "семга", "лук", "маслины", "креветки", "мидии"]
        self.price = "940 рублей"

class Order:
    def __init__(self, terminal):
        self.__terminal = terminal
        self.__positions = []
        self.__price = 0
    
    def __str__(self):
        return f"Список позиций: {self.__positions}\nСтоимость заказа: {self.__price}"
    
    def add_pizza(self, pizza: Pizza):
        self.__positions.append(pizza.name)
        self.__price += pizza.price
    
    @property
    def summ(self):
        return self.__price
    
    def confirm(self):
        self.__terminal.confirm_payment()
    
    def decline(self):
        self.__positions = []
        self.__price = 0

class Terminal:
    def __init__(self, menu_list=PizzaPepperoni, show_menu=True):
        self.__order = Order(self)
        self.menu = menu_list
        self.show_menu = show_menu
    
    def __str__(self):
        result = "Терминал:\n"
        

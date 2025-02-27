class Pizza:
    def __init__(self, name: str, dough: str, sauce: str, components: list, price: str):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.components = components
        self.price = price

    def prepare(self):
        print("Подготовка пиццы")

    def cook(self):
        print("Жарка пиццы")

    def slice(self):
        print("Нарезка пиццы")

    def pack(self):
        print("Упаковка пиццы")

    def __str__(self):
        return f"Название: {self.name}\nТесто: {self.dough}\nСоус: {self.sauce}\nКомпоненты: {self.components}\nЦена: {self.price}"


class PizzaPepperoni(Pizza):
    def __init__(self):
        super().__init__("Пепперони", "Вкусное", "Томатный", ["колбаски пепперони", "моцарелла"], 690)


class PizzaBBQ(Pizza):
    def __init__(self):
        super().__init__("Барбекю", "Вкусное", "Барбекю", ["курочка", "лук", "шампиньоны", "баклажаны", "томаты", "моцарелла"], 820)


class PizzaSeafood(Pizza):
    def __init__(self):
        super().__init__("Дары моря", "Вкусное", "Чесночный", ["сыр фета и моцарелла", "семга", "лук", "маслины", "креветки", "мидии"], 940)


class Order:
    def __init__(self, terminal):
        self._terminal = terminal
        self._positions = []
        self._price = 0

    def __str__(self):
        return f"Список позиций: {self._positions}\nСтоимость заказа: {self._price}"

    def add_pizza(self, pizza: Pizza):
        self._positions.append(pizza.name)
        self._price += pizza.price

    @property
    def price(self):
        return self._price

    def confirm(self):
        self._terminal.confirm_payment()

    def cancel(self):
        self._positions = []
        self._price = 0
        print("Корзина очищена")

    def decline(self):
        self.cancel()


class Terminal:
    def __init__(self, menu_list=None, show_menu=True):
        if not menu_list:
            # Используем все три вида пиццы по умолчанию
            menu_list = [PizzaPepperoni(), PizzaBBQ(), PizzaSeafood()]
        self._menu_list = menu_list
        self._show_menu = show_menu
        self._order = None

    def display_menu(self):
        for item in self._menu_list:
            print(item)

    def create_order(self):
        self._order = Order(self)

    def process_user_input(self):
        while True:
            if self._order is None:
                self.create_order()

            command = input("Введите номер пиццы или 'x' для выхода или 'c' для очистки корзины: ")
            if command == 'x':
                break
            elif command == 'c':
                self._order.cancel()
            else:
                try:
                    index = int(command) - 1
                    if 0 <= index < len(self._menu_list):
                        pizza = self._menu_list[index]
                        self._order.add_pizza(pizza)
                        print(f"Добавлена пицца {pizza.name}")
                except ValueError:
                    print("Неверный ввод. Попробуйте еще раз.")

    def confirm_payment(self):
        total_price = self._order.price
        answer = input(
            f"Ваш заказ на сумму {total_price}. Желаете продолжить? y/n: ")
        if answer.lower() == 'y':
            print("Оплатите заказ!")
        else:
            self._order = None

    def accept_payment(self):
        user_input = ""
        while user_input != "+":
            print("Введите + когда закончите оплату")
            user_input = input()
        print("Оплата принята. Заказ передан в исполнение.")
        return True

    def close_order(self):
        if self._order is not None:
            self._order.decline()
            self._order = None


terminal = Terminal()
terminal.display_menu()
terminal.process_user_input()
if terminal._order is not None:
    terminal.confirm_payment()
    terminal.accept_payment()
    terminal.close_order()

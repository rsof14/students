from abc import ABC


class MenuItem(ABC):
    def __init__(self, title):
        self.__title = title

    def run(self):
        pass

    def get_title(self):
        return self.__title


class Menu(MenuItem):
    def __init__(self, title):
        super().__init__(title)
        self.__items = []
        self.__running = True
        self.parent_item = None

    def set_items(self, items: [MenuItem]):
        self.__items = items

    def get_items(self):
        return self.__items

    def run(self):
        self.__running = True
        while self.__running:
            self.print_menu()
            self.handle_user_input()

    def add_menu_item(self, item: MenuItem):
        item.parent_item = self
        self.__items.append(item)

    def add_back_button(self):
        back_button = Menu("Back")
        back_button.set_items(self.parent_item.get_items())
        self.__items.append(back_button)

    def print_menu(self):
        i = 0
        for item in self.__items:
            i += 1
            print(f"{i}. {item.get_title()}")

    def handle_user_input(self):
        user_input = int(input("Выберите пункт меню "))
        if not 0 < user_input <= len(self.__items):
            print("Вы ввели некорректное значение, повторите ввод")
            self.handle_user_input()
        self.__items[user_input - 1].run()


class SimpleMenuItem(MenuItem):
    def __init__(self, title, action):
        super().__init__(title)
        self.__action = action

    def run(self):
        self.__action()


def simple_func():
    print("Hello, world")


def back():
    pass


if __name__ == "__main__":
    main_menu = Menu("Main Menu")
    first_menu = Menu("First menu")
    second_menu = Menu("Second menu")
    simple_item1 = SimpleMenuItem("simple item 1", simple_func)

    main_menu.add_menu_item(first_menu)
    main_menu.add_menu_item(second_menu)
    first_menu.add_menu_item(simple_item1)
    first_menu.add_back_button()
    second_menu.add_menu_item(simple_item1)
    second_menu.add_back_button()

    main_menu.run()

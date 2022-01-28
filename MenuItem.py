from abc import ABC


class MenuItem(ABC):
    def __init__(self, title=""):
        self.__title = title

    def run(self):
        pass

    def get_title(self):
        return self.__title


class Menu(MenuItem):
    def __init__(self, title="", is_main_menu=True):
        super().__init__(title)
        self.is_main_menu = is_main_menu
        self.__items = []
        self.__running = True
        self.on_print_cmd = None
        self.on_input_cmd = None

    def set_on_print_cmd(self, cmd):
        self.on_print_cmd = cmd

    def set_on_input_cmd(self, cmd):
        self.on_input_cmd = cmd

    def set_items(self, items: [MenuItem]):
        self.__items = items

    def get_items(self):
        return self.__items

    def run(self):
        self.__running = True
        while self.__running:
            if self.on_print_cmd is not None:
                self.on_print_cmd()
            self.print_menu()
            self.handle_user_input()

    def add_menu_item(self, title):
        item = Menu(title, False)
        self.__items.append(item)
        return item

    def add_simple_menu_item(self, title, action):
        item = SimpleMenuItem(title, action)
        self.__items.append(item)
        return item

    def print_menu(self):
        for i, item in enumerate(self.__items):
            print(f"{i + 1}. {item.get_title()}")
        if self.is_main_menu:
            print(f"{len(self.__items) + 1}. Выход")
        else:
            print(f"{len(self.__items) + 1}. Назад")

    def handle_user_input(self):
        user_input = int(input("Выберите пункт меню "))
        if not 0 < user_input <= len(self.__items) + 1:
            print("Вы ввели некорректное значение, повторите ввод")
            return
        if user_input == len(self.__items) + 1:
            self.__running = False
        else:
            # if self.on_input_cmd is not None:
            #     self.on_input_cmd(user_input)
            self.__items[user_input - 1].run()


class SimpleMenuItem(MenuItem):
    def __init__(self, title, action):
        super().__init__(title)
        self.__action = action

    def run(self):
        self.__action()


def simple_func():
    print("Hello, world")


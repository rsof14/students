from students import StudentRepository, Student
from MenuItem import Menu


class StudentsController:
    def __init__(self):
        self.menu = Menu()
        self.students = StudentRepository()
        self.students.load()
        self.__selected_student = None

    def run(self):
        self.menu.run()

    def make_menu(self):
        students_list = self.menu.add_simple_menu_item("Список студентов", self.print_student_list)
        add_student = self.menu.add_simple_menu_item("Добавить студента", self.add_student_in_list)
        # edit_students = self.menu.add_menu_item("Редактировать студента")
        edit_students = self.menu.add_simple_menu_item("Редактировать студента", self.edit_student)
        students = self.students.get_students()
        # for i, student in enumerate(students):
        #     select_student = edit_students.add_menu_item(
        #         f"{student.last_name} {student.first_name} {student.middle_name} ({student.group})")
        #     select_student.set_on_print_cmd(self.print_student_info)
        #     edit_last_name = select_student.add_simple_menu_item("Изменить фамилию", self.edit_last_name)
        #     edit_last_name = select_student.add_simple_menu_item("Изменить имя", self.edit_first_name)
        #     edit_last_name = select_student.add_simple_menu_item("Изменить отчество", self.edit_middle_name)
        #     edit_last_name = select_student.add_simple_menu_item("Изменить группу", self.edit_group)
        #     edit_last_name = select_student.add_simple_menu_item("Добавить оценку", self.add_mark)
        #     edit_last_name = select_student.add_simple_menu_item("Изменить оценку", self.edit_mark)
        #     edit_last_name = select_student.add_simple_menu_item("Удалить оценку", self.del_mark)
        # edit_students.set_on_print_cmd(self.edit_student)
        delete_student = self.menu.add_simple_menu_item("Удалить студента", self.delete_student)
        show_good = self.menu.add_simple_menu_item("Показать отличников", self.print_a_students)
        show_bad = self.menu.add_simple_menu_item("Показать неуспевающих", self.print_f_students)

    def edit_student(self):
        self.print_students_for_edit()
        self.__selected_student = int(input("Введите номер редактируемого студента "))
        while self.__selected_student < 1 or self.__selected_student > self.students.count_students():
            if self.__selected_student < 1 or self.__selected_student > self.students.count_students():
                print("Вы ввели некорректное значение. Введите номер от 1 до " + self.students.count_students())
                self.__selected_student = int(input("Введите номер редактируемого студента "))
        self.print_student_info()
        action = self.edit_actions()
        while action != 8:
            if action == 1:
                self.edit_last_name()
            if action == 2:
                self.edit_first_name()
            if action == 3:
                self.edit_middle_name()
            if action == 4:
                self.edit_group()
            if action == 5:
                self.add_mark()
            if action == 6:
                self.edit_mark()
            if action == 7:
                self.del_mark()
            self.print_student_info()
            action = self.edit_actions()
        if action == 8:
            self.students.save()
            return

    def delete_student(self):
        self.print_students_for_edit()
        self.__selected_student = int(input("Введите номер студента, которого нужно удалить из списка "))
        while self.__selected_student < 1 or self.__selected_student > self.students.count_students():
            if self.__selected_student < 1 or self.__selected_student > self.students.count_students():
                print("Вы ввели некорректное значение. Введите номер от 1 до " + self.students.count_students())
                self.__selected_student = int(input("Введите номер студента, которого нужно удалить из списка "))
        student = self.students.get_student(self.__selected_student)
        print(f"Номер студента для удаления {self.__selected_student}")
        answer = input(
            f"Вы уверены, что хотите удалить студента {student.last_name} {student.first_name} {student.middle_name} ({student.group})? [Да/Нет] ")
        if answer == "Да":
            self.students.remove_student(self.__selected_student)
            self.students.save()
        else:
            return

    def print_a_students(self):
        a_students = self.students.a_student_list()
        if len(a_students) == 0:
            print("Отличников нет")
        else:
            for i, student in enumerate(a_students):
                print(
                    f"==={i + 1}===\nФамилия: {student.last_name}\nИмя: {student.first_name}\nОтчество: {student.middle_name}\nГруппа: {student.group}\nОценки:")
                for key, value in student.marks.items():
                    print("  ", key, ':', value)

    def print_f_students(self):
        f_students = self.students.f_student_list()
        if len(f_students) == 0:
            print("Неуспевающих нет")
        else:
            for i, student in enumerate(f_students):
                print(
                    f"==={i + 1}===\nФамилия: {student.last_name}\nИмя: {student.first_name}\nОтчество: {student.middle_name}\nГруппа: {student.group}\nОценки:")
                for key, value in student.marks.items():
                    print("  ", key, ':', value)

    def edit_actions(self):
        print(
            "1. Изменить фамилию\n2. Изменить имя\n3. Изменить отчество\n4. Изменить группу\n5. Добавить оценку\n6. Изменить оценку\n7. Удалить оценку\n8. Назад")
        action = int(input("Выберите действие "))
        while action < 1 or action > 8:
            print("Вы ввели некорректное значение, введите число от 1 до 8")
            action = int(input("Выберите действие "))
        return action

    def print_students_for_edit(self):
        students = self.students.get_students()
        for i, student in enumerate(students):
            print(
                f"{i + 1}. {student.last_name} {student.first_name} {student.middle_name} ({student.group})")

    def print_student_list(self):
        students = self.students.get_students()
        for i, student in enumerate(students):
            print(
                f"==={i + 1}===\nФамилия: {student.last_name}\nИмя: {student.first_name}\nОтчество: {student.middle_name}\nГруппа: {student.group}\nОценки:")
            for key, value in student.marks.items():
                print("  ", key, ':', value)

    def add_student_in_list(self):
        surname = input("Введите фамилию студента, которого нужно добавить ")
        name = input("Введите имя студента, которого нужно добавить ")
        middle_name = input("Введите отчество студента, которого нужно добавить ")
        group = input("Введите номер группы студента, которого нужно добавить ")
        marks = {}
        self.students.add_student(Student(surname, name, middle_name, group, marks))
        self.students.save()

    def select_student(self, id):
        self.__selected_student = id

    def print_student_info(self):
        student = self.students.get_student(self.__selected_student)
        print(
            f"Редактируемый студент:\nФамилия: {student.last_name}\nИмя: {student.first_name}\nОтчество: {student.middle_name}\nГруппа: {student.group}\nОценки:")
        for key, value in student.marks.items():
            print("  ", key, ':', value)

    def edit_last_name(self):
        new_last_name = input("Введите новую фамилию ")
        student = self.students.get_student(self.__selected_student)
        student.last_name = new_last_name

    def edit_first_name(self):
        new_first_name = input("Введите новое имя ")
        student = self.students.get_student(self.__selected_student)
        student.first_name = new_first_name

    def edit_middle_name(self):
        new_middle_name = input("Введите новое отчество ")
        student = self.students.get_student(self.__selected_student)
        student.middle_name = new_middle_name

    def edit_group(self):
        new_group = input("Введите новую группу ")
        student = self.students.get_student(self.__selected_student)
        student.group = new_group

    def add_mark(self):
        sub = input("Введите предмет ")
        mark = int(input("Введите оценку "))
        student = self.students.get_student(self.__selected_student)
        if student.marks.get(sub) is None:
            student.marks[sub] = mark
        else:
            print("Оценка по этому предмету уже есть")

    def edit_mark(self):
        sub = input("Введите предмет ")
        mark = int(input("Введите оценку "))
        student = self.students.get_student(self.__selected_student)
        if student.marks.get(sub) is not None:
            student.marks[sub] = mark
        else:
            print("У студента еще нет оценки по этому предмету")

    def del_mark(self):
        student = self.students.get_student(self.__selected_student)
        sub = input("Введите предмет ")
        if student.marks.get(sub) is not None:
            if input(f"Вы уверены, что хотите удалить оценку по {sub}? [Да/Нет] ") == "Да":
                del student.marks[sub]
        else:
            print("У студента нет оценки по этому предмету")


if __name__ == "__main__":
    students_controller = StudentsController()
    students_controller.make_menu()
    students_controller.run()

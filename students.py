from dataclasses import (dataclass, asdict)
import json


class StudentRepository:
    def __init__(self):
        self.__students = []

    def add_student(self, student: dataclass()):
        self.__students.append(student)

    def get_student(self, id):
        return self.__students[id - 1]

    def count_students(self):
        return len(self.__students)

    def remove_student(self, id):
        del self.__students[id - 1]

    def get_students(self):
        return self.__students

    def save(self):
        result = []
        for student in self.__students:
            result.append(asdict(student))
        with open("test.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False)

    def load(self):
        with open("test.json", "r", encoding="utf-8") as f:
            python_data = json.load(f)
            for student in python_data:
                self.add_student(Student(**student))
        # student1 = Student("Иванов", "Иван", "Иванович", "ОП-16", {"Математика": 5, "Информатика": 5})
        # student2 = Student("Петров", "Петр", "Петрович", "ОП-16", {"Математика": 4, "Информатика": 3})
        # self.add_student(student1)
        # self.add_student(student2)

    def a_student_list(self):
        student_list = []
        for student in self.__students:
            flag = True
            for key, value in student.marks.items():
                if value != 5:
                    flag = False
                    break
            if flag:
                student_list.append(student)
        return student_list

    def f_student_list(self):
        student_list = []
        for student in self.__students:
            flag = False
            for key, value in student.marks.items():
                if value < 3:
                    flag = True
                    break
            if flag:
                student_list.append(student)
        return student_list


@dataclass
class Student:
    last_name: str
    first_name: str
    middle_name: str
    group: str
    marks: dict[str, int]

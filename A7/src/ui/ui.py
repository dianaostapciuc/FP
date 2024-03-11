from src.services.services import *
# * = imports everything


class UserInterfaceException(Exception):

    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message


class UserInterface:

    def __init__(self, services):
        self._service = services

    def add(self, student: student):
        self._service.add(student)

    def display(self):
        for student in self._service.return_all():
            print(str(student))
        print("\n")

    def filter(self, variable):
        self._service.filter(variable)

    def undo(self):
        if self._service.operations == 0:
            raise ServiceException("Nothing to undo")
        self._service.undo()

    def menu(self):

        while True:
            print("1.Add a student...")
            print("2.Display the list of students...")
            print("3.Filter the list so that students in a given group are deleted from the list...")
            print("4.Undo the last operation...")
            print("0.Exit")
            print("\n")
            choice = input(">")

            if choice == "1":
                student_id = int(input("The student's id is: "))
                name = input("The student's name is: ")
                group = int(input("The student's group is: "))
                if student_id not in range (1000, 9999):
                    raise UserInterfaceException("The id is out of range.")
                if group < 0:
                    raise UserInterfaceException("The value of group is negative.")
                self.add(student(student_id, name, group))

            elif choice == "2":
                self.display()

            elif choice == "3":
                given_group = int(input("Based on what group do you want to filter? "))
                self.filter(given_group)

            elif choice == "4":
                self.undo()

            elif choice == "0":
                return

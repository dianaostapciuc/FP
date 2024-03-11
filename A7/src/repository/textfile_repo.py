from src.repository.memory_repo import *


# * = importing everything

class TextFileRepo(MemoryRepo):

    def __init__(self, file_name):
        super(TextFileRepo, self).__init__()
        self._file_name = file_name
        self._load_file()

    # def get_student(self, given_id):
    #
    #     fin = open(self._file_name, "rt")
    #     lines = fin.readlines()
    #     fin.close()
    #
    #     for student in lines:
    #         current_student = student.split(", ")
    #         if int(current_student[0]) == int(given_id):
    #             return student

    def _load_file(self):
        # r = read, t = text
        loading_file = open(self._file_name, "rt")
        lines = loading_file.readlines()
        loading_file.close()
        for students in lines:
            current_student = students.split(", ")
            new_student = student(int(current_student[0].strip()), current_student[1].strip(),
                                  int(current_student[2].strip()))
            super().add(new_student)

    def _save_file(self):
        # w = write, t = text 
        saving_file = open(self._file_name, "wt")
        for students in self.get_all():  # get_all = returns all students and obj goes through each
            saving_file.write(str(students))
            saving_file.write('\n')
        saving_file.close()

    def add(self, student: student):
        super().add(student)
        self._save_file()

    def deleting_a_student(self, id):
        super().deleting_a_student(id)
        self._save_file()

from src.domain.student import student
from src.repository.memory_repo import MemoryRepo
import pickle
import random


class BinaryFileRepo(MemoryRepo):

    def generated_student(self):

        student_names = ["John", "Anne", "Jade", "Chris", "Daryl", "Rick", "Rose"]
        student_groups = [214, 215, 216, 217, 814, 815, 816, 817, 914, 915, 916, 917]
        new_student = student(random.randint(1000, 9999), student_names[random.randint(0, 6)], student_groups[random.randint(0, 10)])
        return new_student

    def add_a_generated_random_student(self):
        for i in range(10):
            new_student = self.generated_student()
            self.add(new_student)

    def __init__(self, file_name="students.bin"):
        super(BinaryFileRepo, self).__init__()
        # initializes it ?????
        self._file_name = file_name
        self._load_file()
        # self.add_a_generated_random_student()
        self._save_file()

    def _load_file(self):
        # r = read, b = binary
        opening_file = open(self._file_name, "rb")
        objects = pickle.load(opening_file)
        # converts binary
        for student in objects:
            super().add(student)
        opening_file.close()

    def add(self, student: student):
        super().add(student)
        self._save_file()

    def _save_file(self):
        # w = write, b = binary
        saving_file = open(self._file_name, "wb")
        pickle.dump(self.get_all(), saving_file)
        # puts in file and converts
        saving_file.close()
        # here, there's no need to split; it already knows how to manage the string

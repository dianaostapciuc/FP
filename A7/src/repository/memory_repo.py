import copy

from src.domain.student import student
import random


class RepoException(Exception):
    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message


class MemoryRepo(object):

    def __init__(self):
        self._students = []

    def get_element(self, given_id):
        for student in self._students:
            if student.id == given_id:
                return student

    def add(self, student: student):
        check_stud = self.get_element(student.id)
        if check_stud in self._students:
            raise RepoException("The student/id already exists :(((((((")
        self._students.append(student)

    def get_all(self):
        return self._students

    def change_data(self, new_list):
        self._students = copy.deepcopy(new_list)

    def adding_a_generated_student(self):

        student_names = ["John", "Anne", "Jade", "Chris", "Daryl", "Rick", "Rose"]
        student_groups = [214, 215, 216, 217, 814, 815, 816, 817, 914, 915, 916, 917]
        new_student = student(random.randint(1000, 9999), student_names[random.randint(0, 6)],
                              student_groups[random.randint(0, 10)])
        self._students.append(new_student)

    def deleting_a_student(self, id):

        stud = self.get_element(id)
        self._students.remove(stud)
        # deletes a student


def testing_memory_repo():
    repo = MemoryRepo()
    assert repo.get_all() == []
    test_student = student(9999, "Iona", 915)
    repo.add(test_student)
    test_list = [test_student]
    assert repo.get_all() == test_list


if __name__ == "__main__":
    testing_memory_repo()

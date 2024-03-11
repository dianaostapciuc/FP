from src.domain.student import student
import copy
from src.repository.memory_repo import MemoryRepo


class ServiceException(Exception):
    def __init__(self, message):
        self.__message = message

    @property
    def message(self):
        return self.__message


class StudentServices:

    def __init__(self, repository):
        self._repo = repository
        self.operations = 0
        self._history = []
        self._history.append(copy.deepcopy(self._repo.get_all()))

    def add(self, student: student):

        self._repo.add(student)
        self._history.append(copy.deepcopy(self._repo.get_all()))
        self.operations += 1

    def return_all(self):
        return self._repo.get_all()

    def filter(self, given_group):
        all_students = self._repo.get_all()
        # returns a list of lists of students
        for student in all_students:
            if student.group == given_group:
                self._repo.deleting_a_student(student.id)
        self.operations += 1
        self._history.append(copy.deepcopy(self._repo.get_all()))

    def undo(self):
        if self.operations == 0:
            raise ServiceException("Nothing to undo!")

        self.operations -= 1
        self._repo.change_data(copy.deepcopy(self._history[len(self._history) - 2]))
        _random_value = self._history.pop()


def testing_add():
    repo = MemoryRepo()
    assert repo.get_all() == []
    test_student = student(9999, "Iona", 915)
    repo.add(test_student)
    test_list = [test_student]
    assert repo.get_all() == test_list


if __name__ == "__main__":
    testing_add()

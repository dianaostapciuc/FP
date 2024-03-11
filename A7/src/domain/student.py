class student:

    def __init__(self, id: int, name: str, group: int):
        self.id = id
        self.name = name
        self.group = group

    @property
    def get_id(self):
        return self.id

    @property
    def get_name(self):
        return self.name

    @property
    def get_group(self):
        return self.group

    def __str__(self):
        return str(self.id) + ", " + self.name + ", " + str(self.group)


def testing_student():
    new_student = student(6345, "Dan", 915)
    assert new_student.id == 6345
    assert new_student.name == "Dan"
    assert new_student.group == 915
    assert str(new_student) == "6345, Dan, 915"


if __name__ == "__main__":
    testing_student()

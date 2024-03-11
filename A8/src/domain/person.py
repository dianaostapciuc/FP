class person:

    def __init__(self, idd, name, phone_number):
        self._id = idd
        self._name = name
        self._phone_number = phone_number

    @property
    def get_id(self):
        return self._id

    @property
    def get_name(self):
        return self._name

    @property
    def get_phone_number(self):
        return self._phone_number

    def __str__(self):
        return str(self._id) + " " + str(self._name) + " " + str(self._phone_number)


def testing_person():
    new_person = person(4555, "John", "0745649744")
    assert new_person.get_person_id() == 4555
    assert new_person.get_name() == "John"
    assert new_person.get_phone_number() == "0745649744"


if __name__ == "__main__":
    testing_person()


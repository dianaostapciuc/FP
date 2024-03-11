from src.domain.person import person
from src.services.service_exception import ServiceException


def matching_the_string(large_str, small_str):
    small_string_length = len(small_str)
    large_string_length = len(large_str)
    small_str = small_str.lower()  # returns a string where all characters are lower-cased
    large_str = large_str.lower()
    if small_string_length > large_string_length:
        return False
    for i in range(large_string_length):
        if large_str[i: i + small_string_length] == small_str:
            return True
    return False


class PersonService:

    def __init__(self, person_repo:person):
        self._person_repo = person_repo

    def creating_a_person(self, person_id, name, phone_number):
        new_person = person(person_id, name, phone_number)
        self._person_repo.adding_an_object(new_person)

    def adding_a_person(self, person_id, name, phone_number):
        new_person = person(person_id, name, phone_number)
        self._person_repo.adding_an_object(new_person)

    def removing_a_person(self, person_id, name, phone_number):
        new_person = person(person_id, name, phone_number)
        self._person_repo.removing_an_object(new_person)
        return new_person

    def updating_a_person(self, person_id, name, phone_number):
        new_person = person(person_id, name, phone_number)
        self._person_repo.updating_an_object(new_person)

    def get_list(self):
        return self._person_repo.get_all()

    def search_by_name(self, input_name):
        result = ""
        for person in self._person_repo.get_all():
            if matching_the_string(person.get_name, input_name):
                result += str(person) + '\n'
        if result != "":
            return result
        return None

    def search_by_phone_number(self, input_number):
        result = ""
        for person in self._person_repo.get_all():
            if matching_the_string(person.get_phone_number, input_number):
                result += str(person) + '\n'
        if result != "":
            return result
        return None

    # def __str__(self):
    #     result = ""
    #     for person in self._person_repo.get_all():
    #         result += str(person) + '\n'
    #     return result



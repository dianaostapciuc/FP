from src.domain.activity import activity
from src.domain.person import person
from src.repository.repository_exception import RepoException


class Repository:

    def __init__(self):
        self._objects = []

    def finding_an_object_using_id(self, id):

        for each_object in self._objects:
            if int(each_object.get_id) == int(id):
                return each_object
        return None

    def adding_an_object(self, object):
        existing_object = self.finding_an_object_using_id(object.get_id)
        if existing_object is not None:
            raise RepoException("An element with the same id already exists!")
        self._objects.append(object)

    def removing_an_object(self, object):
        existing_object = self.finding_an_object_using_id(object.get_id)
        if existing_object is None:
            raise RepoException("The element does not exist!")
        self._objects.remove(existing_object)

    def updating_an_object(self, object):
        existing_object = self.finding_an_object_using_id(object.get_id)
        if existing_object is None:
            raise RepoException("The element does not exist!")
        position_of_object = self._objects.index(existing_object)
        self._objects.remove(existing_object)
        self._objects.insert(position_of_object, object)

    def get_all(self):
        return self._objects

    def get_list(self):
        return list(self._objects)

    def __len__(self):
        return len(self._objects)

    # def __str__(self):
    #     string = ""
    #     for each_object in self._objects:
    #         string += str(each_object)
    #         string += "/n"
    #     return string

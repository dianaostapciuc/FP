import unittest
from src.domain.person import person

from memory_repo import Repository


class TestingMemoryRepo(unittest.TestCase):

    def test_adding(self):
        repo = Repository()
        test_person = person(4256, "Percy", "0745649744")
        repo.adding_an_object(test_person)
        self.assertIn(test_person, repo.get_all())

    def test_deleting(self):
        repo = Repository()
        test_person = person(4256, "Percy", "0745649744")
        repo.adding_an_object(test_person)
        repo.removing_an_object(test_person)
        self.assertNotIn(test_person, repo.get_all())

    def test_updating(self):
        repo = Repository()
        test_person = person(4256, "Percy", "0745649744")
        repo.adding_an_object(test_person)
        new_person = person(4256, "Daryl", "0745649744")
        repo.updating_an_object(new_person)
        self.assertIn(new_person, repo.get_all())


if __name__ == "__main__":
    unittest.main()

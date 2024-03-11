import unittest
from src.repository.memory_repo import Repository
from src.services.person_services import PersonService
from src.domain.person import person
from src.services.activity_services import ActivityService
from src.domain.activity import activity
from datetime import date, time


class Testing(unittest.TestCase):
    def test_person_add(self):
        repo = Repository()
        persons = PersonService(repo)
        test_person = person(1234, "Daryl", "0745649744")
        persons.adding_a_person(1234, "Daryl", "0745649744")
        self.assertEqual(str(test_person) + '\n', str(persons))

    def test_activity_add(self):
        repo = Repository()
        activities = ActivityService(repo)
        test_activity = activity(333, [1234, 5678], "2022/12/25", "22:22", "very descriptive description")
        activities.adding_an_activity(333, [1234, 5678], "2022/12/25", "22:22", "very descriptive description")
        self.assertEqual(str(test_activity) + '\n', str(activities))

    def test_person_update(self):
        repo = Repository()
        persons = PersonService(repo)
        test_person = person(1234, "Daryl", "0745649744")
        persons.adding_a_person(1234, "Daryl", "0745649744")
        test_person = person(1234, "Rick", "0745649744")
        persons.updating_a_person(1234, "Rick", "0745649744")
        self.assertEqual(str(test_person) + '\n', str(persons))

    def test_activity_update(self):
        repo = Repository()
        activities = ActivityService(repo)
        test_activity = activity(333, [1234, 5678], "2022/12/25", "22:22", "very descriptive description")
        activities.adding_an_activity(333, [1234, 5678], "2022/12/25", "22:22", "very descriptive description")
        test_activity = activity(333, [1234, 5555], "2022/12/25", "22:22", "very descriptive description")
        activities.updating_an_activity(333, [1234, 5555], "2022/12/25", "22:22", "very descriptive description")
        self.assertEqual(str(test_activity) + '\n', str(activities))

    def test_person_delete(self):
        repo = Repository()
        persons = PersonService(repo)
        test_person = person(1234, "Daryl", "0745649744")
        persons.adding_a_person(1234, "Daryl", "0745649744")
        persons.adding_a_person(4321, "Negan", "0745316488")
        persons.removing_a_person(4321, "Negan", "0745316488")
        self.assertEqual(str(test_person) + '\n', str(persons))

    def test_activity_delete(self):
        repo = Repository()
        activities = ActivityService(repo)
        test_activity = activity(333, [1234, 5678], "2022/12/25", "22:22", "very descriptive description")
        activities.adding_an_activity(333, [1234, 5678], "2022/12/25", "22:22", "very descriptive description")
        activities.adding_an_activity(222, [1111, 3333], "2023/11/12", "13:13", "i'm out of ideas")
        activities.removing_an_activity(222, [1111, 3333], "2023/11/12", "13:13", "i'm out of ideas")
        self.assertEqual(str(test_activity) + '\n', str(activities))


if __name__ == '__main__':
    unittest.main()

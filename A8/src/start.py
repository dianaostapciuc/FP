from src.domain.person import person
from src.domain.activity import activity
from src.services.person_services import PersonService
from src.services.activity_services import ActivityService
from src.ui.ui import UserInterface
from src.repository.memory_repo import Repository
import random
from datetime import date, time


def add_random_person(self):
    id = 1000
    names = ["Anne", "John", "Daryl", "Rick", "Rose", "Jade", "Enid", "Lilith", "Paul"]
    for i in range(20):
        id += 125
        name = names[random.randint(0, 8)]
        phone_number = ""
        for j in range(10):
            digit = random.randint(0, 9)
            phone_number += str(digit)
        new_person = person(id, name, phone_number)
        self.adding_an_object(new_person)


def add_random_activity(self):
    activity_id = 2000
    each_person_id = 1250
    all_descriptions = ["reading", "movies", "swimming", "running", "dancing", "singing", "tennis", "studying"]
    for i in range(20):
        person_id = []
        for j in range(5):
            person_id.append(each_person_id)
            each_person_id += 5
        activity_id += 25
        the_date = date(random.randint(2010, 2023), random.randint(1, 12), random.randint(1, 28))
        the_time = time(random.randint(0, 23), random.randint(0, 59))
        description = all_descriptions[random.randint(0, 7)]
        new_activity = activity(activity_id, person_id, the_date, the_time, description)
        self.adding_an_object(new_activity)
    new_activity = activity(3333, [1111, 2222], date(2023, 10, 12), time(10, 13), "swimming")
    self.adding_an_object(new_activity)
    new_activity = activity(4444, [1010, 9999], date(2023, 10, 13), time(10, 10), "theatre")
    self.adding_an_object(new_activity)
    new_activity = activity(6666, [9999, 9998], date(2023, 10, 14), time(22, 23), "horse riding")
    self.adding_an_object(new_activity)
    new_activity = activity(6686, [9999, 9998], date(2023, 11, 7), time(5, 30), "school work")
    self.adding_an_object(new_activity)
    new_activity = activity(6696, [9999, 9998], date(2023, 12, 3), time(20, 20), "singing")
    self.adding_an_object(new_activity)


if __name__ == "__main__":
    person_repo = Repository()
    activity_repo = Repository()
    add_random_person(person_repo)
    add_random_activity(activity_repo)
    person_services = PersonService(person_repo)
    activity_services = ActivityService(activity_repo)
    UI = UserInterface(activity_services, person_services)
    UI.starting_menu()

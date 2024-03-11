from datetime import date, time


class activity:

    def __init__(self, idd, person_id: list, the_date: date, the_time: time, description):
        self._id = idd
        self._person_id = person_id
        self._the_date = the_date
        self._the_time = the_time
        self._description = description

    @property
    def get_id(self):
        return self._id

    @property
    def get_activity_person_id(self):
        return self._person_id

    @property
    def get_date(self):
        return self._the_date

    @property
    def get_time(self):
        return self._the_time

    @property
    def get_description(self):
        return self._description

    def __str__(self):
        return str(self._id) + " " + str(self._person_id) + " " + str(self._the_date) + " " + str(self._the_time) + " "+ str(self._description)


def testing_activity():
    new_activity = activity(4112, [1, 2, 3, 5], date(2022, 12, 20), time(12, 50), "what is this")
    assert new_activity._id == 4112
    assert new_activity._person_id == [1, 2, 3, 5]
    assert new_activity._the_date == date(2022, 12, 20)
    assert new_activity._the_time == time(12, 50)
    assert new_activity._description == "what is this"


if __name__ == "__main__":
    testing_activity()

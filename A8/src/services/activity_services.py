from src.domain.activity import activity
from src.services.service_exception import ServiceException


def matching_the_string(large_str, small_str):
    large_str = str(large_str)
    small_str = str(small_str)
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


class ActivityService:

    def __init__(self, activities_repo: activity):
        self._activities_repo = activities_repo

    def creating_an_activity(self, activity_id, person_id: list, our_date, our_time, description):
        new_activity = activity(activity_id, person_id, our_date, our_time, description)
        self._activities_repo.adding_an_object(new_activity)

    def adding_an_activity(self, activity_id, person_id: list, our_date, our_time, description):
        new_activity = activity(activity_id, person_id, our_date, our_time, description)
        for activities in self._activities_repo.get_all():
            if activities.get_id == activity_id:
                raise ServiceException("Cannot add this.")
            elif activities.get_time == our_time and activities.get_date == our_date:
                raise ServiceException("Cannot add this.")
        self._activities_repo.adding_an_object(new_activity)

    def removing_an_activity(self, activity_id, person_id, our_date, our_time, description):
        new_activity = activity(activity_id, person_id, our_date, our_time, description)
        self._activities_repo.removing_an_object(new_activity)

    def updating_an_activity(self, activity_id, person_id: list, our_date, our_time, description):
        new_activity = activity(activity_id, person_id, our_date, our_time, description)
        self._activities_repo.updating_an_object(new_activity)

    def get_list(self):
        return self._activities_repo.get_all()

    def search_by_date(self, our_date):
        our_date = str(our_date)
        result = ""
        for activity in self._activities_repo.get_all():
            if matching_the_string(activity.get_date, our_date):
                result += str(activity) + '\n'
        if result != "":
            return result
        return None

    def search_by_time(self, our_time):
        our_time = str(our_time)
        result = ""
        for activity in self._activities_repo.get_all():
            if matching_the_string(activity.get_time, our_time):
                result += str(activity) + '\n'
        if result != "":
            return result
        return None

    def search_by_description(self, our_description):
        result = ""
        for activity in self._activities_repo.get_all():
            if matching_the_string(activity.get_description, our_description):
                result += str(activity) + '\n'
        if result != "":
            return result
        return None

    def ordering_the_activities_by_their_start_time(self, given_date):
        list_to_sort = []
        for activity in self._activities_repo.get_all():
            if activity.get_date == given_date:
                list_to_sort.append(activity)
        return sorted(list_to_sort, key=lambda x: x.get_time)

    def creating_and_sorting_a_list_of_the_busiest_days(self, given_date):
        list_of_busiest_days = []
        dictionary_used_for_sort = {}
        for activity in self._activities_repo.get_all():
            if activity.get_date >= given_date:
                list_of_busiest_days.append(activity)
        for activity in list_of_busiest_days:
            current_date = activity.get_date
            number_of_activities = 0
            for different_activity in list_of_busiest_days:
                if current_date == different_activity.get_date:
                    number_of_activities += 1
            dictionary_used_for_sort[current_date] = number_of_activities
        for i in range(len(list_of_busiest_days)):
            number_of_activities1 = dictionary_used_for_sort[activity.get_date]
            j = i + 1
            for j in range(len(list_of_busiest_days)):
                number_of_activities2 = dictionary_used_for_sort[different_activity.get_date]
                if number_of_activities1 > number_of_activities2:
                    list_of_busiest_days[i], list_of_busiest_days[j] = list_of_busiest_days[j], list_of_busiest_days[i]
        return list_of_busiest_days

    def activities_for_a_given_person(self, given_day, given_person):
        list_of_activities = []
        for activity in self._activities_repo.get_all():
            if activity.get_date >= given_day:
                for ids in activity.get_activity_person_id:
                    if int(ids) == int(given_person):
                        list_of_activities.append(activity)
        return list_of_activities

    # def __str__(self):
    #     result = ""
    #     for activity in self._activities_repo.get_all():
    #         result += str(activity) + '\n'
    #     return result

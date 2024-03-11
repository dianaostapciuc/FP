from src.repository.repository_exception import RepoException
from src.services.activity_services import ActivityService
from src.services.person_services import PersonService
from src.services.service_exception import ServiceException
from src.ui.ui_exception import UserInterfaceException
from datetime import date, time


def check_if_integer(variable):
    variable = str(variable)
    if variable[0] == '0':
        return False
    for element in variable:
        if element < '0' or element > '9':
            return False
    return True


def check_if_string(variable):
    if len(variable) < 3:
        return False
    for element in variable:
        if '0' <= element <= '9':
            return False
    return True


def check_if_phone_number(variable):
    if len(variable) < 3:
        return False
    for element in variable:
        if element < '0' or element > '9':
            return False
    return True


def reading_the_date():
    while True:
        try:
            year = int(input("What year? "))
            month = int(input("What month? "))
            day = int(input("What day? "))
            validate_date(year, month, day)
        except UserInterfaceException as uie:
            print(f"There was a {str(type(uie))}, with message: {str(uie)}")
        except ValueError as ve:
            print(f"There was a {str(type(ve))}, with message: {str(ve)}")
        except TypeError as ve:
            print(f"There was a {str(type(ve))}, with message: {str(ve)}")
        else:
            return date(year, month, day)


def reading_the_time():
    while True:
        try:
            hour = int(input("What hour is it? "))
            minutes = int(input("How many minutes? "))
            validate_time(hour, minutes)
        except UserInterfaceException as uie:
            print(f"There was a {str(type(uie))}, with message: {str(uie)}")
        except ValueError as ve:
            print(f"There was a {str(type(ve))}, with message: {str(ve)}")
        except TypeError as ve:
            print(f"There was a {str(type(ve))}, with message: {str(ve)}")
        else:
            return time(hour, minutes)


def validating_the_person_input(person_id, name, phone_number):
    if check_if_integer(person_id) is False or len(person_id) < 3:
        raise UserInterfaceException("The id is not an accepted input!")
    if check_if_string(name) is False:
        raise UserInterfaceException("The name is not an accepted input!")
    if check_if_phone_number(phone_number) is False:
        raise UserInterfaceException("The phone number is not an accepted input!")


def validating_the_activity_input(activity_id, person_id, description):
    if check_if_integer(activity_id) is False or len(activity_id) < 3:
        raise UserInterfaceException("The id is not an accepted input!")
    for ids in person_id:
        if check_if_integer(ids) is False or len(str(ids)) < 3:
            raise UserInterfaceException("The id is not an accepted input!")
    if check_if_string(description) is False:
        raise UserInterfaceException("The description is not an accepted input!")


def validate_date(year, month, day):
    year = int(year)
    month = int(month)
    day = int(day)

    if year > 2023 or year < 2010:
        raise UserInterfaceException("Invalid year")
    if month < 1 or month > 12:
        raise UserInterfaceException("Invalid month")
    if day < 1 or day > 31:
        raise UserInterfaceException("Invalid day")


def validate_time(hour, minutes):
    hour = int(hour)
    minutes = int(minutes)
    if hour < 0 or hour > 23:
        raise UserInterfaceException("Invalid hour")
    if minutes < 0 or minutes > 59:
        raise UserInterfaceException("Invalid minutes")


class UserInterface:

    def __init__(self, activity_service: ActivityService, person_service: PersonService):
        self._activity_service = activity_service
        self._person_service = person_service

    def adding_a_person(self):
        try:
            person_id = input("What is the person's id? ")
            name = input("What is the person's name? ")
            phone_number = input("What is the person's phone number? ")
            validating_the_person_input(person_id, name, phone_number)
        except UserInterfaceException as uie:
            print("There was a error that unfortunately said: " + str(uie))
        else:
            self._person_service.adding_a_person(int(person_id), name, phone_number)

    def removing_a_person(self):
        try:
            person_id = input("What is the person's id? ")
            name = input("What is the person's name? ")
            phone_number = input("What is the person's phone number? ")
            validating_the_person_input(person_id, name, phone_number)
        except UserInterfaceException as uie:
            print("There was a error that unfortunately said: " + str(uie))
        else:
            self._person_service.removing_a_person(int(person_id), name, phone_number)

    def updating_a_person(self):
        try:
            person_id = input("What is the person's id? ")
            name = input("What is the person's name? ")
            phone_number = input("What is the person's phone number? ")
            validating_the_person_input(person_id, name, phone_number)
        except UserInterfaceException as uie:
            print("There was a error that unfortunately said: " + str(uie))
        else:
            self._person_service.updating_a_person(int(person_id), name, phone_number)

    def listing_persons(self):
        person_list = self._person_service.get_list()
        for person in person_list:
            print (str(person))

    def adding_an_activity(self):
        try:
            activity_id = input("What is your activity id? ")
            number_of_persons = int(input("How many persons are participating in this activity? "))
            person_id = []
            for i in range(number_of_persons):
                ids = int(input("What is the person's id? "))
                person_id.append(ids)
            the_date = reading_the_date()
            the_time = reading_the_time()
            description = input("What is the description for the activity? ")
            validating_the_activity_input(activity_id, person_id, description)
        except UserInterfaceException as uie:
            print("There was a error that unfortunately said: " + str(uie))
        else:
            self._activity_service.adding_an_activity(int(activity_id), person_id, the_date, the_time, description)

    def removing_an_activity(self):
        try:
            activity_id = input("What is your activity id? ")
            number_of_persons = int(input("How many persons are participating in this activity? "))
            person_id = []
            for i in range(number_of_persons):
                ids = int(input("What is the person's id? "))
                person_id.append(ids)
            the_date = reading_the_date()
            the_time = reading_the_time()
            description = input("What is the description for the activity? ")
            validating_the_activity_input(activity_id, person_id, description)
        except UserInterfaceException as uie:
            print("There was a error that unfortunately said: " + str(uie))
        else:
            self._activity_service.removing_an_activity(activity_id, person_id, the_date, the_time, description)

    def updating_an_activity(self):
        try:
            activity_id = input("What is your activity id? ")
            number_of_persons = int(input("How many persons are participating in this activity? "))
            person_id = []
            for i in range(number_of_persons):
                ids = int(input("What is the person's id? "))
                person_id.append(ids)
            the_date = reading_the_date()
            the_time = reading_the_time()
            description = input("What is the description for the activity? ")
            validating_the_activity_input(activity_id, person_id, description)
        except UserInterfaceException as uie:
            print("There was a error that unfortunately said: " + str(uie))
        else:
            self._activity_service.updating_an_activity(activity_id, person_id, the_date, the_time, description)

    def listing_activities(self):
        list_of_activities = self._activity_service.get_list()
        for activity in list_of_activities:
            print (str(activity))

    def searching_an_activity(self):
        try:
            types = ["date", "time", "description"]
            print("By what would you like to search?")
            type = input(">")
            if type not in types:
                raise UserInterfaceException("The type is incorrect!")
        except UserInterfaceException as uie:
            print("There was a error that unfortunately said: " + str(uie))
        else:
            if type == "date":
                the_date = input ("What date? ")
                actual_date = self._activity_service.search_by_date(the_date)
                print("This is what you were looking for: " + str(actual_date))

            elif type == "time":
                the_time = input ("What time? ")
                actual_time = self._activity_service.search_by_time(the_time)
                print("This is what you were looking for: " + str(actual_time))

            elif type == "description":
                description = input("What is the description? ")
                actual_description = self._activity_service.search_by_description(description)
                print("This is what you were looking for: " + str(actual_description))

    def searching_a_person(self):
        try:
            types = ["name", "phone_number"]
            type = input("What would you like to search by? ")
            if type not in types:
                raise UserInterfaceException("The type is not correct!")
        except UserInterfaceException as uie:
            print("There was a error that unfortunately said: " + str(uie))
        else:
            if type == "name":
                name = input("What is the name? ")
                actual_name = self._person_service.search_by_name(name)
                print("This is what you were looking for: " + str(actual_name))
            elif type == "phone_number":
                phone_number = input("What is the phone_number? ")
                actual_phone = self._person_service.search_by_phone_number(phone_number)
                print("This is what you were looking for: " + str(actual_phone))

    def list_activities_for_given_date(self):
        sorted_list = []
        given_date = reading_the_date()
        sorted_list = self._activity_service.ordering_the_activities_by_their_start_time(given_date)
        for element in sorted_list:
            print(str(element))

    def list_the_upcoming_busiest_days(self):
        todays_date = date.today()
        list_of_days = []
        list_of_days = self._activity_service.creating_and_sorting_a_list_of_the_busiest_days(todays_date)
        for element in list_of_days:
            print(str(element))

    def list_activities_of_a_given_person(self):
        todays_date = date.today()
        list_of_activities = []
        person_id = input("What's the id of the person? ")
        list_of_activities = self._activity_service.activities_for_a_given_person(todays_date, person_id)
        for element in list_of_activities:
            print(str(element))

    def starting_menu(self):
        command = 0
        while command != "0":
            list_of_commands = ["0", "1.1", "1.2", "1.3", "1.4", "2.1", "2.2", "2.3", "2.4", "3.1", "3.2", "4",
                                "5", "6"]
            print("What would you like to do?")
            print("1.1. Add a person.")
            print("1.2. Remove a person.")
            print("1.3. Update a person.")
            print("1.4. List all persons.")
            print('----------------------------------')
            print("2.1. Add an activity.")
            print("2.2. Remove an activity.")
            print("2.3. Update an activity.")
            print("2.4. List all activities.")
            print('----------------------------------')
            print("3.1. Search for a person.")
            print("3.2. Search for an activity.")
            print('----------------------------------')
            print("Statistics:")
            print("4. Activities for a given date.")
            print("5. Busiest days.")
            print("6. Activities with a given person.")
            print('----------------------------------')
            print("Otherwise... press 0 to exit the program!")
            try:
                command = input(">")
                if command not in list_of_commands:
                    raise UserInterfaceException("There is no such command silly! Try another :).")
            except UserInterfaceException as uie:
                print("There was a error of the type" + str(type(uie)) + "with the message:" + str(uie))
            except RepoException as re:
                print("There was a error of the type" + str(type(re)) + "with the message:" + str(re))
            except ServiceException as se:
                print("There was a error of the type" + str(type(se)) + "with the message:" + str(se))
            else:
                if command == "1.1":
                    self.adding_a_person()
                elif command == "1.2":
                    self.removing_a_person()
                elif command == "1.3":
                    self.updating_a_person()
                elif command == "1.4":
                    self.listing_persons()
                elif command == "2.1":
                    self.adding_an_activity()
                elif command == "2.2":
                    self.removing_an_activity()
                elif command == "2.3":
                    self.updating_an_activity()
                elif command == "2.4":
                    self.listing_activities()
                elif command == "3.1":
                    self.searching_a_person()
                elif command == "3.2":
                    self.searching_an_activity()
                elif command == "4":
                    self.list_activities_for_given_date()
                elif command == "5":
                    self.list_the_upcoming_busiest_days()
                elif command == "6":
                    self.list_activities_of_a_given_person()

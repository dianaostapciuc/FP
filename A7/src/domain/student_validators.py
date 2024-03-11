class studentvalidator:

    @staticmethod
    def _is_id_valid(id):
        return len(id) > 3

    def validate(self, student):

        errors = []
        # V1 - All properties are non-empty

        if not studentvalidator._is_id_valid(student.id):
            errors.append('Invalid id.')
        if len(student.name) < 3:
            errors.append('Student name should have at least 3 letters.')
        if student.group < 100 or student.group > 999:
            errors.append('There is no existent student group with that value.')

        if len(errors) > 0:
            raise StudentValidationException(errors)


class ValidatorException(Exception):
    def __init__(self, message_list="Validation error!"):
        self._message_list = message_list

    @property
    def messages(self):
        return self._message_list

    def __str__(self):
        result = ""
        for message in self.messages:
            result += message
            result += "\n"
        return result


class StudentException(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


class StudentValidationException(StudentException):

    def __init__(self, error_list):
        self._errors = error_list

    def __str__(self):
        result = ''

        for er in self._errors:
            result += er
            result += '\n'
        return result

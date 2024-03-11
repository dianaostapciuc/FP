from src.repository.memory_repo import MemoryRepo
from src.repository.binary_repo import BinaryFileRepo
from src.repository.textfile_repo import TextFileRepo
from src.services.services import StudentServices
from src.domain.student import student
from src.ui.ui import UserInterface
import random

if __name__ == "__main__":

    method = input("What repository would you like to work with? ")
    if method not in ["text", "memory", "binary"]:
        raise ValueError("Invalid implementation method")

    elif method == "text":
        repository = TextFileRepo("students.txt")

    elif method == "binary":
        repository = BinaryFileRepo("students.bin")

    else:
        repository = MemoryRepo()
        for i in range(10):
            student_names = ["John", "Anne", "Jade", "Chris", "Daryl", "Rick", "Rose", "Negan"]
            student_groups = [214, 215, 216, 217, 814, 815, 816, 817, 914, 915, 916, 917]
            new_student = student(random.randint(1000, 9999), student_names[random.randint(0, 6)], student_groups[random.randint(0, 10)])
            repository.add(new_student)

    services = StudentServices(repository)
    UI = UserInterface(services)

    UI.menu()


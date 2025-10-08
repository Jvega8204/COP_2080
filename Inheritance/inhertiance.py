# Implement this
class Student:
    def __init__(self, name, student_id, major):
        self._name = name
        self._student_id = student_id
        self._major = major
    def __str__(self):
        return f"Name: {self._name}, ID: {self._student_id}, Major: {self._major}"
class UndergraduateStudent(Student):
    def __init__(self, name, student_id, major, year):
        super().__init__(name, student_id, major)
        self.__year = year
    def __str__(self):
        return f"{super().__str__()}, Year: {self.__year}"
class GraduateStudent(Student):
    def __init__(self, name, student_id, major, thesis_topic):
        super().__init__(name, student_id, major)
        self.__thesis_topic = thesis_topic
    def __str__(self):
        return f"{super().__str__()}, Thesis Topic: {self.__thesis_topic}"
# Usage
undergrad = UndergraduateStudent("Alice Smith", "U12345", "Computer Science",
"Sophomore")
grad = GraduateStudent("Bob Johnson", "G67890", "Physics", "Quantum Computing")
print(undergrad)
print(grad)
def f(student):
    print(student)
f(undergrad)
f(grad)

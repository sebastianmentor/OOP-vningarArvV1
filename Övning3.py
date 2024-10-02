class Person:
    def __init__(self, namn) -> None:
        self.namn = namn

class Student(Person):
    def __init__(self, namn, studieprogram) -> None:
        super().__init__(namn)
        self.studieprogram = studieprogram

class Lärare(Person):
    def __init__(self, namn, ämne) -> None:
        super().__init__(namn)
        self.ämne = ämne


stud = Student("Kalle", "Pythonutvecklare med inriktning AI")
lärare = Lärare("Sebastian", "Programmering med Python")


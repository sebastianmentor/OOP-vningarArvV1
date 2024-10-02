class Djur:
    def __init__(self, namn, ålder) -> None:
        self.namn = namn
        self.ålder = ålder

class Hund(Djur):
    def skälla(self):
        print("Voff!!")


fido = Hund("Fido", 8)
fido.skälla()
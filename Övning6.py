class Byggnad:
    def __init__(self, antal_våningar, yta) -> None:
        self.antal_våningar = antal_våningar
        self.yta = yta

class Bostadshus(Byggnad):
    def antal_personer(self):
        return round(self.yta/20)

class Kontor(Byggnad):
    def antal_personer(self):
        return round(self.yta/8)
    
bostad = Bostadshus(2, 88)
kontor = Kontor(6, 414)

print(f"Det får plats {bostad.antal_personer()} personer i bostaden!")
print(f"Det får plats {kontor.antal_personer()} personer på kontoret!")

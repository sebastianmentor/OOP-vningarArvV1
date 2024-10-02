class Anställd:
    def __init__(self, namn, lön) -> None:
        self.namn = namn
        self.lön = lön

class Heltid(Anställd):
    def __init__(self, namn, lön) -> None:
        super().__init__(namn, lön)
    
    def årslön(self):
        return 12 * self.lön

class Deltid(Anställd):
    def __init__(self, namn, lön, procent) -> None:
        super().__init__(namn, lön)
        self.procent = procent

    def årslön(self):
        return 12 * self.lön * self.procent
    

fast_anställd = Heltid("Kalle", 25000)
print(fast_anställd.årslön())

slav_anställd = Deltid("Knatte", 25000, 0.25)
print(slav_anställd.årslön())
class Anställd:
    def __init__(self, timlön) -> None:
        self.timlön = timlön

    def beräkna_lön(self):
        raise NotImplementedError
    
class Heltidsanställd(Anställd):
    def beräkna_lön(self):
        return self.timlön * 175


class Timanställd(Anställd):
    def __init__(self, timlön, antal_timmar_arbetade) -> None:
        super().__init__(timlön)
        self.antal_timmar = antal_timmar_arbetade

    def beräkna_lön(self):
        return self.timlön * self.antal_timmar
    

kalle = Heltidsanställd(125)

janne = Timanställd(140, 120)

print(f"Kalle får {kalle.beräkna_lön()} i lön den här månaden!")
print(f"Janne får {janne.beräkna_lön()} i lön den här månaden!")


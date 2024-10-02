class ElektronikApparat:
    def __init__(self, märke, energiförbrukning) -> None:
        self.märke = märke
        self.enegiförbrukning = energiförbrukning

    def energiklassificering(self):
        förbrukning = self.enegiförbrukning
        if förbrukning < 20:
            return "A"
        elif förbrukning < 40:
            return "B"
        elif förbrukning < 60:
            return "C"
        else:
            return "D"
        
    
class Kylskåp(ElektronikApparat):
    def __init__(self, märke, energiförbrukning, volym) -> None:
        super().__init__(märke, energiförbrukning)
        self.volym = volym

class TV(ElektronikApparat):
    def __init__(self, märke, energiförbrukning, skärmstorlek) -> None:
        super().__init__(märke, energiförbrukning)
        self.skärmstorlek = skärmstorlek
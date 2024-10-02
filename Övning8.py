class Transport:
    def __init__(self, hastighet) -> None:
        self.hastighet = hastighet
    

class Båt(Transport):
    def __init__(self, hastighet, vatten_typ) -> None:
        super().__init__(hastighet)
        self.vatten_typ = vatten_typ

class Flygplan(Transport):
    def __init__(self, hastighet, flyghöjd) -> None:
        super().__init__(hastighet)
        self.flyghöjd = flyghöjd


class Fordon:
    def köra(self):
        # Magic ;D
        print(self.__class__.__name__)

class Bil(Fordon):
    def tuta(self):
        print("Tuttut")

class Cyckel(Fordon):
    def ringklocka(self):
        print("Ringring")


bil = Bil()
bil.köra()
bil.tuta()

cyckel = Cyckel()
cyckel.köra()
cyckel.ringklocka()

  
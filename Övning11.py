class Figur:
    def beräkna_area(self):
        # Antingen lyfter vi ett fel för att subklasser inte har implementerat denna metod!
        raise NotImplementedError
        # Annars brukar man returnear NotImplemented i dom fall när vi tar in andra klasser
        # if not isinstance(value, obj):
        #   return NotImplemented        
    
class Rektangel(Figur):
    def beräkna_area(self):
        ...

class Cirkel(Figur):
    def beräkna_area(self):
        ...

class Tiangel(Figur):
    ...

rek = Rektangel()
rek.beräkna_area()

cir = Cirkel()
cir.beräkna_area()

tri = Tiangel()
tri.beräkna_area()


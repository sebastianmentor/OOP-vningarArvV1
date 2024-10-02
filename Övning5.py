class Växt:
    def __init__(self, höjd) -> None:
        self.höjd = höjd

class Träd(Växt):
    def väx(self):
        self.höjd*=1.01

class Blomma(Växt):
    def väx(self):
        self.höjd*=1.05


träd = Träd(10)
träd_längd_ursprung = träd.höjd
blomma = Blomma(10)
blomma_längd_ursprung = blomma.höjd

for tid in range(100):
    träd.väx()
    blomma.väx()

print(f"Efter 100 tidsenheter så är höjden på trädet {träd.höjd:.1f}. Det var {träd_längd_ursprung} från början!")
print(f"Efter 100 tidsenheter så är höjden på blomman {blomma.höjd:.1f}. Det var {blomma_längd_ursprung} från början!")




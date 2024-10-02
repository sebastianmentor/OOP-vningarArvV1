# Dum uppgift. Behövs mer information
class Spel:
    def __init__(self, spelare, poäng) -> None:
        self.spelare = spelare
        self.poäng = poäng

class Fotboll(Spel):
    def räkna_poäng(self):
        ...

class Basket(Spel):
    def räkna_poäng(self):
        ...
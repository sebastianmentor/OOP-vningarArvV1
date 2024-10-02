class Konto:
    def __init__(self, saldo=0) -> None:
        self._saldo = saldo

    def uttagsbegränsning(self):
        return 100_000_000
    
class Sparkonto(Konto):
    def __init__(self, saldo=0, uttag_denna_månad=0) -> None:
        super().__init__(saldo)
        self.uttag_denna_månad = uttag_denna_månad
        self.begränsning = 10_000

    def uttagsbegränsning(self):
        if self.uttag_denna_månad < self.begränsning:
            return self.begränsning - self.uttag_denna_månad
        else:
            return 0
        
class Lönekonto(Konto):
    def __init__(self, saldo=0, uttag_denna_dag=0) -> None:
        super().__init__(saldo)
        self.uttag_denna_dag = uttag_denna_dag
        self.begränsning = 5000

    def uttagsbegränsning(self):
        if self.uttag_denna_dag < self.begränsning:
            return self.begränsning - self.uttag_denna_dag
        else:
            return 0
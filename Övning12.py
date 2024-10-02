class Bibliotek:
    def __init__(self) -> None:
        self.böcker = []

    def lägg_till_bok(self, bok):
        self.böcker.append(bok)


class DigitaltBibliotek(Bibliotek):
    def __init__(self) -> None:
        super().__init__()
        self.länk_till_bok = {}

    def lägg_till_bok(self, bok):
        super().lägg_till_bok(bok)
        self.lägg_till_bok[bok] = "länk"
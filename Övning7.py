class Instrument:
    def spela(self):
        print("Instrumentet låter!")


class Gitarr(Instrument):
    def spela(self):
        # super().spela()
        print("Gitarren plinkar")

class Piano(Instrument):
    def spela(self):
        # super().spela()
        print("Pianot plinkar")

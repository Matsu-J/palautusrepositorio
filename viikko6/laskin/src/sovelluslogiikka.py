class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = {
            "nykyinen": arvo,
            "edellinen": 0
        }

    def miinus(self, operandi):
        self._arvo["edellinen"] = self._arvo["nykyinen"]
        self._arvo["nykyinen"] -= operandi

    def plus(self, operandi):
        self._arvo["edellinen"] = self._arvo["nykyinen"]
        self._arvo["nykyinen"] += operandi

    def nollaa(self):
        self.arvo["edellinen"] = self._arvo["nykyinen"]
        self._arvo["nykyinen"] = 0
    
    def kumoa(self):
        self._arvo["nykyinen"] = self._arvo["edellinen"]

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo["nykyinen"]

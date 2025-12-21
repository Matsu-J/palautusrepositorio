from kps import KiviPaperiSakset
from tekoaly import Tekoaly

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = Tekoaly()

    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")
        self.tekoaly.aseta_siirto(ekan_siirto)
        return tokan_siirto
    
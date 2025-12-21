import unittest
from luo_peli import luo_peli
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class TestLuoPeli(unittest.TestCase):
    def test_luo_pelaaja_vs_pelaaja(self):
        peli = luo_peli('a')
        self.assertIsInstance(peli, KPSPelaajaVsPelaaja)

    def test_luo_tekoaly_peli(self):
        peli = luo_peli('b')
        self.assertIsInstance(peli, KPSTekoaly)

    def test_luo_parannettu_tekoaly_peli(self):
        peli = luo_peli('c')
        self.assertIsInstance(peli, KPSParempiTekoaly)

    def test_virheellinen_tyyppi_palauttaa_none(self):
        peli = luo_peli('x')
        self.assertIsNone(peli)

if __name__ == '__main__':
    unittest.main()

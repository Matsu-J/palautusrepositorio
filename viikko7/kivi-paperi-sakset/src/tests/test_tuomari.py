import unittest
from tuomari import Tuomari

class TestTuomari(unittest.TestCase):
    def setUp(self):
        self.tuomari = Tuomari()

    def test_alkutilanne_pisteet_ovat_nolla(self):
        self.assertEqual(self.tuomari.ekan_pisteet, 0)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)
        self.assertEqual(self.tuomari.tasapelit, 0)

    def test_tasapeli_kirjataan_oikein(self):
        self.tuomari.kirjaa_siirto("k", "k")
        self.assertEqual(self.tuomari.ekan_pisteet, 0)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)
        self.assertEqual(self.tuomari.tasapelit, 1)

    def test_eka_voittaa_kivi_sakset(self):
        self.tuomari.kirjaa_siirto("k", "s")
        self.assertEqual(self.tuomari.ekan_pisteet, 1)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)
        self.assertEqual(self.tuomari.tasapelit, 0)

    def test_eka_voittaa_paperi_kivi(self):
        self.tuomari.kirjaa_siirto("p", "k")
        self.assertEqual(self.tuomari.ekan_pisteet, 1)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)

    def test_eka_voittaa_sakset_paperi(self):
        self.tuomari.kirjaa_siirto("s", "p")
        self.assertEqual(self.tuomari.ekan_pisteet, 1)
        self.assertEqual(self.tuomari.tokan_pisteet, 0)

    def test_toka_voittaa_kivi_sakset(self):
        self.tuomari.kirjaa_siirto("s", "k")
        self.assertEqual(self.tuomari.ekan_pisteet, 0)
        self.assertEqual(self.tuomari.tokan_pisteet, 1)

    def test_toka_voittaa_paperi_kivi(self):
        self.tuomari.kirjaa_siirto("k", "p")
        self.assertEqual(self.tuomari.ekan_pisteet, 0)
        self.assertEqual(self.tuomari.tokan_pisteet, 1)

    def test_toka_voittaa_sakset_paperi(self):
        self.tuomari.kirjaa_siirto("p", "s")
        self.assertEqual(self.tuomari.ekan_pisteet, 0)
        self.assertEqual(self.tuomari.tokan_pisteet, 1)

    def test_useita_kierroksia(self):
        self.tuomari.kirjaa_siirto("k", "s")  # eka voittaa
        self.tuomari.kirjaa_siirto("p", "p")  # tasapeli
        self.tuomari.kirjaa_siirto("s", "k")  # toka voittaa
        
        self.assertEqual(self.tuomari.ekan_pisteet, 1)
        self.assertEqual(self.tuomari.tokan_pisteet, 1)
        self.assertEqual(self.tuomari.tasapelit, 1)

    def test_str_metodi(self):
        self.tuomari.kirjaa_siirto("k", "s")
        tulos = str(self.tuomari)
        self.assertIn("1 - 0", tulos)
        self.assertIn("Tasapelit: 0", tulos)

if __name__ == '__main__':
    unittest.main()

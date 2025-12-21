import unittest
from tekoaly_parannettu import TekoalyParannettu

class TestTekoalyParannettu(unittest.TestCase):
    def setUp(self):
        self.tekoaly = TekoalyParannettu(10)

    def test_tekoaly_palauttaa_valida_siirto(self):
        siirto = self.tekoaly.anna_siirto()
        self.assertIn(siirto, ['k', 'p', 's'])

    def test_alkutilassa_antaa_kiven(self):
        siirto = self.tekoaly.anna_siirto()
        self.assertEqual(siirto, 'k')

    def test_muistaa_yhden_siirron(self):
        self.tekoaly.anna_siirto()  # ensimmäinen siirto
        self.tekoaly.aseta_siirto("k")
        siirto = self.tekoaly.anna_siirto()
        self.assertIn(siirto, ['k', 'p', 's'])

    def test_oppii_pelaajan_siirroista(self):
        # Anna muutama siirto
        self.tekoaly.anna_siirto()
        
        # Pelaaja pelaa useita kertoja kiven
        for _ in range(5):
            self.tekoaly.aseta_siirto("k")
            self.tekoaly.anna_siirto()
        
        # Tekoälyn pitäisi oppia ja antaa paperi (voittaa kiven)
        self.tekoaly.aseta_siirto("k")
        siirto = self.tekoaly.anna_siirto()
        self.assertEqual(siirto, 'p')

    def test_muisti_taytyy_oikein(self):
        tekoaly_pieni = TekoalyParannettu(3)
        
        # Täytetään muisti
        tekoaly_pieni.anna_siirto()
        tekoaly_pieni.aseta_siirto("k")
        tekoaly_pieni.anna_siirto()
        tekoaly_pieni.aseta_siirto("p")
        tekoaly_pieni.anna_siirto()
        tekoaly_pieni.aseta_siirto("s")
        
        # Lisää yksi siirto - vanhimman pitäisi poistua
        siirto = tekoaly_pieni.anna_siirto()
        self.assertIn(siirto, ['k', 'p', 's'])

if __name__ == '__main__':
    unittest.main()

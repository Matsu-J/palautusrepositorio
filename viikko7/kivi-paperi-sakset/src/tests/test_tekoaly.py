import unittest
from tekoaly import Tekoaly

class TestTekoaly(unittest.TestCase):
    def setUp(self):
        self.tekoaly = Tekoaly()

    def test_tekoaly_palauttaa_valida_siirto(self):
        siirto = self.tekoaly.anna_siirto()
        self.assertIn(siirto, ['k', 'p', 's'])

    def test_tekoaly_kiertaa_siirtoja(self):
        # Tekoäly antaa siirtoja kierrossa: p, s, k, p, s, k...
        siirrot = [self.tekoaly.anna_siirto() for _ in range(6)]
        self.assertEqual(siirrot, ['p', 's', 'k', 'p', 's', 'k'])

    def test_aseta_siirto_ei_tee_mitaan(self):
        # aseta_siirto ei tee mitään tavallisessa tekoälyssä
        self.tekoaly.aseta_siirto("k")
        siirto = self.tekoaly.anna_siirto()
        self.assertIn(siirto, ['k', 'p', 's'])

if __name__ == '__main__':
    unittest.main()

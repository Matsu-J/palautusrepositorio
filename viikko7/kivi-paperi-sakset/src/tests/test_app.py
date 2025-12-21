import unittest
import sys
import os

# Lisää src-hakemisto pythonin polkuun
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SECRET_KEY'] = 'test-secret-key'
        self.client = self.app.test_client()

    def test_index_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Kivi-Paperi-Sakset', response.data)

    def test_new_game_redirects_to_game(self):
        response = self.client.post('/new_game', data={'game_type': 'a'})
        self.assertEqual(response.status_code, 302)
        self.assertIn('/game', response.location)

    def test_new_game_invalid_type_redirects_to_index(self):
        response = self.client.post('/new_game', data={'game_type': 'x'})
        self.assertEqual(response.status_code, 302)
        self.assertIn('/', response.location)

    def test_game_page_without_session_redirects(self):
        response = self.client.get('/game')
        self.assertEqual(response.status_code, 302)

    def test_game_page_with_session_loads(self):
        with self.client.session_transaction() as sess:
            sess['game_type'] = 'a'
            sess['tuomari_ekan_pisteet'] = 0
            sess['tuomari_tokan_pisteet'] = 0
            sess['tuomari_tasapelit'] = 0
        
        response = self.client.get('/game')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Pelaaja 1: Tee siirtosi!', response.data)

    def test_make_move_vs_ai(self):
        with self.client.session_transaction() as sess:
            sess['game_type'] = 'b'
            sess['tuomari_ekan_pisteet'] = 0
            sess['tuomari_tokan_pisteet'] = 0
            sess['tuomari_tasapelit'] = 0
        
        response = self.client.post('/make_move', data={'move': 'k'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Kierroksen tulos', response.data)

    def test_make_move_invalid_move_redirects(self):
        with self.client.session_transaction() as sess:
            sess['game_type'] = 'b'
            sess['tuomari_ekan_pisteet'] = 0
            sess['tuomari_tokan_pisteet'] = 0
            sess['tuomari_tasapelit'] = 0
        
        response = self.client.post('/make_move', data={'move': 'x'})
        self.assertEqual(response.status_code, 302)

    def test_make_move_vs_player_shows_waiting(self):
        with self.client.session_transaction() as sess:
            sess['game_type'] = 'a'
            sess['tuomari_ekan_pisteet'] = 0
            sess['tuomari_tokan_pisteet'] = 0
            sess['tuomari_tasapelit'] = 0
        
        response = self.client.post('/make_move', data={'move': 'k'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Pelaaja 2: Tee siirtosi!', response.data)

    def test_second_move_completes_round(self):
        with self.client.session_transaction() as sess:
            sess['game_type'] = 'a'
            sess['tuomari_ekan_pisteet'] = 0
            sess['tuomari_tokan_pisteet'] = 0
            sess['tuomari_tasapelit'] = 0
            sess['waiting_for_second_move'] = 'k'
        
        response = self.client.post('/second_move', data={'move': 's'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Kierroksen tulos', response.data)

    def test_session_cleared_on_index(self):
        with self.client.session_transaction() as sess:
            sess['game_type'] = 'b'
            sess['tuomari_ekan_pisteet'] = 5
        
        self.client.get('/')
        
        with self.client.session_transaction() as sess:
            self.assertNotIn('game_type', sess)
            self.assertNotIn('tuomari_ekan_pisteet', sess)

if __name__ == '__main__':
    unittest.main()

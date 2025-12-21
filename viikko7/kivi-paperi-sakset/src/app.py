from flask import Flask, render_template, request, session, redirect, url_for
from luo_peli import luo_peli
from tuomari import Tuomari
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

WINNING_POINTS = 3
MAX_TIES = 5

def check_winner():
    ekan_pisteet = session.get('tuomari_ekan_pisteet', 0)
    tokan_pisteet = session.get('tuomari_tokan_pisteet', 0)
    tasapelit = session.get('tuomari_tasapelit', 0)
    if ekan_pisteet >= WINNING_POINTS:
        return 1
    elif tokan_pisteet >= WINNING_POINTS:
        return 2
    elif tasapelit >= MAX_TIES:
        return 0  # 0 tarkoittaa tasapelivoittoa
    return None

@app.route('/')
def index():
    # Nollaa sessio kun palataan etusivulle
    session.clear()
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
    game_type = request.form.get('game_type')
    if game_type not in ('a', 'b', 'c'):
        return redirect(url_for('index'))
    
    # Alusta uusi peli
    session['game_type'] = game_type
    session['tuomari_ekan_pisteet'] = 0
    session['tuomari_tokan_pisteet'] = 0
    session['tuomari_tasapelit'] = 0
    session['tekoaly_siirrot'] = []  # Tallenna tekoälyn aiemmat siirrot
    
    return redirect(url_for('game'))

@app.route('/game')
def game():
    if 'game_type' not in session:
        return redirect(url_for('index'))
    
    winner = check_winner()
    if winner is not None:
        return redirect(url_for('show_winner', winner=winner))
    
    game_type = session['game_type']
    game_type_names = {
        'a': 'Pelaaja vs Pelaaja',
        'b': 'Pelaaja vs Tekoäly',
        'c': 'Pelaaja vs Parannettu Tekoäly'
    }
    
    return render_template('game.html', 
                         game_type=game_type,
                         game_type_name=game_type_names[game_type],
                         ekan_pisteet=session.get('tuomari_ekan_pisteet', 0),
                         tokan_pisteet=session.get('tuomari_tokan_pisteet', 0),
                         tasapelit=session.get('tuomari_tasapelit', 0))

@app.route('/make_move', methods=['POST'])
def make_move():
    if 'game_type' not in session:
        return redirect(url_for('index'))
    
    ekan_siirto = request.form.get('move')
    
    # Käytä KPS-luokan validointimetodia
    game_type = session['game_type']
    peli = luo_peli(game_type)
    
    if not peli._onko_ok_siirto(ekan_siirto):
        return redirect(url_for('game'))
    
    # Hae toisen pelaajan siirto
    if game_type == 'a':
        # Pelaaja vs pelaaja - odota toista siirtoa
        session['waiting_for_second_move'] = ekan_siirto
        return render_template('waiting.html', ekan_siirto=ekan_siirto)
    else:
        # Käytä KPS-luokan metodia toisen siirron saamiseen
        tokan_siirto = peli._toisen_siirto(ekan_siirto)
        
        # Tallenna tekoälyn siirrot sessioon parannettua tekoälyä varten
        if game_type == 'c':
            session['tekoaly_siirrot'] = session.get('tekoaly_siirrot', []) + [ekan_siirto]
    
    # Käsittele siirto
    tuomari = Tuomari()
    tuomari.ekan_pisteet = session.get('tuomari_ekan_pisteet', 0)
    tuomari.tokan_pisteet = session.get('tuomari_tokan_pisteet', 0)
    tuomari.tasapelit = session.get('tuomari_tasapelit', 0)
    
    tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
    
    # Tallenna tulokset sessioon
    session['tuomari_ekan_pisteet'] = tuomari.ekan_pisteet
    session['tuomari_tokan_pisteet'] = tuomari.tokan_pisteet
    session['tuomari_tasapelit'] = tuomari.tasapelit
    
    # Näytä kierroksen tulos
    return render_template('result.html',
                         ekan_siirto=ekan_siirto,
                         tokan_siirto=tokan_siirto,
                         ekan_pisteet=tuomari.ekan_pisteet,
                         tokan_pisteet=tuomari.tokan_pisteet,
                         tasapelit=tuomari.tasapelit,
                         game_type=game_type)

@app.route('/second_move', methods=['POST'])
def second_move():
    if 'waiting_for_second_move' not in session:
        return redirect(url_for('game'))
    
    ekan_siirto = session.pop('waiting_for_second_move')
    tokan_siirto = request.form.get('move')
    
    # Käytä KPS-luokan validointimetodia
    peli = luo_peli(session['game_type'])
    if not peli._onko_ok_siirto(tokan_siirto):
        return redirect(url_for('game'))
    
    # Käsittele siirto
    tuomari = Tuomari()
    tuomari.ekan_pisteet = session.get('tuomari_ekan_pisteet', 0)
    tuomari.tokan_pisteet = session.get('tuomari_tokan_pisteet', 0)
    tuomari.tasapelit = session.get('tuomari_tasapelit', 0)
    
    tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
    
    # Tallenna tulokset sessioon
    session['tuomari_ekan_pisteet'] = tuomari.ekan_pisteet
    session['tuomari_tokan_pisteet'] = tuomari.tokan_pisteet
    session['tuomari_tasapelit'] = tuomari.tasapelit
    
    # Näytä kierroksen tulos
    return render_template('result.html',
                         ekan_siirto=ekan_siirto,
                         tokan_siirto=tokan_siirto,
                         ekan_pisteet=tuomari.ekan_pisteet,
                         tokan_pisteet=tuomari.tokan_pisteet,
                         tasapelit=tuomari.tasapelit,
                         game_type=session['game_type'])

@app.route('/winner/<int:winner>')
def show_winner(winner):
    if 'game_type' not in session:
        return redirect(url_for('index'))
    ekan_pisteet = session.get('tuomari_ekan_pisteet', 0)
    tokan_pisteet = session.get('tuomari_tokan_pisteet', 0)
    tasapelit = session.get('tuomari_tasapelit', 0)
    game_type = session['game_type']
    # Tarkista että voittaja on validi
    if winner not in (0, 1, 2):
        return redirect(url_for('game'))
    if winner == 1 and ekan_pisteet < WINNING_POINTS:
        return redirect(url_for('game'))
    if winner == 2 and tokan_pisteet < WINNING_POINTS:
        return redirect(url_for('game'))
    if winner == 0 and tasapelit < MAX_TIES:
        return redirect(url_for('game'))
    return render_template('winner.html', winner=winner, ekan_pisteet=ekan_pisteet, tokan_pisteet=tokan_pisteet, tasapelit=tasapelit, game_type=game_type)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

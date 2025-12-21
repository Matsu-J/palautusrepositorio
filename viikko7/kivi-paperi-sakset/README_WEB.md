# Kivi-Paperi-Sakset Web-sovellus

Web-pohjainen Kivi-Paperi-Sakset peli Flask-sovelluksena.

## Ominaisuudet

- **Pelaaja vs Pelaaja**: Kaksi pelaajaa samalla laitteella
- **Pelaaja vs Tekoäly**: Pelaa yksinkertaista tekoälyä vastaan
- **Pelaaja vs Parannettu Tekoäly**: Pelaa muistavaa tekoälyä vastaan, joka oppii pelaajan siirroista

## Käyttöönotto

### 1. Asenna riippuvuudet

Jos käytät Poetrya:
```bash
poetry install
```

Tai pip:llä:
```bash
pip install flask
```

### 2. Käynnistä sovellus

```bash
cd src
python app.py
```

Tai Poetryn kautta:
```bash
poetry run python src/app.py
```

### 3. Avaa selaimessa

Avaa selain osoitteeseen: http://127.0.0.1:5000

## Pelaaminen

1. Valitse pelityyppi etusivulla
2. Tee siirtosi klikkaamalla kivi (✊), paperi (✋) tai sakset (✌️)
3. Katso kierroksen tulos
4. Jatka peliä tai lopeta

## Tekninen toteutus

Sovellus hyödyntää olemassa olevaa koodia:
- `tuomari.py` - Pitää kirjaa pisteistä
- `tekoaly.py` - Yksinkertainen tekoäly
- `tekoaly_parannettu.py` - Muistava tekoäly
- `luo_peli.py` - Pelien luontitehdas

Web-käyttöliittymä käyttää:
- Flask-kehystä
- Session-hallintaa pelitilan säilyttämiseen
- HTML-templateja (Jinja2)
- Responsiivista CSS-tyyliä

## Testit

Sovellukselle on toteutettu kattavat automaattiset testit:

### Unittest-testit

Yksikkötestit kattavat:
- **Tuomari** - Pisteiden lasku ja pelin logiikka
- **Tekoäly** - Yksinkertainen tekoäly
- **TekoalyParannettu** - Muistava tekoäly
- **Flask-sovellus** - Web-käyttöliittymän toiminnallisuus
- **Pelin luonti** - Factory-metodit

Testit ajetaan:
```bash
cd src
python -m unittest discover tests -v
```

### Robot Framework -testit

API-testit testaavat:
- Etusivun latautuminen
- Uuden pelin luonti eri pelimuodoille
- Virheellisten syötteiden käsittely
- Redirectit ja session hallinta

Robot Framework -testit ajetaan:
```bash
# Käynnistä ensin Flask-serveri
python src/app.py

# Aja testit toisessa terminaalissa
cd src
python -m robot tests/robot_api_tests.robot
```

### Kaikki testit kerralla

Aja kaikki testit skriptillä:
```bash
./run_tests.sh
```

**Huom:** Robot Framework -testit vaativat että Flask-serveri on käynnissä portissa 5000.

### Testitulokset

- **32 unittest-testiä** - Kaikki PASS ✓
- **6 Robot Framework API-testiä** - Kaikki PASS ✓

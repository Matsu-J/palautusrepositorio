*** Settings ***
Library    Browser
Suite Setup    Open Browser And Start Server
Suite Teardown    Close Browser And Stop Server

*** Variables ***
${SERVER_URL}    http://localhost:5001
${BROWSER}    chromium

*** Test Cases ***
Etusivu Latautuu Oikein
    [Documentation]    Tarkista että etusivu latautuu ja sisältää oikeat elementit
    Go To    ${SERVER_URL}
    Get Title    ==    Kivi-Paperi-Sakset
    Get Text    h1    ==    🎮 Kivi-Paperi-Sakset

Pelaaja vs Pelaaja Pelin Aloitus
    [Documentation]    Tarkista että pelaaja vs pelaaja peli käynnistyy
    Go To    ${SERVER_URL}
    Click    button[name="game_type"][value="a"]
    Get Text    h1    ==    Pelaaja vs Pelaaja
    Get Text    h2    contains    Pelaaja 1

Pelaaja vs Tekoäly Pelin Aloitus
    [Documentation]    Tarkista että pelaaja vs tekoäly peli käynnistyy
    Go To    ${SERVER_URL}
    Click    button[name="game_type"][value="b"]
    Get Text    h1    ==    Pelaaja vs Tekoäly

Pelaaja vs Parannettu Tekoäly Pelin Aloitus
    [Documentation]    Tarkista että parannettu tekoäly peli käynnistyy
    Go To    ${SERVER_URL}
    Click    button[name="game_type"][value="c"]
    Get Text    h1    ==    Pelaaja vs Parannettu Tekoäly

Pelaa Yksi Kierros Tekoälyä Vastaan
    [Documentation]    Pelaa yksi kierros ja tarkista että tulos näkyy
    Go To    ${SERVER_URL}
    Click    button[name="game_type"][value="b"]
    
    # Tee siirto (kivi)
    Click    button[name="move"][value="k"]
    
    # Tarkista että tulos näkyy
    Get Text    h1    ==    Kierroksen tulos
    Get Text    body    contains    Kierroksen tulos

Jatka Peliä Kierroksen Jälkeen
    [Documentation]    Tarkista että peliä voi jatkaa kierroksen jälkeen
    Go To    ${SERVER_URL}
    Click    button[name="game_type"][value="b"]
    Click    button[name="move"][value="k"]
    
    # Jatka peliä
    Click    text=Jatka peliä
    Get Text    h2    contains    Pelaaja 1

Lopeta Peli
    [Documentation]    Tarkista että pelin voi lopettaa
    Go To    ${SERVER_URL}
    Click    button[name="game_type"][value="b"]
    Click    button[name="move"][value="k"]
    
    # Lopeta peli
    Click    text=Lopeta peli
    Get Text    h1    ==    🎮 Kivi-Paperi-Sakset

Pelaaja vs Pelaaja Toinen Pelaaja
    [Documentation]    Testaa että toisen pelaajan siirto toimii
    Go To    ${SERVER_URL}
    Click    button[name="game_type"][value="a"]
    
    # Ensimmäinen pelaaja tekee siirron
    Click    button[name="move"][value="k"]
    
    # Tarkista että odotetaan toista pelaajaa
    Get Text    h1    ==    Pelaaja 2: Tee siirtosi!
    
    # Toinen pelaaja tekee siirron
    Click    button[name="move"][value="s"]
    
    # Tarkista että tulos näkyy
    Get Text    h1    ==    Kierroksen tulos

Testaa Kaikki Siirrot
    [Documentation]    Testaa että kaikki siirrot (kivi, paperi, sakset) toimivat
    
    # Testaa kivi
    Go To    ${SERVER_URL}
    Click    button[name="game_type"][value="b"]
    Click    button[name="move"][value="k"]
    Get Text    h1    ==    Kierroksen tulos
    
    # Testaa paperi
    Go To    ${SERVER_URL}
    Click    button[name="game_type"][value="b"]
    Click    button[name="move"][value="p"]
    Get Text    h1    ==    Kierroksen tulos
    
    # Testaa sakset
    Go To    ${SERVER_URL}
    Click    button[name="game_type"][value="b"]
    Click    button[name="move"][value="s"]
    Get Text    h1    ==    Kierroksen tulos

Pisteet Päivittyvät Oikein
    [Documentation]    Tarkista että pisteet päivittyvät pelin aikana
    Go To    ${SERVER_URL}
    Click    button[name="game_type"][value="b"]
    
    # Tee ensimmäinen siirto
    Click    button[name="move"][value="k"]
    
    # Tarkista että pistetaulukko on näkyvissä
    Get Text    .scoreboard    contains    Pelaaja 1
    Get Text    .scoreboard    contains    Tekoäly

*** Keywords ***
Open Browser And Start Server
    [Documentation]    Avaa selain ja käynnistä Flask-serveri
    New Browser    browser=${BROWSER}    headless=True
    New Context
    New Page    ${SERVER_URL}

Close Browser And Stop Server
    [Documentation]    Sulje selain
    Close Browser

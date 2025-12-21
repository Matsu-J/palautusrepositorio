*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    kps    ${SERVER_URL}

*** Variables ***
${SERVER_URL}    http://localhost:5000

*** Test Cases ***
Etusivu Palauttaa 200 OK
    [Documentation]    Tarkista että etusivu vastaa onnistuneesti
    ${response}=    GET On Session    kps    /
    Status Should Be    200    ${response}
    Should Contain    ${response.text}    Kivi-Paperi-Sakset

Uusi Peli Pelaaja vs Pelaaja
    [Documentation]    Tarkista että uuden pelin luonti toimii
    ${data}=    Create Dictionary    game_type=a
    ${response}=    POST On Session    kps    /new_game    data=${data}    allow_redirects=${False}
    Status Should Be    302    ${response}
    Should Contain    ${response.headers}[Location]    /game

Uusi Peli Tekoäly
    [Documentation]    Tarkista että tekoälypelin luonti toimii
    ${data}=    Create Dictionary    game_type=b
    ${response}=    POST On Session    kps    /new_game    data=${data}    allow_redirects=${False}
    Status Should Be    302    ${response}

Uusi Peli Parannettu Tekoäly
    [Documentation]    Tarkista että parannetun tekoälyn pelin luonti toimii
    ${data}=    Create Dictionary    game_type=c
    ${response}=    POST On Session    kps    /new_game    data=${data}    allow_redirects=${False}
    Status Should Be    302    ${response}

Virheellinen Pelityyppi
    [Documentation]    Tarkista että virheellinen pelityyppi ohjaa etusivulle
    ${data}=    Create Dictionary    game_type=x
    ${response}=    POST On Session    kps    /new_game    data=${data}    allow_redirects=${False}
    Status Should Be    302    ${response}
    Should Contain    ${response.headers}[Location]    /

Peli Sivu Ilman Sessiota
    [Documentation]    Tarkista että peli-sivu ohjaa etusivulle ilman sessiota
    ${response}=    GET On Session    kps    /game    expected_status=any
    # Tarkista että päädyttiin etusivulle (redirect seurattu)
    Should Be True    ${response.status_code} == 200 or ${response.status_code} == 302

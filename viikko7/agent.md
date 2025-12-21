Pyysin agenttia tekemää sovellukselle web käyttöliittymän ensin promptilla:

"Rakenna sovellukselle web käyttöliittymä hyödyntäen esimerkiksi Flask kirjastoa. Huomioi että sovelluksella on käytössä poetry joten tarkista sen riippuvuudet ensin tai lisää riippuvuudet sinne mikäli tarvitset lisää riippuvuuksia. Käytä mahdollisimman paljon olemassa olevaa koodia ja mieti tarkkaan ennen kuin rakennat uutta koodia. Käynnistä sovellus välillä ja tarkista että se toimii."

Tekoäly suoriutui tästä suhteellisen nopeasti, joskin tulosteli terminaaliin välillä turhia viestejä echo komennoilla. Tämän jälkeen pyysin tekemään sovellukselle sekä unittestit, että robot testit, sekä voittorajan viisi pistettä. Pyysin myös lisäämään tasapelirajaksi viisi pistettä.

Sovellus itsessään oli toimiva mutta alkuperäisestä toiveesta huolimatta tekoäly hyödynsi olemassa olevaa koodia heikosti joten siitä piti vielä muistuttaa erikseen. Tekoäly ei juurikaan koskenut alkuperäiseen koodiin ja hyödynsi edelleen app.py tiedostoa enemmän kuin alkuperäsitä koodia. Generoitu koodi on selkeää, joskin vähän toisteista. Esimerkiksi siirtojen käsittely esiintyy useamman kerran edelleen. Sovellus oli kuitenkin tästä huolimatta toimiva testattuani kaikki pelimuodot.

Tekoälyn tekemät testit vaikuttaisivat nopeasti katsottuna testaavan sovelluksen toimintaa kattavasti. Kuitenkin eräs huomio robot testeistä on, että resource.robot tiedostoa ei generoitu vaan sen sijaan testit ovat koodimaisemmassa muodossa eivätkä robot frameworkin mahdollistamassa helppolukuisessa muodossa. 

Opin tehtävästä enemmän koodin arvioimisesta sekä refaktoroinnista vähemmän toisteiseksi
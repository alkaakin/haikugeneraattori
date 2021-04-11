
<i>Tietokantasovellus Helsingin yo:n TKT-laitoksen tietokantasovelluskurssia varten</i>

# <b>Haikugeneraattori</b> :penguin:

## <b> https://haiku-generaattori.herokuapp.com/ </b>

Tällä hetkellä sovelluksesta on herokussa versio, joka mahdollistaa seuraavat toiminnot:

- Rekisteröityminen
- Kirjautuminen
- Haikun kirjoittaminen sisäänkirjautuneena (tässä valitaan haikun nimi, genre ja sisältö)
- Satunnaisen haikun generoiminen painamalla "HAIKU TIME"- nappia
- Kaikkien haikujen tarkastelu erikseen listana

Sovellusta tullaan kehittämään seuraavilla tavoin seuraavaan kurssin deadlineen mennessä:

- Eri käyttäjäryhmien luominen ja tunnistaminen
- Ulkoasun parantaminen 
- Haikujen generoiminen suoraan etusivulle sen sijaan, että sovellus näyttää haikun erillisellä sivulla
- Mahdollisuus arvostella (generoitua) haikua
- Mahdollisuus hakea haikuja eri parametrien avulla ja järjestää haikujen listausta (esim. arvosanan mukaan)


<b> TAVOITE SOVELLUKSELLE </b>

Sovellus antaa käyttäjälle mahdollisuuden tallettaa uusia haikuja ja generoida haikuja “satunnaisesti” vanhojen, jo tallennettujen haikujen avulla. Sovellus mahdollistaa lisäksi kaikkien haikujen katselun ja niiden arvostelun. 

## <b> Sovelluksen käyttäjäluokat </b>
- Superkäyttäjä (oikeus kirjoittaa haikuja, generoida haikuja, arvostella haikuja ja poistaa haikuja) 
- Kirjautunut käyttäjä (oikeus kirjoittaa haikuja, generoida haikuja ja arvostella haikuja)
- Ei-kirjautunut käyttäjä (oikeus generoida haikuja)

## <b> Sovelluksen ominaisuuksia </b>
- Sovelluksessa on kirjautumis/rekisteröitymisruutu. 
- Kirjautuminen tarvitaan haikun kirjoittamiseksi ja arvostelemiseksi.
- Haikuja on mahdollista arpoa ja tarkastella kirjautumatta.
- Vain superkäyttäjä voi poistaa jo tehtyjä haikuja.
- Sovellukseen voi syöttää haikun. Haiku syötetään tavuina, jotta varmistutaan sen haikuluonteesta.
- Haikun syöttämisen yhteydessä valitaan haikun genre (sci-fi, kauhu, romanttinen, kitsch, realismi)
- Kaikkia haikuja voi tarkastella erillisellä sivullaan. Ne voi myös arvostella tähdillä 1-5. 
- Haikuja voi tutkia käyttäjäkohtaisesti tai genren perusteella


# Geologisten kivinäytteiden keskustelupalsta

## Sovelluksen toiminnot
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy kirjaamaan ylös ja poistamaan geologisia näytteitä.
* Näytteen lisäämisen jälkeen käyttäjä pystyy lisäämään kuvia näytteiden liitteeksi (enintään 5 per näyte).
* Käyttäjä näkee sovellukseen muiden lisäämät näytteet.
* Käyttäjä pystyy etsimään näytteitä hakusanalla.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät näytteet.
* Käyttäjä pystyy valitsemaan näytteelle kivityypin, kivilajin, näytteen koordinaatit, näytteen käräyspäivämäärän, kivilajin ja lisäksi käyttäjä voi kirjoittaa vapaaseen kenttään kivilajin mineraalit kuvauksen yms.
* Käyttäjä pystyy esittämään kirjattuun näytteeseen kysymyksen / kysymyksiä, joihin muut käyttäjät voivat vastata.


Asenna `flask`-kirjasto, jos tätä ei ole jo asennettu

```
$ pip install flask
```

Luo tietokannan taulut

```
$ sqlite3 database.db < tables.sql
```

Alusta kategoriat

```
$ sqlite3 database.db < init.sql
```


Käynnistä sovellus

```
$ flask run
```

Aluksi sivustolla ei ole mitään lisäyksiä, mutta tässä esimerkkejä, joita voi lisätä:
Huomioi, että sivustolle täytyy olla kirjautunut, jotta voi tehdä lisäyksiä.

## Lisäyksiä
1. 
    * Näytetunnus: AL-74-3
    * Kivityyppi: Magmakivi
    * Koorinaatit: 6671210m N, 386381m E
    * Keräyspäivämäärä: 21.10.2024
    * Kivilaji: Graniitti
    * Kuvaus: Felsinen syväkivi Helsingin alueelta. Aksessorisena mineraalina fluoriitti.

2. 
    * Näytetunnus: BBKR-745
    * Kivityyppi: Metamorfinen kivi
    * Koorinaatit: 6823672m N, 329618m E
    * Keräyspäivämäärä: 12.2.2025
    * Kivilaji: Fylliitti
    * Kuvaus: Alhaiseen asteen metamorfinen kivi Tampereen liuskevyöhykkeeltä.

Esimerkkikuvat ovat kansiossa `Example images` nimettynä näytetunnusten mukaisesti.
Kuvat ovat Wikipediasta Creative Commons lisenssillä. Linkit alkuperäisiin tässä:

Fylliitin kuvat:

[Linkki kuvaan](https://commons.wikimedia.org/wiki/File:Phyllite_%28French_Slate,_Paleoproterozoic;_Snowy_Range_Road_roadcut,_Medicine_Bow_Mountains,_Wyoming,_USA%29_12_%2845625221651%29.jpg)

[Linkki kuvaan](https://commons.wikimedia.org/wiki/File:Phyllite_%28French_Slate,_Paleoproterozoic;_Snowy_Range_Road_roadcut,_Medicine_Bow_Mountains,_Wyoming,_USA%29_2_%2844711620975%29.jpg)

Graniitin kuva:

[Linkki kuvaan](https://commons.wikimedia.org/wiki/File:Biotite_Granite_-_Igneous_Rock.jpg)


Suurta tietomäärää on testattu `seed.py` tiedostolla. `seed.py` luo tuhat käyttäjää, miljoona näytettä ja kymmenen miljoonaa kommenttia.

Sivuston lataamiseen kuluva aika:
* Sivutus, ei indeksöintiä: n.23s
* Sivutus ja indeksöinti: n.0.03s
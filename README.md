# Geologisten kivinäytteiden keskustelupalsta

## Sovelluksen toiminnot
* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy kirjaamaan ylös ja poistamaan geologisia näytteitä.
* Käyttäjä pystyy lisäämään kuvia näytteiden liitteeksi. - EI VALMIS
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
* Näytetunnus: AL-74-3, Kivityyppi: Magmakivi, Koorinaatit 60.1699° N, 24.9384° E, Keräyspäivämäärä 21.10.2026, Kivilaji: Graniitti, Kuvaus: Felsinen syväkivi Helsingin alueelta.
* Näytetunnus: BBKR-745, Kivityyppi: Metamorfinen kivi, Koorinaatit 661.4971° N, 23.7526° E, Keräyspäivämäärä 29.10.2026, Kivilaji: Fylliitti, Kuvaus: Alhaiseen asteen metamorfinen kivi Tampereen liuskevyöhykkeeltä.


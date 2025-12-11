# Pylint-raportti

Pylint antaa seuraavan raportin sovelluksesta:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:11:0: C0410: Multiple imports on one line (db, users, forum) (multiple-imports)
app.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:35:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:55:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:45:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:64:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:69:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:77:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:106:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:143:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:157:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:167:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:167:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:190:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:207:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:207:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:232:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:232:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:253:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:253:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:274:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:274:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:331:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:338:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:364:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:379:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:384:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:392:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:397:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:401:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:408:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:414:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:418:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.71/10 (previous run: 8.68/10, +0.04)

************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)

************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:41:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.78/10 (previous run: 7.04/10, +0.74)

************* Module db
db.py:18:27: C0303: Trailing whitespace (trailing-whitespace)
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)

------------------------------------------------------------------
Your code has been rated at 6.00/10 (previous run: 5.00/10, +1.00)

************* Module forum
forum.py:1:0: C0114: Missing module docstring (missing-module-docstring)
forum.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:18:0: R0913: Too many arguments (8/5) (too-many-arguments)
forum.py:18:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
forum.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:34:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:39:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:48:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:55:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:62:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:66:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:70:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:74:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:74:0: R0913: Too many arguments (8/5) (too-many-arguments)
forum.py:74:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
forum.py:93:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:93:0: R0913: Too many arguments (8/5) (too-many-arguments)
forum.py:93:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
forum.py:112:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:125:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:132:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:139:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:146:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:153:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:157:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:161:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.30/10 (previous run: 7.10/10, +0.20)
```

Käydään ilmoitukset läpi:

## Docstring-ilmoitukset

Suuri osa ilmoituksista ovat seuraavan tyyppisiä:

```
app.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:1:0: C0114: Missing module docstring (missing-module-docstring)
```

Tässä ilmoitetaan ettei moduuleissa tai functiossa ole docstring-kommentteja. Nämä on tietoisesti jätetty pois.

## Tarpeeton else

Raportissa on seuraavia ilmoituksia liittyen `else`-haaroihin:

```
app.py:379:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:379:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
```

Koodin näissä osioissa voisi kirjoittaa tiiviimmin, mutta koodin selkeyden kannalta on tehty päätös, että käytetään useampia else-haarjoa

## Puuttuva palautusarvo

```
app.py:232:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:253:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```

Nämä ilmoitukset liittyvät funtiooihin, joissa käytetään ["GET] ja ["POST] metodeja. Funtiossa on kuitenkin määritelty, että tälle tulee antaa jompi kumpi, joten tilannetta jossa funtio ei palauta arvoa ei voi tapahtua.

## Vaarallinen oletusarvo

```
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
```

db.py tiedostossa on tyhjiä listoja oletusolioina, mutta kun koodissa ei ole muita listaolijoita niin tästä ei ole riskiä.

## Vakion nimi

```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
```

config.py:ssä on nimetty muuttuja secret_key, joka pitäisi nimetä isoilla kirjaimilla. Tämä kuitenkin toteutettu kurssin materiaalin mukaisesti, joten en näe tässä ongelmaa.

## Importit samalla rivillä

```
app.py:11:0: C0410: Multiple imports on one line (db, users, forum) (multiple-imports)
```

Varoitetaan useasta tuonnista samalla rivillä, en näe tässä ongelmaa.

## Liian monta muuttujaa

```
forum.py:18:0: R0913: Too many arguments (8/5) (too-many-arguments)
```

Tässä varoitetaan liian monesta argumentista. Huomioiden tietokannan rakenteen en keksinyt muuta tapaa tehdä tätä.
Toki argumentit voisi antaa listana, joka puretaan funktion sisällä. Kuitenkin tämä mielestäni toisi koodiin turhia rivejä ja monimutkaisuutta.

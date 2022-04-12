# Lukuvinkkikirjasto

![GitHub Action](https://github.com/kimmomuli/Lukuvinkkikirjasto/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/kimmomuli/Lukuvinkkikirjasto/branch/main/graph/badge.svg?token=06TFSWVEKM)](https://codecov.io/gh/kimmomuli/Lukuvinkkikirjasto)

[Linkki sovellukseen](https://lukuvinkkikirjasto2.herokuapp.com/)

## Asennusohjeet
1. Luo `.env` tiedosto projektin juureen ja lisää seuraavat rivit sinne
    ```
    SECRET_KEY=<secret_key>
    DATABASE_URL=<postgresql:///tietokannan_nimi>
    ```
    Missä `<secret_key>` on salainen avain ja `<postgresql:///tietokannan_nimi>` on tietokannan osoite.  
    Salaisen avaimen saa luotua esimerkiksi Python-tulkissa:
    ```
    $ python3
    >>> import secrets
    >>> secrets.token_hex(32)
    <pitkä satunnainen merkkijono>
    ```

2. Asenna riippuvuudet
    ```
    $ poetry install
    ```

## Projektin ajaminen
```
$ poetry run invoke start
```

## Testien ajaminen
1. Luo `.env.test` tiedosto projektin juureen ja lisää seuraa rivi sinne
    ```
    DATABASE_URL=<postgresql:///testi_tietokannan_nimi>
    ```
    Missä `<postgresql:///testi_tietokannan_nimi>` on testeissä käytettävän tietokannan osoite.  
2. Aja testit
    ```
    $ poetry run invoke test
    ```

## Testien kattavuusraportin luominen
```
$ poetry run invoke coverage-report
```

## Pylint

```
poetry run invoke lint
```

## Backlogs ja burndown
[Product backlog ja sprint backlog](https://github.com/kimmomuli/Lukuvinkkikirjasto/projects/1)

<img src="https://user-images.githubusercontent.com/80842633/161778761-6f1b80e4-c75d-4a54-beff-cd797fe3de0c.png" width="600">

## DoD
![Definition of done ](https://github.com/kimmomuli/Lukuvinkkikirjasto/blob/main/dokumentaatio/definiton_of_done.md)


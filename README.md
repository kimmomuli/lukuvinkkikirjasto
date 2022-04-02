# Lukuvinkkikirjasto

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
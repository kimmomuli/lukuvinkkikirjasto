*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Open Register Page


*** Test Cases ***
Luo Kayttaja Ja Kirjaudu Sisaan
    Set Kayttajatunnus  robotti
    Set Salasana  robotti123
    Submit Register Credentials
    Home Page Should Be Open
    Log Out
    Go To Kirjautuminen Page
    Kirjautuminen Page Should Be Open
    Set Kayttajatunnus  robotti
    Set Salasana  robotti123
    Submit Login Credentials
    Home Page Should Be Open

Luo Kayttaja Olemassa Olevalla Kayttajatunnuksella
    Create User  robotti  robotti123
    Set Kayttajatunnus  robotti
    Set Salasana  robotti123
    Submit Register Credentials
    Rekisteroityminen Page Should Be Open
    Page Should contain  Käyttäjätunnus on jo olemassa

Luo Kayttaja Liian Lyhyella Kayttajatunnuksella
    Set Kayttajatunnus  rob
    Set Salasana  robotti123
    Submit Register Credentials
    Rekisteroityminen Page Should Be Open
    Page Should contain  Kayttäjätunnukset on oltava vähintään 4 merkkiä pitkä

Luo Kayttaja Liian Lyhyella Salasanalla
    Set Kayttajatunnus  robotti
    Set Salasana  robot
    Submit Register Credentials
    Rekisteroityminen Page Should Be Open
    Page Should contain  Salasanan on oltava vähintään 6 merkkiä pitkä

Kirjaudu Sisaan vaaralla kayttajatunnuksella
    Create User  robotti  robotti123
    Go To Kirjautuminen Page
    Kirjautuminen Page Should Be Open
    Set Kayttajatunnus  robotti1
    Set Salasana  robotti123
    Submit Login Credentials
    Kirjautuminen Page Should Be Open
    Page Should contain  Väärä käyttäjätunnus tai salasana

Kirjaudu Sisaan vaaralla salasanalla
    Create User  robotti  robotti123
    Go To Kirjautuminen Page
    Kirjautuminen Page Should Be Open
    Set Kayttajatunnus  robotti
    Set Salasana  robotti12
    Submit Login Credentials
    Kirjautuminen Page Should Be Open
    Page Should contain  Väärä käyttäjätunnus tai salasana

Luo Uusi Vinkki Linkki Ei Ole Nakyvissa Jos Kayttaja Ei Ole Kirjautunut Sisaan
    Go To Home Page
    Page Should Not Contain  Luo Uusi Vinkki

Luo Uusi Vinkki Linkki On Nakyvissa Jos Kayttaja On Kirjautunut Sisaan
    Create User And Log In
    Page Should Contain  Luo uusi vinkki

*** Keywords ***
Lisaa Vinkki
    Click Button  luo vinkki

Log Out
    Click Link  Kirjaudu ulos

Submit Login Credentials
    Click Button  Kirjaudu

Submit Register Credentials
    Click Button  Rekisteröidy

Set Kayttajatunnus
    [Arguments]  ${kayttajatunnus}
    Input Text  tunnus  ${kayttajatunnus}

Set Salasana
    [Arguments]  ${salasana}
    Input Password  salasana  ${salasana}

Open Register Page
    Reset Application
    Go To Rekisteroityminen Page
    Rekisteroityminen Page Should Be Open
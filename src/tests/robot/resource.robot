*** Settings ***
Library  SeleniumLibrary
Library  ./AppLibrary.py


*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${LISAA URL}  http://${SERVER}/uusi_vinkki
${REKISTEROITYMINEN URL}  http://${SERVER}/rekisteroityminen
${KIRJAUTUMINEN URL}  http://${SERVER}/kirjautuminen

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  Lukuvinkkisovellus - Lukuvinkit

Rekisteroityminen Page Should Be Open
    Title Should Be  Lukuvinkkisovellus - Rekisteröidy

Kirjautuminen Page Should Be Open
    Title Should Be  Lukuvinkkisovellus - Kirjaudu sisään

Lisaa Page Should Be Open
    Title Should Be  Lukuvinkkisovellus - Luo lukuvinkki

Go To Home Page
    Go To  ${HOME URL}

Go To Rekisteroityminen Page
    Go To  ${REKISTEROITYMINEN URL}

Go To Kirjautuminen Page
    Go To  ${KIRJAUTUMINEN URL}

Go To Lisaa Page
    Go To  ${LISAA URL}

Reset Application And Delete Cookies
    Reset Application
    Delete All Cookies

Create User And Log In
    [Arguments]  ${kayttajatunnus}  ${salasana}
    Create User  ${kayttajatunnus}  ${salasana}
    Go To Kirjautuminen Page
    Kirjautuminen Page Should Be Open
    Input Text  tunnus  ${kayttajatunnus}
    Input Text  salasana  ${salasana}
    Click Button  Kirjaudu
    Home Page Should Be Open

Add Kirjavinkki And Go To Home Page
    [Arguments]  ${otsikko}  ${kirjailija}  ${kirjoitusvuosi}  ${lisaaja}
    Lisaa Kirjavinkki  ${otsikko}  ${kirjailija}  ${kirjoitusvuosi}  ${lisaaja}
    Go To Home Page
    Home Page Should Be Open
    Page Should Contain  ${otsikko}
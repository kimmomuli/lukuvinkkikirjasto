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
    Title Should Be  Lukuvinkkisovellus - Kirjaudu tai rekisteröidy
    Page Should Contain  Rekisteröidy

Kirjautuminen Page Should Be Open
    Title Should Be  Lukuvinkkisovellus - Kirjaudu tai rekisteröidy
    Page Should Contain  Kirjaudu

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
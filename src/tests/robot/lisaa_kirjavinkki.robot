*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Database And Create User


*** Test Cases ***
Lisaa Vinkki Validilla Otsikolla Kirjailijalla Ja Vuodella
    Go To Kirjautuminen Page
    Set Kayttajatunnus  robotti
    Set Salasana  robotti123
    Submit Credentials
    Click Link  Luo uusi vinkki
    Lisaa Page Should Be Open
    Set Otsikko  Sinuhe egyptiläinen
    Set Kirjailija  Mika Waltari
    Set Kirjoitusvuosi  1945
    Lisaa Vinkki
    Home Page Should Be Open


*** Keywords ***
Lisaa Vinkki
    Click Button  luo vinkki

Submit Credentials
    Click Button  Kirjaudu

Lisays Should Succeed
    Home Page Should Be Open

Set Otsikko
    [Arguments]  ${otsikko}
    Input Text  otsikko  ${otsikko}

Set Kirjailija
    [Arguments]  ${kirjailija}
    Input Text  kirjailija  ${kirjailija}

Set Kirjoitusvuosi
    [Arguments]  ${kirjoitusvuosi}
    Input Text  kirjoitusvuosi  ${kirjoitusvuosi}

Set Kayttajatunnus
    [Arguments]  ${kayttajatunnus}
    Input Text  tunnus  ${kayttajatunnus}

Set Salasana
    [Arguments]  ${salasana}
    Input Password  salasana  ${salasana}

Reset Database And Create User
    Create User  robotti  robotti123
    Go To Kirjautuminen Page
    Kirjautuminen Page Should Be Open
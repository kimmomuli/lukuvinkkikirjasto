*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Database And Create User And Log In And Go To Lisaa Page


*** Test Cases ***
Lisaa Vinkki Validilla Otsikolla Kirjailijalla Ja Vuodella
    Set Otsikko  Sinuhe egyptiläinen
    Set Kirjailija  Mika Waltari
    Set Kirjoitusvuosi  1945
    Lisaa Vinkki
    Home Page Should Be Open

Lisaa Vinkki Liian Lyhyella Otsikolla
    Set Otsikko  S
    Set Kirjailija  Mika Waltari
    Set Kirjoitusvuosi  1945
    Lisaa Vinkki
    Lisaa Page Should Be Open
    Page Should Contain  Otsikon tulee sisältää ainakin kaksi merkkiä

Lisaa Vinkki Liian Lyhyella Kirjailijan Nimella
    Set Otsikko  Sinuhe egyptiläinen
    Set Kirjailija  M
    Set Kirjoitusvuosi  1945
    Lisaa Vinkki
    Lisaa Page Should Be Open
    Page Should Contain  Kirjailijan nimen tulee sisältää ainakin kaksi merkkiä

Lisaa Vinkki Liian Pienella Kirjoitusvuodella
    Set Otsikko  Sinuhe egyptiläinen
    Set Kirjailija  Mika Waltari
    Set Kirjoitusvuosi  0
    Lisaa Vinkki
    Lisaa Page Should Be Open
    Page Should Contain  Kirjoitusvuoden pitää olla numero väliltä 1-2025

Lisaa Vinkki Liian Suurella Kirjoitusvuodella
    Set Otsikko  Sinuhe egyptiläinen
    Set Kirjailija  Mika Waltari
    Set Kirjoitusvuosi  2026
    Lisaa Vinkki
    Lisaa Page Should Be Open
    Page Should Contain  Kirjoitusvuoden pitää olla numero väliltä 1-2025

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

Reset Database And Create User And Log In And Go To Lisaa Page
    Reset Application
    Create User And Log In
    Click Link  Luo uusi vinkki
    Lisaa Page Should Be Open
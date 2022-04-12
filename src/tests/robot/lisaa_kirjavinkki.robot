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
    Page Should Contain  Sinuhe egyptiläinen

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

Lisaa Duplikaatti
    Add Kirjavinkki And Go To Home Page  Sinuhe egyptiläinen  Mika Waltari  1945  robotti

    Go To Lisaa Page
    Set Otsikko  Sinuhe egyptiläinen
    Set Kirjailija  Mika Waltari
    Set Kirjoitusvuosi  1945
    Lisaa Vinkki
    Lisaa Page Should Be Open
    Page Should Contain  Olet jo lisännyt kirjavinkin samalla otsikolla


*** Keywords ***
Set Otsikko
    [Arguments]  ${otsikko}
    Input Text  otsikko  ${otsikko}

Set Kirjailija
    [Arguments]  ${kirjailija}
    Input Text  kirjailija  ${kirjailija}

Set Kirjoitusvuosi
    [Arguments]  ${kirjoitusvuosi}
    Input Text  kirjoitusvuosi  ${kirjoitusvuosi}

Lisaa Vinkki
    Click Button  luo vinkki

Reset Database And Create User And Log In And Go To Lisaa Page
    Reset Application
    Create User And Log In  robotti  robotti123
    Click Link  Luo uusi vinkki
    Lisaa Page Should Be Open
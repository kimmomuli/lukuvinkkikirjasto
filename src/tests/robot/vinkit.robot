*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Database And Create User And Log In And Add Kirjavinkki And Go To Home Page


*** Test Cases ***
Poista itse lisatty vinkki
    Page Should Contain  Sinuhe egyptiläinen
    Click Button  Poista
    Page Should Not Contain  Sinuhe egyptiläinen

Toisen Lisaamaassa Vinkissa Ei Nay Poista Nappia
    Page Should Contain  Sinuhe egyptiläinen
    Page Should Contain Button  Poista
    Log Out
    Create User And Log In  robotti2  robotti234
    Page Should Contain  Sinuhe egyptiläinen
    Page Should Not Contain Button  Poista


*** Keywords ***
Log Out
    Click Link  Kirjaudu ulos

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

Reset Database And Create User And Log In And Add Kirjavinkki And Go To Home Page
    Reset Application
    Create User And Log In  robotti  robotti123
    Add Kirjavinkki And Go To Home Page  Sinuhe egyptiläinen  Mika Waltari  1945  robotti
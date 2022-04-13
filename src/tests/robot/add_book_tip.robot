*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Database, Create User, Log In And Go To New Tip Page


*** Test Cases ***
Add Book Tip With Valid Inputs
    Set Title  Sinuhe egyptiläinen
    Set Author  Mika Waltari
    Set Year  1945
    Submit Book Tip
    Home Page Should Be Open
    Page Should Contain Book Tip  Sinuhe egyptiläinen  Mika Waltari  1945  robotti

Add Book Tip With Too Short Title
    Set Title  S
    Set Author  Mika Waltari
    Set Year  1945
    Submit Book Tip
    New Tip Page Should Be Open
    Page Should Contain  Otsikon tulee sisältää ainakin kaksi merkkiä

Add Book Tip With Too Short Author Name
    Set Title  Sinuhe egyptiläinen
    Set Author  M
    Set Year  1945
    Submit Book Tip
    New Tip Page Should Be Open
    Page Should Contain  Kirjailijan nimen tulee sisältää ainakin kaksi merkkiä

Add Book Tip With Too Small Year
    Set Title  Sinuhe egyptiläinen
    Set Author  Mika Waltari
    Set Year  0
    Submit Book Tip
    New Tip Page Should Be Open
    Page Should Contain  Kirjoitusvuoden pitää olla kokonaisluku väliltä 1-2025

Add Book Tip With Too Large Year
    Set Title  Sinuhe egyptiläinen
    Set Author  Mika Waltari
    Set Year  2026
    Submit Book Tip
    New Tip Page Should Be Open
    Page Should Contain  Kirjoitusvuoden pitää olla kokonaisluku väliltä 1-2025

Add Duplicate Book Tip
    Add Book Tip And Go To Home Page  Sinuhe egyptiläinen  Mika Waltari  1945  robotti

    Go To New Tip Page
    Set Title  Sinuhe egyptiläinen
    Set Author  Mika Waltari
    Set Year  1945
    Submit Book Tip
    New Tip Page Should Be Open
    Page Should Contain  Olet jo lisännyt kirjavinkin samalla otsikolla


*** Keywords ***
Set Title
    [Arguments]  ${otsikko}
    Input Text  title  ${otsikko}

Set Author
    [Arguments]  ${kirjailija}
    Input Text  author  ${kirjailija}

Set Year
    [Arguments]  ${kirjoitusvuosi}
    Input Text  year  ${kirjoitusvuosi}

Submit Book Tip
    Click Button  luo vinkki

Reset Database, Create User, Log In And Go To New Tip Page
    Reset Application And Delete Cookies
    Create User And Log In  robotti  robotti123
    Click Link  Luo uusi vinkki
    New Tip Page Should Be Open
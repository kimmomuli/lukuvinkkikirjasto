*** Settings ***
Library  SeleniumLibrary
Library  ./AppLibrary.py


*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${NEW_TIP_URL}  http://${SERVER}/new_tip
${REGISTER_URL}  http://${SERVER}/register
${LOGIN_URL}  http://${SERVER}/login

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}


Home Page Should Be Open
    Title Should Be  Lukuvinkkisovellus - Lukuvinkit

Register Page Should Be Open
    Title Should Be  Lukuvinkkisovellus - Rekisteröidy

Login Page Should Be Open
    Title Should Be  Lukuvinkkisovellus - Kirjaudu sisään

New Tip Page Should Be Open
    Title Should Be  Lukuvinkkisovellus - Luo lukuvinkki

Go To Home Page
    Go To  ${HOME URL}

Go To Register Page
    Go To  ${REGISTER_URL}

Go To Login Page
    Go To  ${LOGIN_URL}

Go To New Tip Page
    Go To  ${NEW_TIP_URL}


Reset Application And Delete Cookies
    Reset Application
    Delete All Cookies

Page Should Contain Book Tip
    [Arguments]  ${title}  ${author}  ${year}  ${adder_username}
    Page Should Contain  ${title}
    Page Should Contain  ${author}
    Page Should Contain  ${year}
    Page Should Contain  ${adder_username}

Create User And Log In
    [Arguments]  ${username}  ${password}
    Create User  ${username}  ${password}
    Go To Login Page
    Login Page Should Be Open
    Input Text  username  ${username}
    Input Text  password  ${password}
    Click Button  Kirjaudu
    Home Page Should Be Open

Add Book Tip And Go To Home Page
    [Arguments]  ${title}  ${author}  ${year}  ${adder_username}
    Add Book Tip  ${title}  ${author}  ${year}  ${adder_username}
    Go To Home Page
    Home Page Should Be Open
    Page Should Contain Book Tip  ${title}  ${author}  ${year}  ${adder_username}
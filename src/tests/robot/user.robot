*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Database And Open Register Page


*** Test Cases ***
Register And Log In
    Set Username  robot
    Set Password  robot123
    Submit Register Credentials
    Home Page Should Be Open
    Log Out
    Go To Login Page
    Login Page Should Be Open
    Set Username  robot
    Set Password  robot123
    Submit Login Credentials
    Home Page Should Be Open

Register With Existing Username 
    Create User  robot  robot123
    Set Username  robot
    Set Password  robot123
    Submit Register Credentials
    Register Page Should Be Open
    Page Should contain  Käyttäjätunnus on jo olemassa

Register With Too Short Username
    Set Username  rob
    Set Password  robot123
    Submit Register Credentials
    Register Page Should Be Open
    Page Should contain  Kayttäjätunnuksen on oltava vähintään 4 merkkiä pitkä

Register With Too Short Password
    Set Username  robot
    Set Password  robot
    Submit Register Credentials
    Register Page Should Be Open
    Page Should contain  Salasanan on oltava vähintään 6 merkkiä pitkä

Log In With Wrong Username
    Create User  robot  robot123
    Go To Login Page
    Login Page Should Be Open
    Set Username  wrong_username
    Set Password  robot123
    Submit Login Credentials
    Login Page Should Be Open
    Page Should contain  Väärä käyttäjätunnus tai salasana

Log In With Wrong Password
    Create User  robot  robot123
    Go To Login Page
    Login Page Should Be Open
    Set Username  robot
    Set Password  robot12
    Submit Login Credentials
    Login Page Should Be Open
    Page Should contain  Väärä käyttäjätunnus tai salasana

Create New Tip Link Is Not Visible If Not Logged In
    Go To Home Page
    Page Should Not Contain  Luo Uusi Vinkki

Create New Tip Link Is Visible If Logged In
    Create User And Log In  robot  robot123
    Page Should Contain  Luo uusi vinkki

Open New Tip Page When Not Logged In
    Go To New Tip Page
    Login Page Should Be Open
    Page Should Contain  Sinun pitää olla kirjautuneena jotta voit lisätä uuden vinkin

*** Keywords ***
Log Out
    Click Link  Kirjaudu ulos

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Submit Login Credentials
    Click Button  Kirjaudu

Submit Register Credentials
    Click Button  Rekisteröidy

Reset Database And Open Register Page
    Reset Application And Delete Cookies
    Go To Register Page
    Register Page Should Be Open
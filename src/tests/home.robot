*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

***Test Cases ***
Click Lisaa Link
    Click Link  Luo uusi vinkki
    Lisaa Page Should Be Open

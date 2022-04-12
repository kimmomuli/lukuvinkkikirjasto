*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

***Test Cases ***
Click Kirjaudu Link
    Click Link  Kirjaudu
    Kirjautuminen Page Should Be Open

*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Database, Create User, Log In, Add Book Tip And Go To Home Page


*** Test Cases ***
Like Self Added Tip
    Page Should Contain Book Tip  Sinuhe egyptiläinen  Mika Waltari  1945  robot
    Click Button  Tykkää
    Page Should Not Contain Button  Tykkää

Dislike Self Added Tip
    Like Tip
    Click Button  En tykkää
    Page Should Not Contain Button  En tykkää

Like Other Users Tip
    Log Out
    Create User And Log In  third_robot  third_robot123
    Page Should Contain Button  Tykkää
    Click Button  Tykkää
    Page Should Not Contain Button  Tykkää

Delete Self Added Tip
    Page Should Contain Book Tip  Sinuhe egyptiläinen  Mika Waltari  1945  robot
    Click Button  Poista
    Page Should Not Contain  Sinuhe egyptiläinen

There Is No Delete Button On A Tip Added By Another User
    Page Should Contain Book Tip  Sinuhe egyptiläinen  Mika Waltari  1945  robot
    Page Should Contain Button  Poista
    Log Out
    Create User And Log In  other_robot  other_robot123
    Page Should Contain Book Tip  Sinuhe egyptiläinen  Mika Waltari  1945  robot
    Page Should Not Contain Button  Poista

*** Keywords ***
Log Out
    Click Link  Kirjaudu ulos

Like Tip
    Click Button  Tykkää

Reset Database, Create User, Log In, Add Book Tip And Go To Home Page
    Reset Application And Delete Cookies
    Create User And Log In  robot  robot123
    Add Book Tip And Go To Home Page  Sinuhe egyptiläinen  Mika Waltari  1945  robot
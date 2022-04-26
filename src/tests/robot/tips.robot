*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Database, Create User, Log In, Add Book Tip And Go To Home Page


*** Test Cases ***
Like Self Added Tip
    Click Button  Tykkää
    Page Should Contain Likes  1

Dislike Self Added Tip
    Like Tip
    Click Button  En tykkää
    Page Should Contain Likes  0

Like Tip Made By Other User
    Click Button  Tykkää
    Log Out
    Create User And Log In  third_robot  third_robot123
    Page Should Contain Button  Tykkää
    Click Button  Tykkää
    Page Should Contain Likes  2

There Is No Like Button If Not Logged In
    Log Out
    Go To Home Page
    Page Should Not Contain Button  Tykkää
    Page Should Not Contain Button  En tykkää

Delete Self Added Tip
    Click Button  Poista
    Page Should Not Contain  Sinuhe egyptiläinen

There Is No Delete Button On A Tip Added By Another User
    Page Should Contain Button  Poista
    Log Out
    Create User And Log In  other_robot  other_robot123
    Page Should Contain Book Tip  Sinuhe egyptiläinen  Mika Waltari  1945  robot
    Page Should Not Contain Button  Poista

Tips Are Sorted By Likes By Default
    Like Tip
    Add Book Tip And Go To Home Page  Binary alphabet  RobotAuthor  1970  robot
    Table Cell Should Contain  id:tip_0  1  2  Mika Waltari

Sort Tips By Time
    Like Tip
    Add Book Tip And Go To Home Page  Binary alphabet  RobotAuthor  1970  robot
    
    Click Button  id:menubutton
    Click Link  Aikaleiman mukaan
    Table Cell Should Contain  id:tip_0  1  2  RobotAuthor

Sort Tips By Likes
    Like Tip
    Add Book Tip And Go To Home Page  Binary alphabet  RobotAuthor  1970  robot
    
    Click Button  id:menubutton
    Click Link  Aikaleiman mukaan
    Click Button  id:menubutton
    Click Link  Tykkäyksien mukaan
    Table Cell Should Contain  id:tip_0  1  2  Mika Waltari


*** Keywords ***
Log Out
    Click Link  Kirjaudu ulos

Like Tip
    Click Button  Tykkää

Reset Database, Create User, Log In, Add Book Tip And Go To Home Page
    Reset Application And Delete Cookies
    Create User And Log In  robot  robot123
    Add Book Tip And Go To Home Page  Sinuhe egyptiläinen  Mika Waltari  1945  robot
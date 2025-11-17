*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  vapaa
    Set Password  salasana123
    Confirm Password  salasana123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  salasana123
    Confirm Password  salasana123
    Click Button  Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  vapaa
    Set Password  abcd123
    Confirm Password  abcd123
    Click Button  Register
    Register Should Fail With Message  Your password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  vapaa
    Set Password  salasana
    Confirm Password  salasana
    Click Button  Register
    Register Should Fail With Message  Your password must include numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  vapaa
    Set Password  salasana123
    Confirm Password  vaarin123
    Click Button  Register
    Register Should Fail With Message  The entered passwords don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  salasana123
    Confirm Password  salasana123
    Click Button  Register
    Register Should Fail With Message  Username kalle is already taken

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
*** Settings ***
Library     SeleniumLibrary    


*** Variables ***
${browser}    firefox
${url}    https://www.saucedemo.com/

*** Test Cases ***
test login
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Login_test
    Close Browser


*** Keywords ***
Login_test
    
    Wait Until Element Is Visible    id=user-name
    Input Text    id=user-name    standard_user
    Input Text    id=password    secret_sauce
    Click Button    id=login-button
    Click Element    id=add-to-cart-sauce-labs-backpack
    Click Button    id=add-to-cart-sauce-labs-onesie
    Click Element    xpath://*[@id="shopping_cart_container"]/a
    Click Element    id=remove-sauce-labs-backpack
    Click Button    id=checkout
    Input Text    id=first-name    divi
    Input Text    id=last-name    kumar
    Input Text    id=postal-code    636202
    Click Button    id=continue
    Click Button    id=finish
    Sleep    5s



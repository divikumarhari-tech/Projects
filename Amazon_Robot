*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}    firefox
${url}        https://www.amazon.in/

*** Test Cases ***
test login
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Shopping
    # Close Browser

*** Keywords ***
Shopping
    Wait Until Element Is Visible    class:nav-a nav-a-2   nav-progressive-attribute
    Click Element    class:nav-a nav-a-2   nav-progressive-attribute
    Wait Until Element Is Visible    id=ap_email_login   10s
    Input Text    id=ap_email_login    divikumarhari@gmail.com
    Click Button    xpath://*[@id="continue"]/span/input
    Wait Until Element Is Visible    id=ap_password    10s
    Input Text    id=ap_password    Amazon007@
    Click Button    id=signInSubmit
    Wait Until Element Is Visible    id=auth-mfa-otpcode
    Sleep    15s 
    Click Button    id=auth-signin-button
    Sleep    5s
    Input Text    xpath://*[@id="twotabsearchtextbox"]    Samsung mobile
    Click Element    xpath://*[@id="nav-search-submit-button"]
    Wait Until Element Is Visible    xpath://html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[10]/div/div/span/div/div/div/div[1]/div/div[2]/div/span/a/div/img
    Sleep    2s
    Click Element    xpath:///html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[10]/div/div/span/div/div/div/div[2]/div/div/div[1]/a/h2/span
    Switch Window
    Sleep    5s
    Click Button    id=add-to-cart-button
    Sleep    2s
    Click Button    href=/cart?ref_=ox_ewc_ret_gtc_dsk_in
    Sleep    5s
    Click Button    id=sc-buy-box-ptc-button
    Sleep    3s



    

    

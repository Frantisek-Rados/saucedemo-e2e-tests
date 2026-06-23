*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}         https://www.saucedemo.com/
${USER}        standard_user
${PASSWORD}    secret_sauce

*** Test Cases ***
Prihlasenie na SauceDemo
    Open Browser    ${URL}    chrome
    Input Text    id=user-name    ${USER}
    Input Text    id=password    ${PASSWORD}
    Click Button    id=login-button
    Wait Until Page Contains    Products
    Close Browser
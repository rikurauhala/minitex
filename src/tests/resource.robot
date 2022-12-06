*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input New Reference Command
    Input  n

Input New Reference
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}
    Input  ${author}
    Input  q
    Input  ${title}
    Input  ${year}
    Input  ${publisher}
    Run Application

    

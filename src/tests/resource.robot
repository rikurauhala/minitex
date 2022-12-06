*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input New Reference Command
    Input  n

Input New Reference
    [Arguments]  ${author}  ${title}  ${year}  ${publisher}
    Input  ${author}
    Input Quit Command
    Input  ${title}
    Input  ${year}
    Input  ${publisher}
    Input Quit Command
    Run Application

Input Quit Command
    Input  q
    

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

Input Quit Command
    Input  q

Input Print Command
    Input  s

Input Export Command
    Input  e

Delete Reference Of Index
    [Arguments]  ${index}
    Input  d
    Input Integer  ${index}

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

Input Edit Reference Command
    Input  u

Input Edit Author Command
    Input Integer  1

Choose Reference Index To Edit
    [Arguments]  ${index}
    Input Integer  ${index}

Input Edited Reference Field
    [Arguments]  ${string}
    Input  ${string}
    Input  q

Delete Reference Of Index
    [Arguments]  ${index}
    Input  d
    Input Integer  ${index}

Input New Doi Command
    Input  o

Input Doi
    [Arguments]  ${doi}
    Input  ${doi}
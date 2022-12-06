*** Settings ***
Resource  resource.robot
Test Setup  Clear Database

*** Test Cases ***
Create New Reference
    Input New Reference Command
    Input New Reference  Philip Pullman  Kultainen Kompassi  1996  Tammi
    Output Should Contain  Added a new reference.

Print References
Store Reference In Database
Export Reference To Bibtex File
Delete Reference

*** Keywords ***
Clear Database
    Clear Database
    

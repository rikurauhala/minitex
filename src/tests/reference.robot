*** Settings ***
Resource  resource.robot

*** Test Cases ***
Create New Reference
    Input New Reference Command
    Input New Reference  Philip Pullman  Kultainen Kompassi  1996  Tammi
    Output Should Contain  Added a new reference.
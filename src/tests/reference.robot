*** Settings ***
Resource  resource.robot
Test Setup  Clear Database

*** Test Cases ***
Create New Reference
    Input New Reference Command
    Input New Reference  Philip Pullman  Kultainen Kompassi  1996  Tammi
    Input Quit Command
    Run Application
    Output Should Contain  Added a new reference.

Print References
    Input New Reference Command
    Input New Reference  Philip Pullman  Kultainen Kompassi  1996  Tammi
    Input Print Command
    Input Quit Command
    Run Application
    Output Should Contain  1: Philip Pullman | Kultainen Kompassi | Tammi (1996)

Store References In Database
    Input New Reference Command
    Input New Reference  Philip Pullman  Kultainen Kompassi  1996  Tammi
    Input Quit Command
    Run Application
    Input New Reference Command
    Input New Reference  George R. R. Martin  Tuf Voyaging  2003  Meisha Merlin
    Input Print Command
    Input Quit Command
    Run Application
    Output Should Contain  1: Philip Pullman | Kultainen Kompassi | Tammi (1996)
    Output Should Contain  2: George R. R. Martin | Tuf Voyaging | Meisha Merlin (2003)

Delete References In Database
    Input New Reference Command
    Input New Reference  Philip Pullman  Kultainen Kompassi  1996  Tammi
    Input New Reference Command
    Input New Reference  George R. R. Martin  Tuf Voyaging  2003  Meisha Merlin
    Delete Reference Of Index  2
    Input Print Command
    Input Quit Command
    Run Application
    Output Should Contain  1: Philip Pullman | Kultainen Kompassi | Tammi (1996)
    Output Should Not Contain  2: George R. R. Martin | Tuf Voyaging | Meisha Merlin (2003)

Export References Into Bibtex File
    Input New Reference Command
    Input New Reference  Philip Pullman  Kultainen Kompassi  1996  Tammi
    Input New Reference Command
    Input New Reference  George R. R. Martin  Tuf Voyaging  2003  Meisha Merlin
    Input Export Command
    Input Quit Command
    Run Application
    Export Message Should Contain  References exported succesfully to *your filepath*
    Format Database

*** Keywords ***
Clear Database
    Format Database
        
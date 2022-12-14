# User manual

This document contains the *user manual*, including instructions on how to download and run the application.

## Prerequisites

Python version 3.10 or higher is needed to run the application. You may use [pyenv](https://github.com/pyenv/pyenv) or similar tools to easily switch to the correct version. [Poetry](https://python-poetry.org/) should also be installed. The application has been mainly tested on machines running Linux but should work fine on other operating systems as long as the aforementioned software are properly installed.

## Installing

The application can be installed by running the following commands. You may use [alternative ways](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) such as cloning using HTTPS or the GitHub CLI. You may also download the [latest release](https://github.com/rikurauhala/minitex/releases).

```bash
# Get the source code
$ git clone git@github.com:rikurauhala/minitex.git

# Change directory
$ cd minitex

# Install dependencies
$ poetry install
```

## Running

The application can be started by running the `start` command. There is no need to initialize the database as it will be handled automatically after running the application for the first time.

```bash
# Run the application
$ poetry run invoke start
```

## Data storage

All application data is saved in the *data* directory. By default, the database file is named **database.db** but this can be changed by editing the value in the file `.env`. If left blank, the application will use the default value. There is no need to gitignore the .env file as it contains no secrets.

```bash
DATABASE_FILENAME="database.db"
```

## User interface

The application has a command-line user interface. The application can be used by typing commands in the terminal.

## Commands

Commands can be used to control the program. The following output is printed when the application is started. Commands can be typed after the `Input command: ` line.

```
Commands:
[ q ] quit
[ h ] print all the commands
[ n ] add a new reference
[ o ] add a new reference based on DOI
[ s ] show all references
[ e ] export the references to a BibTeX file
[ d ] delete a reference
[ u ] edit a reference
Input command: 
```

### Quit

The application can be terminated by entering the command `q` for *quit*.

### Print all the commands

Typing the command `h` for *help* will print a list of all available commands (see above).

### Add a new reference

A new reference can be added manually by typing `n` for *new reference*. The application will then ask for further details: an arbitrary number of *authors* in the format `last name, first name`. One or more authors can be given. After typing the desired number of author(s), the process can be continued by typing `q` in the terminal.

After inserting valid author(s), the application will ask for the *title* of the reference, the *year* of publication and lastly the *publisher*. The year should be a valid integer. Other fields should be strings. After succesfully adding a reference, the application will print `Added a new reference`. If something goes wrong or invalid input is given, an error message will be printed instead.

```
Input command: n
Input authors in format lastname, firstname (q to stop): Penttonen, Matti
Input authors in format lastname, firstname (q to stop): Meineche, Schmidt Erik 
Input authors in format lastname, firstname (q to stop): Goos, Gerhard
Input authors in format lastname, firstname (q to stop): q
Input title: Algorithm Theory - SWAT 2002 [...]
Input year published: 2002
Input publisher: Springer Berlin / Heidelberg
Added a new reference.
```

### Add a new reference based on DOI

Instead of filling in the information manually, a new reference can also be added by giving the [DOI](https://www.doi.org/) or the *Digital Object Identifier* of a reference. The application automatically fetches the information of the publication based on the DOI and adds it to the database. Adding a new reference this way can be done by using the command `o` for *D(O)I* and giving a valid identifier.

Inserting an invalid DOI will not work. The DOI also has to refer to a *book* as it is the only reference type supported by the application at the moment.

```
Input command: o
Insert a valid DOI (q to cancel): 10.1007/3-540-45471  
Invalid DOI, try again.
Insert a valid DOI (q to cancel): 10.1007/3-540-45471-3
Added a new reference.
```

### Show all references

The program remembers the references it has been given. The command `s` for *show* will print a list of all references in the database.

```
Input command: s
References: 
1: Matti Penttonen, Schmidt Erik Meineche and Gerhard Goos | Algorithm Theory - SWAT 2002 [...] | Springer Berlin / Heidelberg (2002)
2: Martti Penttonen and Erik Meineche Schmidt | Algorithm Theory — SWAT 2002 | Springer Berlin Heidelberg (2002)
```

### Export the references to a BibTeX file

All references can be exported into a file with the command `e` for export. The exported data can be found in the file `data/references.bib`. The exported data is in the [BibTeX](https://en.wikipedia.org/wiki/BibTeX) format.

```
Input command: e
References exported to ~/minitex/data/references.bib succesfully.
```

The exported data can be inspected or used in an actual application with BibTeX support.

```bash
user@machine:~/minitex$ cat data/references.bib 

@BOOK{PMG02,
    title = "Algorithm Theory - SWAT 2002 [...]",
    author = "Penttonen, Matti and Meineche, Schmidt Erik and Goos, Gerhard",
    publisher = "Springer Berlin / Heidelberg",
    year = "2002"
}
```

### Delete a reference

Existing references can also be deleted. The command `d` for *delete* will ask for an index of a reference to be deleted. It would be a good idea to list the references (and their indices) with the command `s` first.

```
Input command: s
References: 
1: Matti Penttonen, Schmidt Erik Meineche and Gerhard Goos | Algorithm Theory - SWAT 2002 [...] | Springer Berlin / Heidelberg (2002)
Input command: d
Enter the index of the reference you wish to delete: 1
Reference deleted.
Input command: s
References have not been added yet.
```

### Edit a reference

After adding new references, they can also be edited. The command for this is `u` which stands for... *I guess we ran out of free letters at this point*.

```
Input command: s
References: 
1: Martti Penttonen and Erik Meineche Schmidt | Algorithm Theory — SWAT 2002 | Springer Berlin Heidelberg (2002)
Input command: u
Enter the index of the reference you wish to edit: 1
[ 1 ] edit authors
[ 2 ] edit title
[ 3 ] edit year
[ 4 ] edit publisher
Input field to edit: 2
Enter a new value: Algorithm Theory
Reference edited.
Input command: s
References: 
1: Martti Penttonen and Erik Meineche Schmidt | Algorithm Theory | Springer Berlin Heidelberg (2002)
```

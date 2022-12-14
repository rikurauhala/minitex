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

## Configuration

All application data is saved in the *data* directory. By default, the database file is named **database.db** but this can be changed by editing the value in the file `.env`. If left blank, the application will use the default value. There is no need to gitignore the .env file as it contains no secrets.

```bash
DATABASE_FILENAME="database.db"
```

## User interface

The application has a command-line user interface. The application can be used by typing commands in the terminal.

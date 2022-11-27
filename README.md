# Minitex

Ohjelmistotuotanto-kurssin miniprojekti | Helsingin yliopisto | Syksy 2022

## Status

![Continuous Integration](https://github.com/rikurauhala/minitex/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/rikurauhala/minitex/branch/main/graph/badge.svg?token=MIVVZGAX67)](https://codecov.io/gh/rikurauhala/minitex)

## Instructions

### How to install

```bash
# Get the source code
$ git clone git@github.com:rikurauhala/minitex.git

# Change directory
$ cd minitex

# Install dependencies
$ poetry install
```

### How to run

```bash
# Run the application
$ poetry run python src/index.py

# Alternative way to run
$ poetry shell
$ python src/index.py
```

## Documentation

- [Product Backlog](https://docs.google.com/spreadsheets/d/e/2PACX-1vT0XfimtFOWroZy0wJ5NKa43JU2sddjG1ixwx4_bO4ShlPGQ1gfIO_tivunbP-bqmIWVCWoO5qOdBI6/pubhtml)
- [Continuous Integration](https://github.com/rikurauhala/minitex/blob/main/.github/workflows/main.yml)

## Definition of Done

Program is planned well. Code is written with python. Code tests are passed with 75% coverage. Program works as intended and user story tests are done and passed with Robot Framework. Code is documented. Continuous integration and delivery is used.

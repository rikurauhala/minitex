# Minitex

Minitex is a command-line application for managing academic references in the BibTeX format. Created for the software engineering course [Ohjelmistotuotanto](https://ohjelmistotuotanto-hy.github.io/) at the [University of Helsinki](https://www.helsinki.fi/en/faculty-science/faculty/computer-science) in autumn 2022.

Created by:
- [Ilari Haho](https://github.com/Fimen)
- [Isak Pulkki](https://github.com/isakpulkki)
- [Riku Rauhala](https://github.com/rikurauhala)
- [Henri Remonen](https://github.com/HRemonen)
- [Samppa Salo](https://github.com/Sam0ni)

## Status

![Continuous Integration](https://github.com/rikurauhala/minitex/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/rikurauhala/minitex/branch/main/graph/badge.svg?token=MIVVZGAX67)](https://codecov.io/gh/rikurauhala/minitex)

## Releases

- [v1.0.0](https://github.com/rikurauhala/minitex/releases/tag/v1.0.0)
- [Demo](https://github.com/rikurauhala/minitex/releases/tag/demo)
- [Sprint 2](https://github.com/rikurauhala/minitex/releases/tag/sprint2)

## Instructions

See the [user manual](docs/manual.md) for more information.

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
$ poetry run invoke start

# Alternative way to run
$ poetry shell
$ python src/index.py
```

### How to test

```bash
# Run unit tests 
$ poetry run invoke test

# Run user story tests
$ poetry run invoke robot
```

## Documentation

- [Product Backlog](https://docs.google.com/spreadsheets/d/e/2PACX-1vT0XfimtFOWroZy0wJ5NKa43JU2sddjG1ixwx4_bO4ShlPGQ1gfIO_tivunbP-bqmIWVCWoO5qOdBI6/pubhtml)
- [User Story tests with acceptance criteria](src/tests/reference.robot)
- [Continuous Integration](.github/workflows/main.yml)
- [Test Coverage Report](https://app.codecov.io/gh/rikurauhala/minitex)
- [User manual](docs/manual.md)
- [Architecture](docs/architecture.md)
- [Course Finish Report](docs/raportti.md)

## Definition of Done

Program is planned well. Code is written with Python. Code tests are passed with 75% coverage. Program works as intended and user story tests are done and passed with Robot Framework. Code is documented. Continuous integration and delivery is used.



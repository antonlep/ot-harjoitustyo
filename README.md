# pygame-breakout

## Documentation
[Requirements specification](https://github.com/antonlep/ot-harjoitustyo/blob/master/dokumentaatio/requirements_specification.md)

[Work hour record](https://github.com/antonlep/ot-harjoitustyo/blob/master/dokumentaatio/work_hours.md)

## Required software

- Python (>= 3.8)
- Poetry (>= 1.1.11)

## Installation

- Install dependencies:

`poetry install`

- Start the game:

`poetry run invoke start`

## List of commands

### Run the game

`poetry run invoke start`

### Run tests

`poetry run invoke test`

### Generate a test coverage report to htmlcov directory

`poetry run invoke coverage-report`

### Run pylint checks

`poetry run invoke lint`

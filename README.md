# pygame-breakout

## Documentation
[Requirements specification](https://github.com/antonlep/ot-harjoitustyo/blob/master/dokumentaatio/requirements_specification.md)

[Work hour record](https://github.com/antonlep/ot-harjoitustyo/blob/master/dokumentaatio/work_hours.md)

## Required software

- Python (>= 3.8)
- Poetry (>= 1.1.11)

## Installation

-Install dependencies:
`poetry install`

-Start the game:
'poetry run invoke start`

## List of commands

### Run the game

'''bash
poetry run invoke start
'''

### Run tests

'''bash
poetry run invoke test
'''

### Generate a test coverage report to htmlcov directory

'''bash
poetry run invoke coverage-report
'''

### Run pylint checks

'''bash
poetry run invoke lint
'''

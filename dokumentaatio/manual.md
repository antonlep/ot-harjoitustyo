# User manual

Download latest source code from [release](https://github.com/antonlep/ot-harjoitustyo/releases) from Assets/Source code. Unzip the folder to the disk and run all the commands in ot-harjoitustyo folder.

## Configuration

File names that are used for data storage are defined in .env file in the root folder.

## Installation

Install dependencies:

`poetry install`

Start the game:

`poetry run invoke start`

In Windows 10 and depending on python configuration it might be needed to run the following command to start the game

`poetry run python src/index.py`

## Keys

In main menu screen:

Left, right, up and down keys to navigate the options

Enter or space to select start a new game option

During playing:

N to start a new game

Space to launch the ball

Left and right key to move the paddle

## Instructions

Try to break all tile in the screen to move to the next level. Next level will have higher difficulty level, meaning the ball speed will be faster. You get one point for one destroyed tile.

In the beginning, you have three lives left. If the ball goes outside the game area, you lose one live. If lives go to zero, game is over and current points are saved to high score list if score is good enough.

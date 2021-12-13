# User manual

Download latest source code from [release](https://github.com/antonlep/ot-harjoitustyo/releases) from Assets/Source code.

## Configuration

File names that are used for data storage are defined in .env file in the root folder.

## Installation

Install dependencies

`poetry install`

Start the game

`poetry run invoke start`

## Keys

N to start a new game

Space to launch the ball

Left and right key to move the paddle

## Instructions

Try to break all tile in the screen to move to the next level. Next level will have higher difficulty level, meaning the ball speed will be faster. You get one point for one destroyed tile.

In the beginning, you have three lives left. If the ball goes outside the game area, you lose one live. If lives go to zero, game is over and current points are saved to high score list if score is good enough.

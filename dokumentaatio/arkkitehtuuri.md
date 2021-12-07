# Architecture

## Class diagram

![kaavio](https://user-images.githubusercontent.com/76871257/143781059-ea33a3d6-a537-41fa-ab24-dd74d334eb84.jpg)

## Sequence diagram
### User presses N to start a new game
![kaavio2](https://user-images.githubusercontent.com/76871257/145069517-b10af718-548a-443f-b019-c36abe461fd2.PNG)
First, GameLoop checks what keys have been pressed. When N key is pressed, GameLevel resets ball and paddle position, removes old tiles and creates new tiles. Ball is set up to lie on top of the paddle and finally the objects are rendered to the display.

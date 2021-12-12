# Architecture descripttion

## Structure
Program has hierarchical structure with three main levels: On top GameLoop 

![kaavio](https://user-images.githubusercontent.com/76871257/145709371-7f60b10c-c89a-4495-95e4-a56c6ee5d60a.PNG)

## Sequence diagram
### User presses N to start a new game
![kaavio2](https://user-images.githubusercontent.com/76871257/145069517-b10af718-548a-443f-b019-c36abe461fd2.PNG)
First, GameLoop checks what keys have been pressed. When N key is pressed, GameLevel resets ball and paddle position, removes old tiles and creates new tiles. Ball is set up to lie on top of the paddle and objects are rendered to the display.

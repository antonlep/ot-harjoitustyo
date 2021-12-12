# Architecture descripttion

## Main structure
Program has hierarchical structure with three main levels: On top level, GameLoop keeps track of current game state and takes care of interactions of classes below. On second level, GameLevel handles object interactions during gameplay, Renderer displays objects to the screen, EventQueue handles user generated input and Repository is resposible of data storage. On third level are simple game objects that GameLevel and Renderer use. 
![kaavio](https://user-images.githubusercontent.com/76871257/145709371-7f60b10c-c89a-4495-95e4-a56c6ee5d60a.PNG)

## UI

![cap2](https://user-images.githubusercontent.com/76871257/145710098-3a30dd83-f3e8-4139-ba6f-828e9bdc5f40.PNG)


## Game logic

## Data storage


## Sequence diagram
### User presses N to start a new game
![kaavio2](https://user-images.githubusercontent.com/76871257/145069517-b10af718-548a-443f-b019-c36abe461fd2.PNG)
First, GameLoop checks what keys have been pressed. When N key is pressed, GameLevel resets ball and paddle position, removes old tiles and creates new tiles. Ball is set up to lie on top of the paddle and objects are rendered to the display.

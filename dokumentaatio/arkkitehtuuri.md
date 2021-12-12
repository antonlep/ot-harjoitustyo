# Architecture descripttion

## Main structure
Program has hierarchical structure with three main levels: On top, GameLoop keeps track of the current game state and takes care of the interactions of classes below. On the second level, GameLevel handles object interactions during gameplay, Renderer displays objects to the screen, EventQueue handles user generated input and Repository is resposible for data storage. On the third level are simple game objects that GameLevel and Renderer use. 
![kaavio](https://user-images.githubusercontent.com/76871257/145709371-7f60b10c-c89a-4495-95e4-a56c6ee5d60a.PNG)

## UI
User interface is implemented using pygame library for object display and user input. EventQueue reads user input from keypresses, and Renderer displays objects to the screen using pygame Display object.  
![cap2](https://user-images.githubusercontent.com/76871257/145710098-3a30dd83-f3e8-4139-ba6f-828e9bdc5f40.PNG)

## Game logic
Game object positions and movements are handled inside GameLevel classs and objects below. Pygame library is used for modelling game objects and their interactions. Current game state, number of lives, number of points and current level are tracked inside GameLoop.
![cap3](https://user-images.githubusercontent.com/76871257/145710314-bcb37b73-7739-43b9-b305-bebad2e79092.PNG)

## Data storage
Repository takes care of data storage using SQLite database. Database name is defined in .env file that is located in application root folder.
![cap4](https://user-images.githubusercontent.com/76871257/145710447-6de2eead-714e-4b41-8c55-c88b3fcc2be4.PNG)


## Sequence diagram
### User presses N to start a new game
![kaavio2](https://user-images.githubusercontent.com/76871257/145069517-b10af718-548a-443f-b019-c36abe461fd2.PNG)
First, GameLoop checks what keys have been pressed. When N key is pressed, GameLevel resets ball and paddle position, removes old tiles and creates new tiles. Ball is set up to lie on top of the paddle and objects are rendered to the display.

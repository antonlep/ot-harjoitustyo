# Architecture descripttion

## Main structure
Program has hierarchical structure with three main levels: On top, GameLoop keeps track of the current game state and takes care of the interactions of classes below. On the second level, GameLevel handles game objects and their interactions, Renderer displays objects to the screen, EventQueue handles user generated input, MainMenu includes menu logic and Repository is resposible for data storage. On the third level are simple game objects that GameLevel and Renderer use. 
![kaavio](https://user-images.githubusercontent.com/76871257/147405485-0c727660-818b-479d-92f2-9d7e09c8d368.PNG)

## UI
User interface is implemented using pygame library for object display and user input. EventQueue reads user input from keypresses, and Renderer displays objects to the screen using pygame Display object.  
![cap2](https://user-images.githubusercontent.com/76871257/145710098-3a30dd83-f3e8-4139-ba6f-828e9bdc5f40.PNG)

## Game logic
Game object positions and movements are handled inside GameLevel classs and objects below. Pygame library is used for modelling game objects and their interactions. Current game state, number of lives, number of points and current level are tracked inside GameLoop.
![cap3](https://user-images.githubusercontent.com/76871257/145710314-bcb37b73-7739-43b9-b305-bebad2e79092.PNG)

## Game logic
MainMenu class includes logic for what are menu options, and how they are changed.
![menu](https://user-images.githubusercontent.com/76871257/147405589-8cadaca8-963d-4496-a7e2-f29a097e9d82.PNG)

## Data storage
Repository takes care of data storage using SQLite database. Database name is defined in .env file that is located in application root folder.
![cap4](https://user-images.githubusercontent.com/76871257/145710447-6de2eead-714e-4b41-8c55-c88b3fcc2be4.PNG)

## Main functionalities

### Example of a game loop, where right key is pressed and ball hits one tile
First, GameLoop gets information of keypress from EventQueue. Then it calls GameLevel to update object positions, mainly to move ball to next position and paddle to the right. After objects have been moved, collisions between paddle, ball and tiles are checked. In this example there was tile collision, so GameLevel calls Tile kill method to remove the tile from the game area. Next, there is a check if all tiles have been removed or if the ball has gone outside the game area. Top score is taken from Repository, and game objects and game state information is sent to Renderer. Renderer calls Display methods to display objects to the screen. Finally clock is advanced, and in the next stage the loop would start all over again. 
![Capture](https://user-images.githubusercontent.com/76871257/145853516-9f685755-8209-4168-85ec-8d325e07bee7.PNG)

### User presses N to start a new game
First, GameLoop checks what keys have been pressed. When N key is pressed, GameLevel resets ball and paddle position, removes old tiles and creates new tiles. Ball is set up to lie on top of the paddle and objects are rendered to the display. Finally clock is advanced.
![class3](https://user-images.githubusercontent.com/76871257/147406350-ac7befc8-caa9-4107-8509-d688a6e77db1.PNG)


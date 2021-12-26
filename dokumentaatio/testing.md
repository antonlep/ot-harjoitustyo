# Test document

Program has been tested by making unit tests for smaller components and integration tests for larger functionalities, especially for GameLoop class. Tests have been made automatically with unittest. In addition manual tests have been done to validate large scale system functionality.

## Unit testing and integration testing

### UI

UI is somewhat tested by testing EventQueue class with EventQueueTest class in simple cases. Renderer class is not tested with unit tests.

### Game logic

Game objects and their interactions are tested with PaddleTest and TestGameLevel classes. Cases that the ball moves correctly, don't go through walls and hits the paddle and walls in correct way are gone through. Game logic is tested with TestGameLoop class where Renderer, Repository and EventQueue are mock components, but the real classes are used for game logic components GameLevel, Ball, Paddle and Tiles. Different game states are tested there to assess correct integrated behavior.

### Repository

Repository is tested with TestRepository class. Test database is stored in memory by using sqlite :memory option, so no additional test databases are created to the disk. Repository methods are tested with unit tests.

### Test coverage

Test branch coverage is 84% when not including UI class Renderer.

![coverage](https://user-images.githubusercontent.com/76871257/147408495-a5e39ebe-3c37-48dd-8859-1bbe90dce5c6.PNG)

## System testing

System testing has been done manually. Proram has been installed and functionalities listed in requirement document have been tested in Linux and in Windows 10 machines. Different database configurations have been tested by modifying .env file. Cases where database doesn't exist or already exists have been gone through.

## Remaining quality issues

In some cases game over screen is displayed when user exits the software by pressing (x) during game play, so the game is not immediately closed.

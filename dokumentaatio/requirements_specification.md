# Requirements specification
## Purpose
A game, where the goal is to knock down rows of bricks with a ball, using a movable paddle to hit the ball. 
## User interface
### Three main views:
- Start screen with buttons for a new game, for changing color, for a difficulty level and for exiting the game
- Gameplay view
  - Moving paddle on the bottom
  - Eight rows of bricks on the top
  - Current score display
  - Highest previous score display
  - Difficulty level display
  - Number of balls left
- High score list with points
## Basic functionalities
- [x] During gameplay, user can move the paddle left and right
- [x] User can hit the ball with paddle
- [x] User can break tiles with ball
- [x] User gets points by breaking tiles
- [x] User can start a new game
- [x] When user misses the ball three times, game is over
- [x] After user has cleared all the bricks from the game area, the next level starts with higher difficulty
- [x] High score list is displayed after game over
- [x] Highest scores are added to high score list
- [ ] User can insert name to high score list
- [ ] User can display high score list
- [x] User can change the game difficulty level which controls the ball speed
- [x] Option to change colors 

## Further development ideas
- Multiple levels with different brick layouts
- Some bricks would require multiple hits to break
- Possibility to pause the game
- Special bonuses: multiple balls, widening or shortening the paddle, temporarily speeding up the ball, reversing the controls

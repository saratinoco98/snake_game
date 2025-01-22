# 🐍 Python Snake Game

A classic Snake Game implementation using Python's Turtle graphics library. Control a snake as it moves around the screen, eat food to grow longer, and try to achieve the highest score without hitting the walls or yourself!

## 🎮 Game Features

- Smooth snake movement with arrow key controls
- Score tracking system
- Food spawning mechanics
- Collision detection (walls and self)
- Game over screen
- Clean and modular code structure

## 🛠️ Prerequisites

Before running the game, make sure you have:
- Python 3.x installed on your system
- Turtle graphics library (comes with Python standard library)

## 🎯 How to Play

1. Run the main game file:
```bash
python main.py
```

2. Use the arrow keys to control the snake:
   - ⬆️ Up Arrow: Move Up
   - ⬇️ Down Arrow: Move Down
   - ⬅️ Left Arrow: Move Left
   - ➡️ Right Arrow: Move Right

3. Try to eat the food to grow longer and increase your score
4. Avoid hitting the walls or the snake's own body
5. Click anywhere on the screen to exit when game is over

## 🏗️ Project Structure

```
snake-game/
│
├── main.py          # Main game loop and setup
├── snake.py         # Snake class and movement logic
├── food.py          # Food class and spawning mechanics
└── scoreboard.py    # Score tracking and display
```

## 🎨 Game Controls

- **Arrow Keys**: Control snake direction
- **Click**: Exit game (when game is over)

## 🎯 Game Rules

1. The snake starts with a length of 3 segments
2. Each food item eaten:
   - Increases score by 1 point
   - Makes the snake longer
   - Spawns new food at random location
3. Game ends if the snake:
   - Hits the wall
   - Collides with itself

## 🔧 Technical Details

- Window Size: 600x600 pixels
- Movement Speed: 0.09 second delay
- Written in Python using OOP principles
- Uses Turtle graphics for display

## 🚀 Future Enhancements

- [ ] High score system
- [ ] Multiple difficulty levels
- [ ] Power-ups
- [ ] Sound effects
- [ ] Start menu
- [ ] Pause functionality
- [ ] Custom snake skins



## 👥 Author

Sara Tinoco

## 🙏 Acknowledgments
- Course: 100 Days of Code: The Complete Python Pro Bootcamp
- Dr. Angela Yu
- Inspired by the classic Snake game
- Built using Python's Turtle graphics library

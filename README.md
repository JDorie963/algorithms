# Tic Tac Toe with PyQt5

A graphical Tic Tac Toe game built with Python and PyQt5, featuring a user-friendly interface and a computer opponent powered by the minimax algorithm for optimal gameplay.

---

## Features

- **Welcome Screen**: A starting page with options to begin the game or exit the application.
- **Game Board**: A 3x3 interactive board with clear visuals.
- **Single Player**: Play against an AI opponent powered by the minimax algorithm.
- **Dynamic Turns**: The game alternates between player X and AI O.
- **Win Detection**: Recognizes winning combinations or draws and displays the result.
- **Play Again or Exit**: Prompts the player to restart or return to the main menu after the game ends.

---

## Installation

Follow these steps to set up the project:

### Prerequisites
- Python 3.7+
- PyQt5

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/JDorie963/algorithms.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tic-tac-toe-pyqt5
   ```
3. Install required dependencies:
   ```bash
   pip install PyQt5
   ```
4. Run the application:
   ```bash
   python main.py
   ```

---

## How to Play

1. Launch the application using `python main.py`.
2. From the welcome screen, click "Start Game" to begin.
3. Player X (you) always starts.
4. Click on an empty square to make your move.
5. The AI (Player O) will respond with its move.
6. The game ends when there is a winner or the board is full (a draw).
7. After the game, a prompt will appear to either replay or return to the main menu.

---

## Project Structure

```plaintext
├── main.py         # Entry point of the application
├── game_page.py    # Core logic and GUI for the game
```

### File Descriptions
- **`main.py`**: Initializes the application and launches the welcome page.
- **`game_page.py`**: Contains the game logic, including the welcome page, gameplay mechanics, AI implementation, and UI design.

---

## Screenshots

### Welcome Screen
The starting screen with options to begin the game or exit:
![Welcome Screen](https://via.placeholder.com/400x300.png?text=Welcome+Screen)

### Gameplay
A 3x3 grid where Player X and AI O take turns:
![Game Board](https://via.placeholder.com/400x300.png?text=Game+Board)

---

## AI Logic
The AI opponent uses the **Minimax algorithm** to evaluate optimal moves:

- **Maximizing Player**: AI (Player O) tries to maximize its score.
- **Minimizing Player**: Human (Player X) tries to minimize the AI's score.
- **Recursive Backtracking**: Explores all possible game states to find the optimal move.

---

## Future Improvements
- Add multiplayer functionality for two human players.
- Enhance the UI with animations and sound effects.
- Implement difficulty levels for the AI.
- Add a score tracking system.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- PyQt5 Documentation: [https://www.riverbankcomputing.com/software/pyqt/intro](https://www.riverbankcomputing.com/software/pyqt/intro)
- Minimax Algorithm: [Wikipedia](https://en.wikipedia.org/wiki/Minimax)

---

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork this repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

Enjoy playing Tic Tac Toe! 🎮


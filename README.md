# Tic-Tac-Toe with AI

This project implements a classic Tic-Tac-Toe game in C with a built-in AI opponent that uses the Minimax algorithm for optimal gameplay. Players can challenge the AI or test their skills in this simple yet intelligent implementation.

## Features
- **Player vs AI**: Play against an AI opponent that uses the Minimax algorithm to determine the best possible move.
- **Intelligent AI**: The AI evaluates all possible moves to ensure optimal performance.
- **Interactive Gameplay**: The game allows the user to input their moves through the terminal.
- **Simple and Clean Code**: Easy-to-read C code that demonstrates fundamental concepts like arrays, recursion, and game logic.

## How It Works
- The game board is a 3x3 grid, displayed in the terminal.
- Players take turns (Player X and AI O) placing their marks on the board.
- The AI calculates the best move at each turn using the Minimax algorithm.
- The game ends when:
  - A player wins by getting 3 marks in a row, column, or diagonal.
  - The board is full, resulting in a draw.

## Prerequisites
To compile and run this program, you need:
- A C compiler (e.g., GCC).
- A terminal or command-line interface.

## Compilation and Execution
1. Clone the repository or copy the code into a file named `main.c`.
2. Open a terminal and navigate to the directory containing `main.c`.
3. Compile the program using GCC:
   ```bash
   gcc main.c -o tic_tac_toe
   ```
4. Run the compiled program:
   ```bash
   ./tic_tac_toe
   ```

## Gameplay Instructions
1. Start the game by running the program.
2. The board is displayed as a 3x3 grid with rows and columns numbered 1 to 3.
3. Player X goes first:
   - Enter the row and column numbers (e.g., `1 2` to place an X in the first row, second column).
   - If the input is invalid or the cell is already occupied, the program will prompt you to try again.
4. The AI (Player O) will make its move automatically.
5. The game continues until there is a winner or a draw.

## Example Output
```
Welcome to Tic-Tac-Toe!
   |   |   
---|---|---
   |   |   
---|---|---
   |   |   

Player X's Turn: Enter row (1-3) and column (1-3): 1 1
 X |   |   
---|---|---
   |   |   
---|---|---
   |   |   

AI's Turn:
 X |   |   
---|---|---
   | O |   
---|---|---
   |   |   
```

## Code Highlights
- **Minimax Algorithm**: The AI uses this algorithm to evaluate all possible moves recursively, aiming to maximize its score and minimize the player's score.
- **Dynamic Memory Allocation**: The `find_best_move` function allocates memory to store the AI's best move.
- **Modular Functions**: The code is organized into reusable functions for better readability and maintainability.

## File Structure
- `main.c`: Contains the entire implementation of the Tic-Tac-Toe game.

## Future Improvements
- Add support for Player vs Player mode.
- Implement a graphical user interface (GUI) for better visualization.
- Enhance AI difficulty levels to allow for easier or more challenging gameplay.

## License
This project is open source and available under the [MIT License](LICENSE).

## Contributions
Contributions are welcome! Feel free to open an issue or submit a pull request to improve the code or add new features.

## Acknowledgments
Special thanks to the developers of the Minimax algorithm for inspiring the AI logic in this project.

---
Enjoy the game and have fun challenging the AI!


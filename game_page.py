from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QMessageBox


class WelcomePage(QMainWindow):
    """
    WelcomePage class displays the initial welcome screen with options to
    start the game or exit the application.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe - Welcome")
        self.setGeometry(100, 100, 400, 300)

        # Central widget and layout setup
        self.central_widget = QWidget() # main container
        self.setCentralWidget(self.central_widget)
        ''' vertical layout manager. will arrange
         UI elements one below the other in a column.'''
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Welcome Label
        self.welcome_label = QLabel("Welcome to Tic Tac Toe!", self)
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setFont(QFont("Arial", 15, QFont.Bold))
        self.layout.addWidget(self.welcome_label)

        # Buttons to start the game or exit
        self.start_button = QPushButton("Start Game", self)
        self.start_button.setFont(QFont("Arial", 14))
        self.start_button.clicked.connect(self.start_game)
        self.layout.addWidget(self.start_button)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setFont(QFont("Arial", 14))
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

    def start_game(self):
        """
        Starts the game by opening the GamePage and closing the WelcomePage.
        """
        self.game_page = GamePage()
        self.game_page.show()
        self.close()


class GamePage(QMainWindow):
    """
    GamePage class manages the gameplay, including player turns,
    AI logic, and checking for win or draw conditions.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 800, 800)

        # Central widget and layout setup
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Initialize game variables
        self.current_player = "X"  # X always starts
        self.board = ["" for _ in range(9)]

        # Info Label to display player turns or game messages
        self.info_label = QLabel("Player X's Turn", self)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.layout.addWidget(self.info_label)

        # Game Board with a 3x3 grid of buttons
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(10) # 10 pixels spacing between grid cells

        self.buttons = []

        for i in range(9):
            button = QPushButton("", self)
            button.setFont(QFont("Arial", 36, QFont.Bold))
            button.setStyleSheet("background-color: #ADD8E6; border: 2px solid #000;") # light blue
            button.setFixedSize(200, 200)

            # Connect button to the make_move function
            button.clicked.connect(lambda _, index=i: self.make_move(index))
            self.grid_layout.addWidget(button, i // 3, i % 3)
            self.buttons.append(button)

        self.layout.addLayout(self.grid_layout)

    def make_move(self, index):
        """
        Handles player X's move and triggers AI's move if applicable.
        """
        if self.board[index] == "" and self.current_player == "X":
            self.board[index] = "X"
            self.buttons[index].setText("X")
            self.buttons[index].setStyleSheet("background-color: #90EE90;") # Light green

            if self.check_winner():
                self.show_result("Player X Wins!")
                return
            elif "" not in self.board:  # Check for a draw
                self.show_result("It's a Draw!")
                return

            # Switch to AI's turn
            self.current_player = "O"
            self.info_label.setText("Player O's Turn")
            self.ai_move()

    def ai_move(self):
        """
        Handles AI's move using the minimax algorithm.
        """
        best_score = -float('inf')
        best_move = None

        # Find the best possible move for AI
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                score = self.minimax(self.board, 0, False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i

        # Make the AI's move
        if best_move is not None:
            self.board[best_move] = "O"
            self.buttons[best_move].setText("O")
            self.buttons[best_move].setStyleSheet("background-color: #FFB6C1;") # Light pink

        if self.check_winner():
            self.show_result("Player O Wins!")
            return
        elif "" not in self.board:  # Check for a draw
            self.show_result("It's a Draw!")
            return

        # Switch back to Player X's turn
        self.current_player = "X"
        self.info_label.setText("Player X's Turn")


    def minimax(self, board, depth, is_maximizing):
        """
        Minimax algorithm to evaluate the optimal move for the AI.
        """
        winner = self.get_winner()
        if winner == "X":
            return -10 + depth
        elif winner == "O":
            return 10 - depth
        elif "" not in board:  # Draw
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == "":
                    board[i] = "O"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = "" # Undo the move (backtracking to explore other possibilities).
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == "":
                    board[i] = "X"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        """
        Checks if there's a winner.
        """
        return self.get_winner() is not None

    def get_winner(self):
        """
        Determines if there's a winning combination on the board.
        """
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]

        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "":
                return self.board[a]
        return None

    def show_result(self, message):
        """
        Displays the game result and prompts the player to restart or quit.
        """
        reply = QMessageBox.question(
            self, "Game Over", f"{message}\nDo you want to play again?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
        ) # last argument is default...
        if reply == QMessageBox.Yes:
            self.reset_game()
        else:
            self.back_to_menu()

    def reset_game(self):
        """
        Resets the board for a new game.
        """
        self.board = ["" for _ in range(9)]
        self.current_player = "X"
        self.info_label.setText("Player X's Turn")
        for button in self.buttons:
            button.setText("")
            button.setStyleSheet("background-color: #ADD8E6; border: 2px solid #000;")

    def back_to_menu(self):
        """
        Returns to the welcome page.
        """
        self.welcome_page = WelcomePage()
        self.welcome_page.show()
        self.close()


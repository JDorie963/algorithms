#include <stdio.h>
#include <stdlib.h>

#define ROWS 3
#define COLS 3

// Function to print the current state of the Tic-Tac-Toe board
void print_board(char board[ROWS][COLS]) {
    printf("\n");
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            printf(" %c ", board[i][j]);
            if (j < COLS - 1) {
                printf("|");
            }
        }
        printf("\n");
        if (i < ROWS - 1) {
            printf("---|---|---\n");
        }
    }
    printf("\n");
}

// Function to check if a player has won
int check_win(char board[ROWS][COLS], char player) {
    // Check rows
    for (int i = 0; i < ROWS; i++) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player) {
            return 1;
        }
    }

    // Check columns
    for (int j = 0; j < COLS; j++) {
        if (board[0][j] == player && board[1][j] == player && board[2][j] == player) {
            return 1;
        }
    }

    // Check diagonals
    if ((board[0][0] == player && board[1][1] == player && board[2][2] == player) ||
        (board[0][2] == player && board[1][1] == player && board[2][0] == player)) {
        return 1;
    }

    return 0;
}

// Function to check if the board is full (draw)
int is_board_full(char board[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (board[i][j] == ' ') {
                return 0; // Board is not full
            }
        }
    }
    return 1; // Board is full
}

// Minimax algorithm (for AI player)
int minimax(char board[ROWS][COLS], int depth, int is_maximizing, char player) {
    if (check_win(board, 'X')) {
        return -10 + depth; 
    } else if (check_win(board, 'O')) {
        return 10 - depth;
    } else if (is_board_full(board)) {
        return 0; 
    }

    if (is_maximizing) {
        int best_score = -1000;
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (board[i][j] == ' ') {
                    board[i][j] = 'O';
                    int score = minimax(board, depth + 1, 0, 'O');
                    board[i][j] = ' ';
                    best_score = fmax(score, best_score);
                }
            }
        }
        return best_score;
    } else {
        int best_score = 1000;
        for (int i = 0; i < ROWS; i++) {
            for (int j = 0; j < COLS; j++) {
                if (board[i][j] == ' ') {
                    board[i][j] = 'X';
                    int score = minimax(board, depth + 1, 1, 'X');
                    board[i][j] = ' ';
                    best_score = fmin(score, best_score);
                }
            }
        }
        return best_score;
    }
}

// Find the best move for the AI player
int* find_best_move(char board[ROWS][COLS]) {
    int best_score = -1000;
    int best_row = -1;
    int best_col = -1;

    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            if (board[i][j] == ' ') {
                board[i][j] = 'O';
                int score = minimax(board, 0, 0, 'O');
                board[i][j] = ' ';
                if (score > best_score) {
                    best_score = score;
                    best_row = i;
                    best_col = j;
                }
            }
        }
    }

    int* best_move = (int*)malloc(2 * sizeof(int));
    best_move[0] = best_row;
    best_move[1] = best_col;
    return best_move;
}

int main() {
    char board[ROWS][COLS] = {
        {' ', ' ', ' '},
        {' ', ' ', ' '},
        {' ', ' ', ' '}
    };

    char current_player = 'X';

    printf("Welcome to Tic-Tac-Toe!\n");
    print_board(board);

    while (1) {
        if (current_player == 'X') {
            int row, col;
            printf("Player X's Turn: Enter row (1-3) and column (1-3): ");
            scanf("%d %d", &row, &col);
            row--;
            col--;

            if (row < 0 || row >= ROWS || col < 0 || col >= COLS || board[row][col] != ' ') {
                printf("Invalid move. Try again.\n");
                continue;
            }

            board[row][col] = 'X';
        } else {
            printf("AI's Turn:\n");
            int* best_move = find_best_move(board);
            int row = best_move[0];
            int col = best_move[1];
            board[row][col] = 'O';
            free(best_move);
        }

        print_board(board);

        if (check_win(board, 'X')) {
            printf("Player X wins!\n");
            break;
        } else if (check_win(board, 'O')) {
            printf("AI wins!\n");
            break;
        } else if (is_board_full(board)) {
            printf("It's a draw!\n");
            break;
        }

        current_player = (current_player == 'X') ? 'O' : 'X';
    }

    return 0;
}
import pygame
import sys
import tkinter as tk
from tkinter import messagebox

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
LINE_WIDTH = 5
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Game variables
board = [['' for _ in range(3)] for _ in range(3)]
turn = 'X'
winner = None
game_over = False

# Initialize window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tx3")

# Initialize Tkinter root
root = tk.Tk()
root.withdraw() 

# restart confirmation
def restart_dialog():
    result = messagebox.askyesno("Restart", "Do you want to play again?")
    if result:
        restart_game()

# Draw grid
def draw_grid():
    window.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(window, BLACK, (i * WIDTH // 3, 0), (i * WIDTH // 3, HEIGHT), LINE_WIDTH)
        pygame.draw.line(window, BLACK, (0, i * HEIGHT // 3), (WIDTH, i * HEIGHT // 3), LINE_WIDTH)

# Draw X|O 
def draw_symbol(row, col):
    x = col * WIDTH // 3 + WIDTH // 6
    y = row * HEIGHT // 3 + HEIGHT // 6
    if board[row][col] == 'X':
        pygame.draw.line(window, RED, (x - 50, y - 50), (x + 50, y + 50), LINE_WIDTH)
        pygame.draw.line(window, RED, (x + 50, y - 50), (x - 50, y + 50), LINE_WIDTH)
    elif board[row][col] == 'O':
        pygame.draw.circle(window, BLUE, (x, y), 50, LINE_WIDTH)

# Check for a win
def check_winner():
    global winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            winner = board[row][0]
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            winner = board[0][col]
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        return True
    return False

# Restart the game
def restart_game():
    global board, turn, winner, game_over
    board = [['' for _ in range(3)] for _ in range(3)]
    turn = 'X'
    winner = None
    game_over = False

# Display winner 
def display_winner():
    global game_over
    if winner:
        messagebox.showinfo("Winner", f"Player {winner} wins!")
    else:
        messagebox.showinfo("Winner", "It's a draw!")
    restart_dialog()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // (HEIGHT // 3)
            col = x // (WIDTH // 3)
            if board[row][col] == '':
                board[row][col] = turn
                if check_winner():
                    display_winner()
                elif all(board[i][j] != '' for i in range(3) for j in range(3)):
                    display_winner()
                else:
                    turn = 'O' if turn == 'X' else 'X'

    draw_grid()
    for row in range(3):
        for col in range(3):
            if board[row][col] != '':
                draw_symbol(row, col)
    pygame.display.update()

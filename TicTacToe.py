import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        
        # Game state
        self.current_player = 'X'  # Player is X, Computer is O
        self.board = [''] * 9
        self.buttons = []
        
        # Create the game board
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.window,
                    text='',
                    font=('Arial', 20),
                    width=6,
                    height=3,
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i, column=j)
                self.buttons.append(button)
    
    def button_click(self, row, col):
        index = row * 3 + col
        
        # Check if the cell is empty
        if self.board[index] == '':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.reset_game()
            elif '' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                # Computer's turn
                self.current_player = 'O'
                self.computer_move()
    
    def computer_move(self):
        # Simple AI: randomly choose an empty cell
        empty_cells = [i for i, cell in enumerate(self.board) if cell == '']
        if empty_cells:
            move = random.choice(empty_cells)
            self.board[move] = 'O'
            self.buttons[move].config(text='O')
            
            if self.check_winner('O'):
                messagebox.showinfo("Game Over", "Computer wins!")
                self.reset_game()
            elif '' not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = 'X'
    
    def check_winner(self, player):
        # Check rows, columns and diagonals
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False
    
    def reset_game(self):
        self.board = [''] * 9
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text='')
    
    def run(self):
        self.window.mainloop()

# Create and run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()

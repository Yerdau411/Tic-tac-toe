import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x500")
        self.window.configure(bg="#2c3e50")
        self.window.resizable(False, False)
        
        # Game state
        self.current_player = "X"
        self.board = [""] * 9
        self.game_active = True
        
        # Colors
        self.bg_color = "#2c3e50"
        self.button_color = "#34495e"
        self.button_hover = "#3498db"
        self.x_color = "#e74c3c"
        self.o_color = "#f39c12"
        self.text_color = "#ecf0f1"
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_label = tk.Label(
            self.window,
            text="Tic Tac Toe",
            font=("Arial", 24, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        title_label.pack(pady=20)
        
        # Player turn indicator
        self.turn_label = tk.Label(
            self.window,
            text=f"Player {self.current_player}'s Turn",
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.turn_label.pack(pady=10)
        
        # Game board frame
        board_frame = tk.Frame(self.window, bg=self.bg_color)
        board_frame.pack(pady=20)
        
        # Create buttons for the game board
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(
                    board_frame,
                    text="",
                    font=("Arial", 20, "bold"),
                    width=6,
                    height=3,
                    bg=self.button_color,
                    fg=self.text_color,
                    relief="flat",
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i, column=j, padx=2, pady=2)
                button.bind("<Enter>", lambda e, btn=button: self.on_hover(btn, True))
                button.bind("<Leave>", lambda e, btn=button: self.on_hover(btn, False))
                row.append(button)
            self.buttons.append(row)
        
        # Reset button
        reset_button = tk.Button(
            self.window,
            text="New Game",
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg=self.text_color,
            relief="flat",
            command=self.reset_game,
            width=15,
            height=2
        )
        reset_button.pack(pady=20)
        
        # Score display
        score_frame = tk.Frame(self.window, bg=self.bg_color)
        score_frame.pack(pady=10)
        
        self.score_x = 0
        self.score_o = 0
        
        score_x_label = tk.Label(
            score_frame,
            text="Player X: 0",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.x_color
        )
        score_x_label.pack(side=tk.LEFT, padx=10)
        
        score_o_label = tk.Label(
            score_frame,
            text="Player O: 0",
            font=("Arial", 12),
            bg=self.bg_color,
            fg=self.o_color
        )
        score_o_label.pack(side=tk.LEFT, padx=10)
        
        self.score_x_label = score_x_label
        self.score_o_label = score_o_label
        
    def on_hover(self, button, entering):
        if entering and button["text"] == "":
            button.configure(bg=self.button_hover)
        else:
            button.configure(bg=self.button_color)
            
    def button_click(self, row, col):
        if not self.game_active:
            return
            
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[row][col].configure(
                text=self.current_player,
                fg=self.x_color if self.current_player == "X" else self.o_color
            )
            
            if self.check_winner():
                self.game_active = False
                winner = self.current_player
                if winner == "X":
                    self.score_x += 1
                    self.score_x_label.configure(text=f"Player X: {self.score_x}")
                else:
                    self.score_o += 1
                    self.score_o_label.configure(text=f"Player O: {self.score_o}")
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            elif "" not in self.board:
                self.game_active = False
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.configure(text=f"Player {self.current_player}'s Turn")
                
    def check_winner(self):
        # Winning combinations
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] == self.current_player):
                # Highlight winning combination
                for pos in combo:
                    row, col = pos // 3, pos % 3
                    self.buttons[row][col].configure(bg="#e74c3c")
                return True
        return False
        
    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_active = True
        
        # Reset all buttons
        for row in self.buttons:
            for button in row:
                button.configure(text="", bg=self.button_color)
                
        self.turn_label.configure(text=f"Player {self.current_player}'s Turn")
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run() 
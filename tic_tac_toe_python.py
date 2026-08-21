# Tic Tac Toe in Python Practice Project

import tkinter as tk
from tkinter import font

class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {}
        self.create_board_display()
        self.create_board_grid()

# Setting up the display:
    def create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master = display_frame,
            text = "Ready?",
            font = font.Font(size=28, weight="bold")
        )

        self.display.pack()

# Setting up the game's grid:
    def create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=26, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightgreen"
                )
                self._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )

def main():
    board = TicTacToeBoard()
    board.mainloop()

if __name__ == "__main__":
    main()
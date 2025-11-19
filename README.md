# python.game

PROJECT TITLE: Game Hub
Author:Sai Sai

Description:
This project is a graphical Tic-Tac-Toe game built with Python and Tkinter.
It's contains a simple game menu and you can open and play Tic Tac Toe.
The game allows two players to play on a 3×3 grid, shows the winner, detects draws, and allows restarting the game.
More games can be added later (like Snake & Ladder).

Purposr of the program:
The goal of this project is to create a complete Python application that demonstrates:
GUI programming (Tkinter canvas)
Clean function decomposition
Use of data structures (lists, sets, tuples, dicts)
Reading/writing logs to external files
Using a simple API
Proper error handling and input validation
Git workflow with atomic commits

 Features:

- **tic_tac_toe()** – Main function that launches the Tic Tac Toe game window.  
- **cell_click(r, c)** – Handles player moves, validates if a cell is empty, updates the board, checks for win/draw, and switches the turn.  
- **restart()** – Resets the board and restarts the game.  
- **draw_symbol(r, c, symbol)** – Draws “X” or “O” in the selected cell.  
- **check_win()** – Checks for winning conditions in rows, columns, and diagonals.  
- **check_draw()** – Checks if the game is a draw (all cells filled).  
- **draw_win_line(index, kind)** – Draws a line across the winning row, column, or diagonal.  
- **canvas_click(event)** – Handles mouse clicks on the canvas to detect player moves.  
- **x_mark(r, c)** & **o_mark(r, c)** – Functions that draw the X and O symbols.


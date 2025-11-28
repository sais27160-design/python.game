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

1. tic_tac_toe() – Initializes the game window, board, canvas, symbols, stats, and UI.
2. move(r, c) – Handles a player's move (decorated with @log_move).
3. click(event) – Detects mouse click position and calls move().
4. restart() – Clears the board and resets the game.
5. draw_grid() – Draws the Tic Tac Toe 3×3 grid.
6. draw_symbol(r, c, symbol) – Draws X or O in the selected cell.
7. X.__call__(r, c) – Draws a blue X.
8. O.__call__(r, c) – Draws a red O.
9. win_line(index, kind) – Draws the green line through the winning row/column/diagonal.
10. win() – Checks all winning conditions.
11. draw() – Checks if the game is a draw.
12. save_stats(stats) – Saves X wins, O wins, and draws into stats.json.
13. log_move(func) – Logs each move function call.
14. Symbol – Base class holding canvas, cell size, and padding.
15. X(Symbol) and O(Symbol) – Classes responsible for drawing player symbols.
16. Restart button – Calls restart().
17. Quit button – Closes the game window.


![Main Screen](<img width="996" height="897" alt="image" src="https://github.com/user-attachments/assets/5844b1e0-4573-4c31-8d5c-66dcbbcbab26" />)  

Installation:
1.git clone https://github.com/yourusername/my_project.git
cd my_project
2.pip install -r requirements.txt
3.python homescreen.py

Usage:
Open homescreen.py.
Click Play Tic Tac Toe to open the game.
Click Restart in the Tic Tac Toe window to start a new game.
Wins, losses, and draws are tracked and displayed.
Add more games to the hub by creating functions similar to open_tictactoe().

TODO:
(Incomplete Features)

Add more games to the hub (e.g., Snake & Ladder).
Implement export of stats to PDF.
Fix edge cases (e.g., move outside the grid).
AI opponent for Tic Tac Toe.

Project Structure:

my_project/
├── .git/                 
├── .gitignore            
├── README.md             
├── requirements.txt      
├── homescreen.py        
├── project.py           
├── utils.py              
├── tests/                
│   └── test_utils.py     
└── data/                 
    └── stats.json       

Acknowledgments:
[tutorial from Coad Coach youtube] for inspiration






    


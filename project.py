import tkinter as tk
from tkinter import messagebox

def tic_tac_toe():
    """
    Launch the Tic Tac Toe game in a new window.
    
    """

    root = tk.Toplevel()
    root.title("Tic Tac Toe")

    #Game 
    player = ["X"]
    board = []
    for i in range(3):
        board.append(["", "", ""])


    canvas_size = 500
    cell_size = canvas_size // 3
    padding = 40

    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
    canvas.grid(row=0, column=0, columnspan=3, pady=20)

    #Draw grid
    def draw_grid():
        """
        Draw the Tic Tac Toe grid lines on the canvas.
        
        """
        for i in range(1, 3):
            canvas.create_line(0, i * cell_size, canvas_size, i * cell_size, width=3)
            canvas.create_line(i * cell_size, 0, i * cell_size, canvas_size, width=3)

    draw_grid()
    
    def draw_board_line(x1, y1, x2, y2):
        """
        Draw a single line on the canvas.
        x1, y1: Start coordinates.
        x2, y2: End coordinates.
        """
        canvas.create_line(x1, y1, x2, y2, width=3)

    #symbols
    def x_mark(r, c):
        """
        Draw an X symbol in the specified cell.
        
        """
        x1 = c * cell_size + padding
        y1 = r * cell_size + padding
        x2 = (c + 1) * cell_size - padding
        y2 = (r + 1) * cell_size - padding
        canvas.create_line(x1, y1, x2, y2, width=4, fill="blue")
        canvas.create_line(x1, y2, x2, y1, width=4, fill="blue")

    def o_mark(r, c):
        """
        Draw an O symbol in the specified cell.
        
        """
        x1 = c * cell_size + padding
        y1 = r * cell_size + padding
        x2 = (c + 1) * cell_size - padding
        y2 = (r + 1) * cell_size - padding
        canvas.create_oval(x1, y1, x2, y2, width=4, outline="red")

    #symbol for players
    def draw_symbol(r, c, symbol):
        """
        Draw the symbol (X or O) in the given cell.
        
        """
        if symbol == "X":
            x_mark(r, c)
        else:
            o_mark(r, c)

    #win line 
    def draw_win_line(index, kind):
        """
        Draw a line to indicate the winning row, column, or diagonal.
         "desc" (diagonal descending), "asc" (diagonal ascending)
        """
        if kind == "row":
            y = index * cell_size + cell_size // 2
            canvas.create_line(20, y, canvas_size - 20, y, width=6, fill="green")
        elif kind == "col":
            x = index * cell_size + cell_size // 2
            canvas.create_line(x, 20, x, canvas_size - 20, width=6, fill="green")
        elif kind == "desc":
            canvas.create_line(20, 20, canvas_size - 20, canvas_size - 20, width=6, fill="green")
        elif kind == "asc":
            canvas.create_line(20, canvas_size - 20, canvas_size - 20, 20, width=6, fill="green")
    
    #check win
    def check_win():
        """
        Check if a player has won the game.
        
        """
        #rows
        for r in range(3):
            if board[r][0] == board[r][1] == board[r][2] != "":
                draw_win_line(r, "row")
                return board[r][0]

        #columns
        for c in range(3):
            if board[0][c] == board[1][c] == board[2][c] != "":
                draw_win_line(c, "col")
                return board[0][c]

        #diagonals
        if board[0][0] == board[1][1] == board[2][2] != "":
            draw_win_line(0, "desc")
            return board[0][0]

        if board[0][2] == board[1][1] == board[2][0] != "":
            draw_win_line(0, "asc")
            return board[0][2]

        return None
    
    #check draw
    def check_draw():
        """
        Check if the game is a draw (all cells filled with no winner).
        
        """
        return all(board[r][c] != "" for r in range(3) for c in range(3))

    
    #click on canvas
    def canvas_click(event):
        """
        Handle mouse click events on the canvas.
        
        """
        c = event.x // cell_size
        r = event.y // cell_size

        if r > 2 or c > 2:
            return

        cell_click(r, c)

    canvas.bind("<Button-1>", canvas_click)
    
    #player move
    def cell_click(r, c):
        """
        Process a player's move on the selected cell.
        
        """
        if board[r][c] != "":
            return

        board[r][c] = player[0]
        draw_symbol(r, c, player[0])
        
        
        winner = check_win()
        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            restart()
            return

        if check_draw():
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            restart()
            return

        # switch player
        player[0] = "O" if player[0] == "X" else "X"

    
    #game restart
    def restart():
        """
        Reset the game board to empty and redraw the grid.
        """
        for r in range(3):
            for c in range(3):
                board[r][c] = ""
        player[0] = "X"
        canvas.delete('all')
        draw_grid()
    
    #buttons
    btn_restart = tk.Button(root, text="Restart", width=10, command=restart)
    btn_restart.grid(row=4, column=0, pady=10)

    btn_quit = tk.Button(root, text="Quit", width=10, command=root.destroy)
    btn_quit.grid(row=4, column=2, pady=10)

   




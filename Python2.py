# x = 1054


# print(f"hello world {x:.2f} ")

# x = 12

# if x > 10 or x < 10 :
#     print('nor equal')
 
# elif x == 10:
#     print('equal')

# else:
#     print('invalid input')   
    
    
# print('The end')         

# n = int(input())
# sec = (n // 10) % 10
# first = n % 10
# third = (n // 100)

# print(sec,first,third)

# x = float(input())
# f=  x - int(x)
# d1 = int(f * 10)

# print(d1)

# x = float(input())
# f=   int(x)
# d1 = x - f
# print(d1)

# for i in range(1,6):
#     print('*' * i)

# print()
        
# for i in range(1,6):
#     print('* ' * i)   
    
# print()     

# for i in range(5, 0, -1):
#     print('* ' * i)
    
# print()

# for i in range(1 , 6):
#     print("  " * (5 - i) + "* " * i)
   
# print()    

# for i in range(1 , 7):
#  print(" " * (6 - i) + "* " * (i - 1) + "*")
 
# print()






# for i in range(1, 7):
#     for j in range(6 - i):
#         print(' ', end='')
#     for a in range(1, i + 1):
#         if a == 1 or a == i or i == 6:
#             print('*', end='')
#         else:
#             print(' ', end='')
#         if a != i: 
#             print(' ', end='')
#     print()



# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(i, end=' ')
#     print()



# num = 1 
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(num, end=' ')
#         num += 1
#     print()





# num = 1
# counts = [1, 2, 3, 4, 4, 5]
# for i in range(6):
#     print(' ' * (6 - i - 1), end='')

    
#     for j in range(counts[i]):
#         print(num, end=' ')
#         num += 1
# #     print()
# ==================================================================


# import tkinter as tk
# from tkinter import messagebox

# # --- Window Setup ---
# root = tk.Tk()
# root.title("Tic Tac Toe")

# # --- Variables ---
# player = "X"
# board = [["" for _ in range(3)] for _ in range(3)]
# canvas_size = 300
# cell_size = canvas_size // 3
# canvas = tk.Canvas(root, width=canvas_size, height=canvas_size, bg="white")
# canvas.pack(pady=20)

# # --- Draw Grid ---
# def draw_grid():
#     for i in range(1, 3):
#         canvas.create_line(0, i*cell_size, canvas_size, i*cell_size, width=3)
#         canvas.create_line(i*cell_size, 0, i*cell_size, canvas_size, width=3)

# draw_grid()

# # --- Draw X or O ---
# def draw_symbol(r, c, symbol):
#     x1 = c*cell_size + 20
#     y1 = r*cell_size + 20
#     x2 = (c+1)*cell_size - 20
#     y2 = (r+1)*cell_size - 20
#     if symbol == "X":
#         canvas.create_line(x1, y1, x2, y2, width=4, fill="blue")
#         canvas.create_line(x1, y2, x2, y1, width=4, fill="blue")
#     else:
#         canvas.create_oval(x1, y1, x2, y2, width=4, outline="red")

# # --- Check Win ---
# def check_win():
#     # Rows
#     for r in range(3):
#         if board[r][0] == board[r][1] == board[r][2] != "":
#             draw_win_line(r, "row")
#             return board[r][0]
#     # Columns
#     for c in range(3):
#         if board[0][c] == board[1][c] == board[2][c] != "":
#             draw_win_line(c, "col")
#             return board[0][c]
#     # Diagonals
#     if board[0][0] == board[1][1] == board[2][2] != "":
#         draw_win_line(0, "desc")
#         return board[0][0]
#     if board[0][2] == board[1][1] == board[2][0] != "":
#         draw_win_line(0, "asc")
#         return board[0][2]
#     return None

# # --- Check Draw ---
# def check_draw():
#     for row in board:
#         for cell in row:
#             if cell == "":
#                 return False
#     return True

# # --- Draw Winning Line ---
# def draw_win_line(index, kind):
#     if kind == "row":
#         y = index*cell_size + cell_size//2
#         canvas.create_line(20, y, canvas_size-20, y, width=4, fill="green")
#     elif kind == "col":
#         x = index*cell_size + cell_size//2
#         canvas.create_line(x, 20, x, canvas_size-20, width=4, fill="green")
#     elif kind == "desc":
#         canvas.create_line(20, 20, canvas_size-20, canvas_size-20, width=4, fill="green")
#     elif kind == "asc":
#         canvas.create_line(20, canvas_size-20, canvas_size-20, 20, width=4, fill="green")

# # --- Click Handler ---
# def click(event):
#     global player
#     r = event.y // cell_size
#     c = event.x // cell_size
#     if board[r][c] == "":
#         board[r][c] = player
#         draw_symbol(r, c, player)
#         winner = check_win()
#         if winner:
#             messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
#             restart_game()
#         elif check_draw():
#             messagebox.showinfo("Tic Tac Toe", "It's a draw!")
#             restart_game()
#         else:
#             player = "O" if player == "X" else "X"

# # --- Restart Game ---
# def restart_game():
#     global board, player
#     board = [["" for _ in range(3)] for _ in range(3)]
#     player = "X"
#     canvas.delete("all")
#     draw_grid()

# canvas.bind("<Button-1>", click)

# # --- Buttons ---
# frame = tk.Frame(root)
# frame.pack()
# restart_btn = tk.Button(frame, text="Restart", command=restart_game, width=10, height=2)
# restart_btn.pack(side="left", padx=10)
# quit_btn = tk.Button(frame, text="Quit", command=root.quit, width=10, height=2)
# quit_btn.pack(side="left", padx=10)

# root.mainloop()
# ================================================


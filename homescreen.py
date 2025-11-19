import tkinter as tk

#Open Game
def open_tictactoe():
    from project import tic_tac_toe
    tic_tac_toe()


#Window 
root = tk.Tk()
root.title("Game Hub")
root.geometry("800x800")
root.config(bg="lightblue")

#Title 
title = tk.Label(root, text="GAME MENU", font=("Arial", 24), bg="lightblue")
title.pack(pady=40)

#Buttons 
play_btn = tk.Button(root, text="Play Tic Tac Toe", font=("Arial", 16),
                     width=18, command=open_tictactoe)
play_btn.pack(pady=15)

choose_btn = tk.Button(root, text="Sneak and ladder", font=("Arial", 16),
                       width=18)
choose_btn.pack(pady=15)

exit_btn = tk.Button(root, text="Exit", font=("Arial", 16),
                     width=18, command=root.destroy)
exit_btn.pack(pady=15)


root.mainloop()

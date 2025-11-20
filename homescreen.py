import tkinter as tk

#Open Game
def open_tictactoe():
    from project import tic_tac_toe
    tic_tac_toe()


#Window 
game = tk.Tk()
game.title("Game Hub")
game.geometry("800x800")
game.config(bg="lightblue")

#Title 
title = tk.Label(game, text="GAME MENU", font=("Arial", 24), bg="lightblue")
title.pack(pady=40)

#Buttons 
play_btn = tk.Button(game, text="Play Tic Tac Toe", font=("Arial", 16),
                     width=18, command=open_tictactoe)
play_btn.pack(pady=15)

choose_btn = tk.Button(game, text="Sneak and ladder", font=("Arial", 16),
                       width=18)
choose_btn.pack(pady=15)

exit_btn = tk.Button(game, text="Exit", font=("Arial", 16),
                     width=18, command=game.destroy)
exit_btn.pack(pady=15)


game.mainloop()

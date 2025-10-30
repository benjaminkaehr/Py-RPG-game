import tkinter as tk
from tkinter.font import BOLD

# -Exit with ESC-
def on_escape(event=None):
    root.destroy()

# -Creates the Window-
root = tk.Tk() 
root.title("Hangman Minigame")
root.attributes("-fullscreen",True)
root.configure(bg="#FFFFF5")
root.bind_all("<Escape>",on_escape)
root.resizable(False,False)


#--Screens--
Game_Screen = tk.Frame(root, bg="#FFFFFF")
def show_game():
    Menu_Screen.forget()
    Game_Screen.tkraise()
    Game_Screen.pack(fill="both", expand=True)
    Game_Normal_Buttons()

#--Grundvarabeln Variablen--
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()



#---Menu---
Menu_Screen = tk.Frame(root, bg="#FFFFF5")
Menu_Screen.pack(fill="both", expand=True)
Menu_Screen.tkraise()

def show_menu():
    Menu_Screen.tkraise()

#--Canvas für Design-Linien--
canvas = tk.Canvas(Menu_Screen, bg="#FFFFF5", highlightthickness=0)
canvas.pack(fill="both", expand=True)

#-Diagonale Linien-
for i in range(0, screen_width, 200):
    canvas.create_line(i, 0, i + 300, screen_height, fill="#CFCFCF", width=2)
for i in range(0, screen_width, 250):
    canvas.create_line(i, screen_height, i + 300, 0, fill="#E5E5E5", width=1)

#-Horizontale Linien-
canvas.create_line(100, 100, screen_width - 100, 100, fill="#AAAAAA", width=2)
canvas.create_line(100, screen_height - 100, screen_width - 100, screen_height - 100, fill="#AAAAAA", width=2)


#--Menu Buttons & Labels--
Menu_title = tk.Label(Menu_Screen, text="Py-RPG-game", font=("Arial", 48, BOLD), fg="#000000", bg="#FFFFF5" )
Menu_title.place(relx=0.5, rely=0.1, anchor="center")

Menu_Start_Button = tk.Button(Menu_Screen, text="Start Game", font=("Arial", 28), fg="#000000", bg="#FFFFC2", width=10, height=1, command=show_game)
Menu_Start_Button.place(relx=0.5, rely=0.375, anchor="center")

Menu_Settings_Button = tk.Button(Menu_Screen, text="Settings", font=("Arial", 28), fg="#000000", bg="#FFFFC2", width=10, height=1)
Menu_Settings_Button.place(relx=0.5, rely=0.45, anchor="center")

Menu_Screen_Button = tk.Button(Menu_Screen, text="Exit Game", font=("Arial", 28), fg="#000000", bg="#FFC2C2", width=10, height=1, command=root.destroy)
Menu_Screen_Button.place(relx=0.5, rely=0.525, anchor="center")



#---Game---
def Game_Normal_Buttons():
    Game_Angrerifen_Button = tk.Button(Game_Screen, text="Angreifen", font=("Arial", 28), fg="#000000", bg="#FFFFC2", width=10, height=1)
    Game_Angrerifen_Button.place(relx=0.74, rely=0.8, anchor="center")
    Game_Verteidigen_Button = tk.Button(Game_Screen, text="Verteidigen", font=("Arial", 28), fg="#000000", bg="#FFFFC2", width=10, height=1)
    Game_Verteidigen_Button.place(relx=0.8, rely=0.73, anchor="center")
    Game_Inventar_Button = tk.Button(Game_Screen, text="Inventar", font=("Arial", 28), fg="#000000", bg="#FFFFC2", width=10, height=1)
    Game_Inventar_Button.place(relx=0.86, rely=0.66, anchor="center")



#--Main loop needs to be at the end of the file--
root.mainloop()
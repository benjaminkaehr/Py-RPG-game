import tkinter as tk
from tkinter.font import BOLD

# -exit with esc-
def on_escape(event=None):
    root.destroy()

# -Creates the Window-
root = tk.Tk() 
root.title("Hangman Minigame")
root.attributes("-fullscreen",True)
root.configure(bg="#FFFFF5")
root.bind_all("<Escape>",on_escape)
root.resizable(False,False)

#---Menu---
Menu_Screen = tk.Frame(root, bg="#FFFFF5")
Menu_Screen.pack(fill="both", expand=True)
Menu_Screen.tkraise()

def show_menu():
    Menu_Screen.tkraise()

#--Menu Buttons & Labels--
Menu_title = tk.Label(Menu_Screen, text="Py-RPG-game", font=("Arial", 48, BOLD), fg="#000000", bg="#FFFFF5" )
Menu_title.pack(pady=100)

Menu_Start_Button = tk.Button(Menu_Screen, text="Start Game", font=("Arial", 28), fg="#000000", bg="#FFFFC2", width=10, height=1)
Menu_Start_Button.place(relx=0.5, rely=0.375, anchor="center")

Menu_Settings_Button = tk.Button(Menu_Screen, text="Settings", font=("Arial", 28), fg="#000000", bg="#FFFFC2", width=10, height=1)
Menu_Settings_Button.place(relx=0.5, rely=0.45, anchor="center")

Menu_Screen_Button = tk.Button(Menu_Screen, text="Exit Game", font=("Arial", 28), fg="#000000", bg="#FFC2C2", width=10, height=1, command=root.destroy)
Menu_Screen_Button.place(relx=0.5, rely=0.525, anchor="center")

#--Main loop needs to be at the end of the file--
root.mainloop()
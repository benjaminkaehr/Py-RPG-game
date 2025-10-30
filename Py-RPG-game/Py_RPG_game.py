import tkinter as tk

# -exit with esc-
def on_escape(event=None):
    root.destroy()

# -Creates the Window-
root = tk.Tk() 
root.title("Hangman Minigame")
root.attributes("-fullscreen",True)
root.configure(bg="#FFFFED")
root.bind_all("<Escape>",on_escape)
root.resizable(False,False)

#-Screens-
screen1 = tk.Frame(root, bg="#FFFFED")
screen1.pack(fill="both", expand=True)
screen1.tkraise()

#--Main loop needs to be at the end of the file--
root.mainloop()

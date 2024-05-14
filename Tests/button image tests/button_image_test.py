import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


app = ttk.Window(title="Board Games Collection", themename="superhero", resizable=(False, False))


path = os.path.join("data", "icons", "game_icon.png")
lol = ttk.PhotoImage(file=path)
lol = lol.subsample(25)

games_btn = ttk.Button(app, text="hello", image=lol)
games_btn.pack()

path1 = os.path.join("data", "icons", "test_icon.png")
lol1 = ttk.PhotoImage(file=path1)
lol1 = lol1.subsample(25)

games_btn1 = ttk.Button(app, text="hi", image=lol1)
games_btn1.pack()

app.mainloop()
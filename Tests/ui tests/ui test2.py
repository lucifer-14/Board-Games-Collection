import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar, Frame

class MainForm(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        
        # Create main container
        self.main_container = ttk.Frame(self)
        self.main_container.pack(fill=BOTH, expand=YES)

        # Create side panel for buttons
        self.side_panel = ttk.Frame(self.main_container, padding=(10, 10))
        self.side_panel.pack(side=LEFT, fill=Y)

        # Create content panel to show profile info or game list
        self.content_panel = ttk.Frame(self.main_container, padding=(10, 10))
        self.content_panel.pack(side=RIGHT, fill=BOTH, expand=YES)

        # Create buttons in the side panel
        self.profile_btn = ttk.Button(self.side_panel, text="Profile", command=self.show_profile)
        self.profile_btn.pack(fill=X, pady=10)

        self.games_btn = ttk.Button(self.side_panel, text="Games", command=self.show_games)
        self.games_btn.pack(fill=X, pady=10)

        # Title label
        self.title = ttk.Label(self.main_container, text="App Name", font=("Garamond", 24))
        self.title.pack(fill=X, pady=10, anchor=CENTER)

    def show_profile(self):
        self.clear_content()
        profile_label = ttk.Label(self.content_panel, text="Profile Information", font=("Garamond", 18))
        profile_label.pack(fill=BOTH, expand=YES)

    def show_games(self):
        self.clear_content()
        games_label = ttk.Label(self.content_panel, text="List of Games", font=("Garamond", 18))
        games_label.pack(fill=BOTH, expand=YES)

    def clear_content(self):
        for widget in self.content_panel.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = ttk.Window(title="Application", themename="superhero", resizable=(False, False))
    MainForm(app)
    app.mainloop()

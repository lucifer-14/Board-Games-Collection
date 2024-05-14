import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)

        # Title
        title = ttk.Label(self, text="My Cool App", font=("Garamond", 24))
        title.pack(pady=10)

        # Menu Buttons
        menu_frame = ttk.Frame(self)
        menu_frame.pack(pady=10)

        profile_button = ttk.Button(menu_frame, text="Profile", command=self.show_profile)
        profile_button.pack(side=LEFT, padx=5)

        games_button = ttk.Button(menu_frame, text="Games", command=self.show_games)
        games_button.pack(side=LEFT, padx=5)

        # Content Frame
        self.content_frame = ttk.Frame(self)
        self.content_frame.pack(fill=BOTH, expand=YES, pady=10)

    def show_profile(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        profile_label = ttk.Label(self.content_frame, text="Profile Information", font=("Garamond", 16))
        profile_label.pack(pady=10)

    def show_games(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        games_label = ttk.Label(self.content_frame, text="Games List", font=("Garamond", 16))
        games_label.pack(pady=10)

        game_list = ["Game 1", "Game 2", "Game 3"]
        for game in game_list:
            game_label = ttk.Label(self.content_frame, text=game)
            game_label.pack()

if __name__ == "__main__":
    app = ttk.Window(title="My Cool App", themename="superhero", resizable=(False, False))
    App(app)
    app.mainloop()

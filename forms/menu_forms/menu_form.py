import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import utils.config_handler as CONF_H
import utils.image_handler as IMG_H


class Menu_Form(ttk.Frame):
    def __init__(self, master) -> None:
        master.pack(fill=BOTH, expand=YES)      # master = main_container
        self.master = master

        self.conf_h = CONF_H.Config_Handler()

        w_width = master.winfo_screenwidth()
        w_height = master.winfo_screenheight()

        self.style = ttk.Style()
        self.style.configure('Custom.TButton', font=('Garamond', 12))

        # icons = {"game": "game_icon.png",
        #          "profile": "profile_icon.png"}
        # self.photoimages = []
        # for k, v in icons.items():
        #     path = os.path.join("data", "icons", v)
        #     with open(path, 'rb') as f:
        #         print(f.read())
        #     self.photoimages.append(ttk.PhotoImage(name=k, file=path))

        self.menu_container = ttk.Frame(master, padding=20)
        self.menu_container.pack(fill=BOTH, expand=YES)

        self.top_container = ttk.Frame(self.menu_container)
        self.top_container.pack(side=TOP, fill=X, pady=(0,10), expand=YES)

        lbl_title = ttk.Label(self.top_container, text=self.conf_h.get_config("APP_NAME").title(), font=("Garamond", 20))
        lbl_title.pack(fill=X)

        sep = ttk.Separator(self.top_container)
        sep.pack(fill=X, expand=YES)

        self.create_side_panel()
        self.create_main_panel()

    def create_side_panel(self):

        side_panel = ttk.Frame(self.menu_container)
        side_panel.pack(side=LEFT, fill=Y)

        # path = os.path.join("data", "icons", "game_icon.png")
        # lol = ttk.PhotoImage(file=path)

        img_h = IMG_H.Image_Handler()
        game_icon = img_h.get_icon("game", 150, 150)
        print(game_icon)

        games_btn = ttk.Button(side_panel, image=game_icon)
        games_btn.image = game_icon
        games_btn.pack(fill=X, pady=10, expand=YES)

        profile_btn = ttk.Button(side_panel, text="profile")
        profile_btn.pack(fill=X, pady=10)



        # title = ttk.Label(master=self.main_menu_container, text="Main Menu", font=("Garamond", 24))
        # title.pack(fill=X, pady=10, expand=YES, anchor=CENTER)

        # self.create_buttons()

    def create_main_panel(self):

        main_panel = ttk.Frame(self.menu_container, padding=(5, 10))
        main_panel.pack(side=RIGHT, fill=BOTH, expand=YES)

        lbl = ttk.Label(main_panel, text="hello")
        lbl.pack(fill=X)


        pass

    def create_buttons(self) -> None:
        container = ttk.Frame(self.main_menu_container)
        container.pack(fill=X, expand=YES, pady=5)

        login_btn = ttk.Button(master=container, text="Log In", style='Custom.TButton', command=self.on_login)
        login_btn.pack(fill=X, pady=10)

        register_btn = ttk.Button(master=container, text="Register", style='Custom.TButton', command=self.on_register)
        register_btn.pack(fill=X, pady=10)

        exit_btn = ttk.Button(master=container, text="Exit", style='Custom.TButton', command=self.on_exit())
        exit_btn.pack(fill=X, pady=10)
    
    def clear_content(self) -> None:
        for widget in self.master.winfo_children():
            widget.pack_forget()

    def on_login(self) -> None:
        self.clear_content()
        FALF.Login_Form(self.master)
    
    def on_register(self) -> None:
        self.clear_content()
        FALR.Register_Form(self.master)

    def on_exit(self) -> None:
        # sys.exit()
        pass

if __name__ == "__main__":

    app = ttk.Window(title="Board Games Collection", themename="superhero", resizable=(False, False))
    main_container = ttk.Frame(app)
    main_container.pack(fill=BOTH, expand=YES)
    Menu_Form(main_container)

    app.mainloop()
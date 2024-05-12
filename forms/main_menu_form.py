import sys
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import forms.auth_forms.login_form as FALF

class Main_Menu_Form(ttk.Frame):
    def __init__(self, master) -> None:
        master.pack(fill=BOTH, expand=YES)      # master = main_container
        self.master = master

        w_width = master.winfo_screenwidth()
        w_height = master.winfo_screenheight()

        self.style = ttk.Style()
        self.style.configure('Custom.TButton', font=('Garamond', 12))

        self.main_menu_container = ttk.Frame(master, padding=(w_width / 8, w_height / 10))
        self.main_menu_container.pack(fill=BOTH, expand=YES)

        title = ttk.Label(master=self.main_menu_container, text="Main Menu", font=("Garamond", 24))
        title.pack(fill=X, pady=10, expand=YES, anchor=CENTER)

        self.create_buttons()

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
        pass

    def on_exit(self) -> None:
        # sys.exit()
        pass

if __name__ == "__main__":

    app = ttk.Window(title="Board Games Collection", themename="superhero", resizable=(False, False))
    main_container = ttk.Frame(app)
    main_container.pack(fill=BOTH, expand=YES)
    Main_Menu_Form(main_container)

    app.mainloop()
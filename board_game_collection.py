import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import socket_handle
import sql_handle
from authentication_handle import login_form

class Main_Form(ttk.Frame):
    def __init__(self, master) -> None:
        w_width = master.winfo_screenwidth()
        w_height = master.winfo_screenheight()
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)

        self.style = ttk.Style()
        self.style.configure('Custom.TButton', font=('Garamond', 12))

        self.main_container = ttk.Frame(self)
        self.main_container.pack(fill=BOTH, expand=YES)

        self.main_menu_container = ttk.Frame(self.main_container, padding=(w_width / 8, w_height / 10))
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

        exit_btn = ttk.Button(master=container, text="Exit", style='Custom.TButton', command=self.quit)
        exit_btn.pack(fill=X, pady=10)
    
    def clear_content(self) -> None:
        for widget in self.main_container.winfo_children():
            widget.pack_forget()

    def on_login(self) -> None:
        self.clear_content()
        login_form.Login_Form(self.main_container)
        # print(self)
        # main_container2 = ttk.Frame(self)
        # main_container2.pack()

        # label = ttk.Label(main_container2, text="ehllo")
        # label.pack()
        # print(label)
    
    def on_register(self) -> None:
        pass




if __name__ == "__main__":

    app = ttk.Window(title="Board Games Collection", themename="superhero", resizable=(False, False))
    Main_Form(app)
    app.mainloop()
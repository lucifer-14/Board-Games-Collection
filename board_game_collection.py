import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import socket_handle
import sql_handle
from forms.main_menu_form import Main_Menu_Form


class Main_Form(ttk.Frame):
    def __init__(self, master) -> None:
        w_width = master.winfo_screenwidth()
        w_height = master.winfo_screenheight()
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)

        self.main_container = ttk.Frame(self)
        self.main_container.pack(fill=BOTH, expand=YES)

        Main_Menu_Form(self.main_container)



if __name__ == "__main__":

    app = ttk.Window(title="Board Games Collection", themename="superhero", resizable=(False, False))
    Main_Form(app)
    app.mainloop()
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import socket_handle
import sql_handle
import forms.main_menu_form as FMMF
import utils.config_handler as CONF_H

class Main_Form(ttk.Frame):
    def __init__(self, master) -> None:
        w_width = master.winfo_screenwidth()
        w_height = master.winfo_screenheight()
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)

        self.main_container = ttk.Frame(self)
        self.main_container.pack(fill=BOTH, expand=YES)

        FMMF.Main_Menu_Form(self.main_container)



if __name__ == "__main__":
    conf_h = CONF_H.Config_Handler()
    APP_NAME = conf_h.get_config("APP_NAME")
    app = ttk.Window(title=APP_NAME, themename="superhero", resizable=(False, False))
    Main_Form(app)
    app.mainloop()
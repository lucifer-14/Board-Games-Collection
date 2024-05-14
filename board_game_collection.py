import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import socket_handle
import sql_handle
import forms.main_menu_form as FMF
import forms.menu_forms.menu_form as FMMF
import utils.config_handler as CONF_H

class Main_Form(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)

        conf_h = CONF_H.Config_Handler()

        w_width = master.winfo_screenwidth()
        w_height = master.winfo_screenheight()

        self.pack(fill=BOTH, expand=YES)

        self.main_container = ttk.Frame(self)
        self.main_container.pack(fill=BOTH, expand=YES)

        if conf_h.get_config('CURRENT_SESSION'):
            FMMF.Menu_Form(self.main_container)
        else:
            FMF.Main_Menu_Form(self.main_container)



if __name__ == "__main__":
    conf_h = CONF_H.Config_Handler()
    APP_NAME = conf_h.get_config("APP_NAME")
    app = ttk.Window(title=APP_NAME, themename="superhero", resizable=(False, False))
    Main_Form(app)
    app.mainloop()
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import forms.main_menu_form as FMMF
import socket_handle.auth_handle.register as SAR
import validation.auth_handle.register_form_validation as VAR


class Register_Form(ttk.Frame):
    def __init__(self, master) -> None:
        # super.__init__(master)
        master.pack(fill=BOTH, expand=YES)      # master = main_container
        self.master = master

        w_width = master.winfo_screenwidth()
        w_height = master.winfo_screenheight()

        self.username = ttk.StringVar(value="")
        self.email = ttk.StringVar(value="")
        self.password = ttk.StringVar(value="")
        self.re_password = ttk.StringVar(value="")

        self.register_container = ttk.Frame(master, padding=(w_width / 8, w_height / 10))
        self.register_container.pack(fill=BOTH, expand=YES)
        
        title = ttk.Label(self.register_container, text="Register Form", font=("Garamond", 24), anchor=CENTER)
        title.pack(fill=X, pady=(10,40), expand=YES, anchor=CENTER)

        subcontainer = ttk.Frame(self.register_container)
        subcontainer.pack(fill=X, expand=YES, pady=2)

        hidden_lbl = ttk.Label(subcontainer, width=18)
        hidden_lbl.pack(side=LEFT, padx=5)
        self.hidden_comment = ttk.Label(subcontainer, font=("Garamond", 12))
        self.hidden_comment.pack(fill=X, padx=5, expand=YES)

        self.create_form_entry("Username:", self.username)
        self.create_form_entry("Email:", self.email)
        self.create_form_entry("Password:", self.password, is_password=True)
        self.create_form_entry("Re-Type Password:", self.re_password, is_password=True)

        self.create_control_buttons()


    def create_form_entry(self, label: str, variable: ttk.StringVar, is_password: bool = False) -> None:
        container = ttk.Frame(self.register_container)
        container.pack(fill=X, expand=YES, pady=10)
        
        lbl = ttk.Label(master=container, text=label.title(), width=18)
        lbl.pack(side=LEFT, padx=5)
        # lbl.grid(row=0, column=0, padx=(5, 0), sticky=E)

        if is_password:
            ent = ttk.Entry(master=container, textvariable=variable, show="*", width=30)
        else:
            ent = ttk.Entry(master=container, textvariable=variable, width=30)
        
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        # ent.grid(row=0, column=1, padx=(0, 5), sticky=W+E)


    def create_control_buttons(self):
        container = ttk.Frame(self.register_container)
        container.pack(fill=X, expand=YES, pady=(25, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Register",
            command=self.on_register,
            bootstyle=SUCCESS,
            width=8,
        )
        sub_btn.pack(side=RIGHT, padx=10)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Go Back",
            command=self.on_back,
            bootstyle=DANGER,
            width=8,
        )
        cnl_btn.pack(side=RIGHT, padx=10)


    def clear_content(self) -> None:
        for widget in self.master.winfo_children():
            widget.pack_forget()


    def on_register(self) -> None:

        reg_validation = VAR.Register_Form_Validation(username=self.username.get(),
                                                      email=self.email.get(),
                                                      password=self.password.get(),
                                                      re_password=self.re_password.get())
        
        validation_res, comment = reg_validation.validate()
        self.hidden_comment.config(text=comment)


        if validation_res:
            self.hidden_comment.config(bootstyle=SUCCESS)

            register_handle = SAR.Register(username=self.username.get(),
                                           email=self.email.get(),
                                           password=self.password.get())
            
            register_res = register_handle.register_request()

            self.hidden_comment.config(text=register_res['comment'])

            if register_res['is_register_success']:
                self.hidden_comment.config(bootstyle=SUCCESS)
            
            else:
                self.hidden_comment.config(bootstyle=DANGER)
                

        else:
            self.hidden_comment.config(bootstyle=DANGER)




    def on_back(self):
        self.clear_content()
        FMMF.Main_Menu_Form(self.master)
        


if __name__ == "__main__":

    app = ttk.Window(title="Board Games Collection", themename="superhero", resizable=(False, False))
    main_container = ttk.Frame(app)
    main_container.pack(fill=BOTH, expand=YES)
    Register_Form(main_container)

    app.mainloop()
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Login_Form(ttk.Frame):
    def __init__(self, master) -> None:
        # super.__init__(master)
        master.pack(fill=BOTH, expand=YES)      # master = main_container

        w_width = master.winfo_screenwidth()
        w_height = master.winfo_screenheight()

        self.username = ttk.StringVar(value="")
        self.password = ttk.StringVar(value="")

        self.login_container = ttk.Frame(master, padding=(w_width / 8, w_height / 10))
        self.login_container.pack(fill=BOTH, expand=YES)
        
        title = ttk.Label(self.login_container, text="Login Form", font=("Garamond", 24), anchor=CENTER)
        title.pack(fill=X, pady=(10,50), expand=YES, anchor=CENTER)

        self.create_form_entry("Username or Email:", self.username)
        self.create_form_entry("Password:", self.password, is_password=True)


    def create_form_entry(self, label: str, variable: ttk.StringVar, is_password: bool = False) -> None:
        container = ttk.Frame(self.login_container)
        container.pack(fill=X, expand=YES, pady=5)
        
        lbl = ttk.Label(master=container, text=label.title(), width=20)
        lbl.pack(side=LEFT, padx=5)
        # lbl.grid(row=0, column=0, padx=(5, 0), sticky=E)

        if is_password:
            ent = ttk.Entry(master=container, textvariable=variable, show="*")
        else:
            ent = ttk.Entry(master=container, textvariable=variable)
        
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        # ent.grid(row=0, column=1, padx=(0, 5), sticky=W+E)


    def create_control_buttons(self):
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Login",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)
        sub_btn.focus_set()

        cnl_btn = ttk.Button(
            master=container,
            text="Go Back",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

if __name__ == "__main__":

    app = ttk.Window(title="Board Games Collection", themename="superhero", resizable=(False, False))
    main_container = ttk.Frame(app)
    main_container.pack(fill=BOTH, expand=YES)
    Login_Form(main_container)

    app.mainloop()
from tkinter import *
from tkinter import ttk

class LoginWindow:

    def __init__(self, root):

        root.title("Login")

        mainframe = ttk.Frame(root, padding="12")
        mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
       
        ttk.Label(mainframe, text="Username").grid(column=0, row=0, sticky=W)
        self.username = StringVar()
        username_entry = ttk.Entry(mainframe, width=30, textvariable=self.username)
        username_entry.grid(column=0, row=1)

        ttk.Label(mainframe, text="Password").grid(column=0, row=2, sticky=W, pady="5 0")
        self.password = StringVar()
        password_entry = ttk.Entry(mainframe, width=30, textvariable=self.password, show="*")
        password_entry.grid(column=0, row=3)
        
        #forgot_password_btn = ttk.Button(mainframe, text="Forgot password?", command=self.forgot_password)
        #forgot_password_btn.configure()
        #forgot_password_btn.grid(column=0, row=5, sticky=W)
        mainframe.rowconfigure(4, weight=10)

        ttk.Button(mainframe, text="Login", command=self.submit_login, width=30).grid(column=0, row=5, pady="10 0")

        username_entry.focus()
        #root.bind("<Return>", self.submit_login)
        
    def submit_login(self, *args):
        print("Pressed Login")
        print(self.username.get(), self.password.get())

    def forgot_password(self, *args):
        print("Pressed forgot password")

root = Tk()
LoginWindow(root)
root.mainloop()
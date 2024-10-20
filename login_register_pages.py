from csv import *
from tkinter import *
from tkinter import messagebox

type_of_login = None
user_name = None

class login_register_class:
    def __init__(self):
        self.root = Tk()  
        self.root.geometry("600x500")
        self.root.minsize(width=600, height=500)
        self.root.maxsize(width=600, height=500)
        self.root.title("Login Page")
        self.root.configure(background="black")  # Set black background

        content_frame = Frame(self.root, bg="black")
        content_frame.pack(side=TOP, pady=50, padx=100)

        # Login text
        login_label = Label(content_frame, text='Log in!', font=("Helvetica", 20, "bold"), bg="black", fg="white")
        login_label.grid(column=0, row=0, columnspan=2, pady=50, padx=90)

        # Username label and input
        username_text = Label(content_frame, text="Username:", font="Helvetica 10", bg="black", fg="white")
        username_text.grid(column=0, row=1, padx=0)

        self.username = StringVar()
        self.username_entry = Entry(content_frame, width=25, font=("Arial", 10), bd=1, highlightthickness=1, highlightbackground="white", relief="flat", textvariable=self.username, fg="white", bg="black", insertbackground='white')
        self.username_entry.grid(column=1, row=1, padx=10)

        # Password label and input
        password_text = Label(content_frame, text="Password:", font="Helvetica 10", bg="black", fg="white")
        password_text.grid(column=0, row=3, pady=10, padx=1)

        self.password = StringVar()
        self.password_entry = Entry(content_frame, width=25, font=("Arial", 10), bd=1, highlightthickness=1, highlightbackground="white", relief="flat", show="*", textvariable=self.password, fg="white", bg="black", insertbackground='white')
        self.password_entry.grid(column=1, row=3, pady=10, padx=0)

        # Login button
        button1 = Button(content_frame, text="            Login              ", relief="flat", bg="white", fg="black", font="Helvetica 10", command=self.clicked)
        button1.grid(column=0, row=5, columnspan=2, pady=10)

        # Button hover effect
        def on_enter(e):
            button1['bg'] = "#333"
            button1['fg'] = "white"

        def on_leave(e):
            button1['bg'] = "white"
            button1['fg'] = "black"

        button1.bind("<Enter>", on_enter)
        button1.bind("<Leave>", on_leave)

        # Register button
        button2 = Button(content_frame, text="          Register            ", relief="flat", bg="white", fg="black", font="Helvetica 10", command=self.open_register_page)
        button2.grid(column=0, row=7, columnspan=2, pady=10)

        # Button hover effect
        def on_enter(e):
            button2['bg'] = "#333"
            button2['fg'] = "white"

        def on_leave(e):
            button2['bg'] = "white"
            button2['fg'] = "black"

        button2.bind("<Enter>", on_enter)
        button2.bind("<Leave>", on_leave)

        # Show password checkbox
        show = Checkbutton(content_frame, text="Show password", relief="flat", bg="black", fg="white", command=self.show_password, selectcolor="black")
        show.grid(column=0, row=4, columnspan=2, pady=10)

        self.root.mainloop()

    def clicked(self):
        global user_name
        u_name = str(self.username.get())
        p_word = str(self.password.get())

        boolean = self.verify(u_name, p_word)
        if boolean:
            user_name = u_name
            self.root.destroy()
        else:
            messagebox.showerror("Error occurred", "Invalid username / password!")

        self.username.set('')
        self.password.set('')


    def show_password(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show="*")

    def verify(self, name, pword):
        global type_of_login
        try:
            with open("files/login_credentials.csv") as fp:
                data = reader(fp)
                for i in data:
                    if i == '':
                        continue
                    if str(i[0]) == name and str(i[1]) == pword:
                        type_of_login = i[2]
                        return True
                    
        except Exception as e:
            messagebox.showerror("Error occurred", "Some error occurred while trying to login!")
            print(e)
            type_of_login = None
            return False
        
        type_of_login = None    
        return False

    def open_register_page(self):
        self.root.destroy()
        register_page_class()



class register_page_class:
    def __init__(self):
        self.root = Tk()  
        self.root.geometry("500x400")
        self.root.minsize(width=500, height=400)
        self.root.maxsize(width=500, height=400)
        self.root.title("Registration Page")
        self.root.configure(background="black")  # Set black background

        content_frame = Frame(self.root, bg="black")
        content_frame.pack(side=TOP, pady=50, padx=100)

        # Login text
        login_label = Label(content_frame, text='Register!', font=("Helvetica", 20, "bold"), bg="black", fg="white")
        login_label.grid(column=0, row=0, columnspan=2, pady=50, padx=90)

        # Username label and input
        username_text = Label(content_frame, text="Username:", font="Helvetica 10", bg="black", fg="white")
        username_text.grid(column=0, row=1, padx=0)

        self.username = StringVar()
        self.username_entry = Entry(content_frame, width=25, font=("Arial", 10), bd=1, highlightthickness=1, highlightbackground="white", relief="flat", textvariable=self.username, fg="white", bg="black", insertbackground='white')
        self.username_entry.grid(column=1, row=1, padx=10)

        # Password label and input
        password_text = Label(content_frame, text="Password:", font="Helvetica 10", bg="black", fg="white")
        password_text.grid(column=0, row=3, pady=10, padx=1)

        self.password = StringVar()
        self.password_entry = Entry(content_frame, width=25, font=("Arial", 10), bd=1, highlightthickness=1, highlightbackground="white", relief="flat", show="*", textvariable=self.password, fg="white", bg="black", insertbackground='white')
        self.password_entry.grid(column=1, row=3, pady=10, padx=0)

        #  register button
        button = Button(content_frame, text="         Register          ", relief="flat", bg="white", fg="black", command=self.register)
        button.grid(column=0, row=5, columnspan=2, pady=10)

        # Button hover effect
        def on_enter(e):
            button['bg'] = "#333"
            button['fg'] = "white"

        def on_leave(e):
            button['bg'] = "white"
            button['fg'] = "black"

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

        # Show password checkbox
        show = Checkbutton(content_frame, text="Show password", relief="flat", bg="black", fg="white", command=self.show_password, selectcolor="black")
        show.grid(column=0, row=4, columnspan=2, pady=10)

        self.root.mainloop()

    def register(self):
        u_name = str(self.username.get())
        p_word = str(self.password.get())

        try:
            with open("files/login_credentials.csv", "a", newline = '') as fp:
                csv_fp = writer(fp)
                data = [u_name, p_word, "customer"]
                csv_fp.writerow(data)

                fp.flush()
                messagebox.showinfo("User Registration", "Registration Successful!")
                self.root.destroy()

                login_register_class()
        except Exception as e:
            messagebox.showerror("Error occurred", "Some error occurred while trying to login!")
            print(e)
            self.username.set('')
            self.password.set('')
        

    def show_password(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show="*")

if __name__ == "__main__":
    login_type = login_register_class()
    # The type of login would be accessible after the window closes
    try:
        print("Login Type:", type_of_login)
    except Exception as e:
        print("don't close the window before logging in....")
        print(e)
    
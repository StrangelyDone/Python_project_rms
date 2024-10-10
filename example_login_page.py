from tkinter import *


def clicked():
    print(u.get(), p.get())
    u.set('')
    p.set('')

def show_password():
    if password.cget("show") == "*":
        password.config(show = '')
    else:
        password.config(show = "*")


root = Tk()
root.geometry("800x600")
root.title("Login Page")

#my trial of setting a background image...(this doesn't work).. idk why
'''img = PhotoImage(file = "img.png")
bg_image = Label(root, image = img)
bg_image.pack(side = TOP)'''

content_frame = Frame(root, bg = "#ffffff")
content_frame.pack(side = TOP, pady = 50, padx = 100)

#Login text
login_label = Label(content_frame, text = 'Log in!', font = ("Helvatica", 20, "bold"), bg = "#ffffff")
login_label.grid(column = 0, row = 0, columnspan = 2, pady = 50, padx = 75)


#username stuff
username_text = Label(content_frame, text = "Username:", font = "Helvatica 10", bg = "#ffffff")
username_text.grid(column = 0, row = 1, padx = 10)

u = StringVar()
username = Entry(content_frame, width=30, font=("Arial", 10), bd = 1, highlightthickness=1, highlightbackground="#ddd", relief = "flat", textvariable = u)
    #think about some way to highlight the borders of the entry box
username.grid(column = 1, row = 1, padx = 5)


#password stuff
password_text = Label(content_frame, text = "Password:", font = "Helvatica 10", bg = "#ffffff")
password_text.grid(column = 0, row = 3, pady = 10, padx = 10)

p = StringVar()
password = Entry(content_frame, width=30, font=("Arial", 10), bd = 1, highlightthickness=1, highlightbackground="#ddd", relief = "flat", show = "*", textvariable = p)
password.grid(column = 1, row = 3, pady = 10, padx = 5)


#login button
button = Button(content_frame, text = "            Login            ", relief = "flat", bg = "#20a384", command = clicked)
button.grid(column = 0, row = 5, columnspan = 2, pady = 10)

    #Button hover effect and understand this actually!!!!!
def on_enter(e):
    button['bg'] = "#10af70"

def on_leave(e):
    button['bg'] = "#20a384"

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)


#hide password stuff and check button
show = Checkbutton(content_frame, text = "Show password", relief = "flat", bd = 1, highlightthickness = 1, highlightbackground = "#ddd", bg = "#ffffff", command = show_password)
show.grid(column = 0, row = 4, columnspan = 2, pady = 10)



root.mainloop()


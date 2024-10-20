import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
import Menu_Management
import order_management
from Payment_option import trigger 

Username = "User1"

class mine:

    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Customer/Admin")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')

        #figure some way to know the row span of a device so it works nicely! 
        self.row_length = 2

        image_path=PhotoImage(master = self.root, file='images/open page 1 Large.png')
        bg_image=tk.Label(self.root, image=image_path)
        bg_image.pack()

        self.button1 = tk.Button(self.root , text="Menu", font=('Courier New Bold', 18), height=2, fg='black', command=self.menu, relief="flat", bg="white")
        self.button1.pack(padx=20, pady=20)

        self.button2 = tk.Button(self.root , text="Order History", font=('Times New Roman Bold', 18), height=2, fg='black', command=self.view_orders, relief="flat", bg="white")
        self.button2.pack(padx=20, pady=20)

        def on_enter(e):
            self.button1['bg'] = "#333"
            self.button1['fg'] = "white"

        def on_leave(e):
            self.button1['bg'] = "white"
            self.button1['fg'] = "black"

        self.button1.bind("<Enter>", on_enter)
        self.button1.bind("<Leave>", on_leave)

        def on_enter(e):
            self.button2['bg'] = "#333"
            self.button2['fg'] = "white"

        def on_leave(e):
            self.button2['bg'] = "white"
            self.button2['fg'] = "black"

        self.button2.bind("<Enter>", on_enter)
        self.button2.bind("<Leave>", on_leave)

        self.root.mainloop()

    def go_back(self):
        self.root.destroy()
        self.__init__()

    def view_orders(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.title("Order Management")
        self.root.configure(bg="black")
        self.root.geometry("800x600")
        
        # Top Frame
        self.top_frame = tk.Frame(self.root, bg='black')
        self.top_frame.pack(fill='x', padx=10, pady=10)

        self.title = tk.Label(self.top_frame, text="Orders", font=("Courier New Bold", 24), bg="black", fg="white")
        self.title.pack(side='top', padx=10)

        # Table Frame
        self.table_frame = tk.Frame(self.root, bg="black")
        self.table_frame.pack(fill="both", expand=True)

        self.style = ttk.Style()
        self.style.theme_use("default")

        self.style.configure("Treeview", background="black", foreground="white", fieldbackground="black", rowheight=40)

        self.style.configure("Treeview.Heading", background="black", foreground="white", font=("Courier New Bold", 12))
        
        self.tree = ttk.Treeview(self.table_frame, columns=("Customer", "Items", "Total"), show="headings")
        self.tree.heading("Customer", text="Customer Name")
        self.tree.heading("Items", text="Items")
        self.tree.heading("Total", text="Total Cost")

        self.tree.column("Customer", anchor="center", width=150)
        self.tree.column("Items", anchor="center", width=280)
        self.tree.column("Total", anchor="center", width=100)

        self.tree.pack(fill="both", expand=True, padx = 10)

        # Button Frame (for view and mark complete (no refresh here!))
        self.button_frame = tk.Frame(self.root, bg="black")
        self.button_frame.pack(fill="x", pady=10)

        self.view_button = tk.Button(self.button_frame, text="View Details", font=("Arial", 14), bg="white", fg="black", command=self.view_details)
        self.view_button.pack(side="right", padx=20)

        self.back_button = tk.Button(self.button_frame, text="Back", font=("Arial", 14), bg="white", fg="black", command=self.go_back)
        self.back_button.pack(side="left", padx=20)

        self.load_data()

    def load_data(self):
    
        cart = order_management.Cart_class()
        orders = cart.order_reader_user(Username)
        #print(orders)

        for order in orders:
            self.tree.insert("", "end", values=order)

    def view_details(self):
        selected_order = self.tree.selection()
        if selected_order:
            order_data = self.tree.item(selected_order, "values")
            temp = tk.Tk()
            temp.geometry("800x200")
            temp.config(bg="black")

            text_frame = tk.Frame(temp, bg = "black")
            text_frame.pack(padx = 20, pady = 20)
            orders_display = tk.Text(text_frame, font=('Arial', 18), bg='black', fg='white', height=15, width=60, bd=2, relief="ridge")
            orders_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            orders_display.insert(tk.END, f"Customer Name: {order_data[0]}\nItems: {order_data[1]}\nTotal cost: {order_data[2]}\n")

    def menu(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Menu")
        self.root.configure(bg='black')

        self.label = tk.Label(self.root, text="Please explore our delightful selection of starters, meals, and desserts.", font=('Courier New Bold', 22), bg='black', fg='white')
        self.label.pack(padx=20, pady=20)

        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.pack(fill='both', expand=1)

        self.my_canvas = tk.Canvas(self.main_frame, bg='black')
        self.my_canvas.pack(side='left', fill='both', expand=1)

        # Bind the canvas resize event
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Create the second frame inside the canvas
        self.second_frame = tk.Frame(self.my_canvas, bg='black')

        # Add the second frame to the canvas
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # Images and buttons
        self.image_1 = PhotoImage(file='images/starters Small.png')
        self.button_starters = tk.Button(self.second_frame, text="Starters", font=('Arial', 18), image=self.image_1, command=self.starters)
        self.button_starters.grid(row=0, column=0, padx=150, pady=10)
        self.button_starters.image = self.image_1

        self.image_2 = PhotoImage(file='images/meals Small.png')
        self.button_meals = tk.Button(self.second_frame, text="Meals", font=('Arial', 18), image=self.image_2, command=self.meals)
        self.button_meals.grid(row=0, column=2, padx=100, pady=10)
        self.button_meals.image = self.image_2

        self.image_3 = PhotoImage(file='images/desserts Small.png')
        self.button_desserts = tk.Button(self.second_frame, text="Desserts", font=('Arial', 18), image=self.image_3, command=self.desserts)
        self.button_desserts.grid(row=1, column=1, pady = 10)
        self.button_desserts.image = self.image_3

        self.back = tk.Button(self.second_frame, text="back", font=('Arial', 18), command = self.go_back, relief="flat", bg="white", fg="black",)
        self.back.grid(row=2, column=0, pady=10, columnspan=3, sticky= 'sw', padx = 40)

        def on_enter(e):
            self.back['bg'] = "#333"
            self.back['fg'] = "white"

        def on_leave(e):
            self.back['bg'] = "white"
            self.back['fg'] = "black"

        self.back.bind("<Enter>", on_enter)
        self.back.bind("<Leave>", on_leave)

        self.proceed = tk.Button(self.second_frame, text="Proceed", font=('Arial', 18), command = self.customer, relief="flat", bg="white", fg="black",)
        self.proceed.grid(row=2, column=2, pady=10, columnspan=3, sticky= 'se')

        def on_enter(e):
            self.proceed['bg'] = "#333"
            self.proceed['fg'] = "white"

        def on_leave(e):
            self.proceed['bg'] = "white"
            self.proceed['fg'] = "black"

        self.proceed.bind("<Enter>", on_enter)
        self.proceed.bind("<Leave>", on_leave)

        self.root.mainloop()

    def starters(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Starters")
        self.root.configure(bg='black')

        self.check_state = tk.IntVar()
        menu = Menu_Management.Menu_class()
        starters = menu.get_starter_items()
        self.starter_selection = {}

        # Main frame to hold the canvas
        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.pack(fill='both', expand=1)

        # Canvas for scrolling
        self.my_canvas = tk.Canvas(self.main_frame, bg='black')
        self.my_canvas.pack(side='left', fill='both', expand=1)

        # Scrollbar
        self.my_scrollbar = tk.Scrollbar(self.main_frame, orient='vertical', command=self.my_canvas.yview)
        self.my_scrollbar.pack(side='right', fill='y')

        # Configure canvas to work with the scrollbar
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Second frame inside the canvas to hold the checkbuttons
        self.second_frame = tk.Frame(self.my_canvas, bg='black')
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # Add checkbuttons inside the second frame in a grid layout with "self.row_length" images per row (also some how configure it!)
        for i in range(len(starters)):
            var = tk.BooleanVar()
            self.starter_selection[f"{starters[i]}"] = var
            image1 = PhotoImage(file=f'images/{starters[i]}.png')

            # Position checkbuttons in a 3-column grid
            self.check = tk.Checkbutton(self.second_frame, text=f"{starters[i]}", font=('Arial', 16), bg='black', image=image1, variable=var, compound='top')
            self.check.grid(row=i // self.row_length, column=i % self.row_length, padx=10, pady=15)
            self.check.image = image1

        # Back/confirm button
        self.back = tk.Button(self.second_frame, text="Confirm", font=('Arial', 18), command=self.menu, relief="flat", bg="white", fg="black")
        self.back.grid(row=(len(starters) // 3) + 2, column=1, padx=50, pady=10, sticky = 'se')

        def on_enter(e):
            self.back['bg'] = "#333"
            self.back['fg'] = "white"

        def on_leave(e):
            self.back['bg'] = "white"
            self.back['fg'] = "black"

        self.back.bind("<Enter>", on_enter)
        self.back.bind("<Leave>", on_leave)

        self.root.mainloop()

    def meals(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Meals")
        self.root.configure(bg='black')

        self.check_state = tk.IntVar()
        menu = Menu_Management.Menu_class()
        meals = menu.get_meal_items()
        self.meal_selection = {}

        # Main frame to hold the canvas
        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.pack(fill='both', expand=1)

        # Canvas for scrolling
        self.my_canvas = tk.Canvas(self.main_frame, bg='black')
        self.my_canvas.pack(side='left', fill='both', expand=1)

        # Scrollbar
        self.my_scrollbar = tk.Scrollbar(self.main_frame, orient='vertical', command=self.my_canvas.yview)
        self.my_scrollbar.pack(side='right', fill='y')

        # Configure canvas to work with the scrollbar
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Second frame inside the canvas to hold the checkbuttons
        self.second_frame = tk.Frame(self.my_canvas, bg='black')
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # Add checkbuttons inside the second frame in a grid layout with 3 images per row
        for i in range(len(meals)):
            var = tk.IntVar()
            self.meal_selection[f"{meals[i]}"] = var
            image1 = PhotoImage(file=f'images/{meals[i]}.png')

            # Position checkbuttons in a 3-column grid
            self.check = tk.Checkbutton(self.second_frame, text=f"{meals[i]}", font=('Arial', 16), bg='black', image=image1, variable=var, compound='top')
            self.check.grid(row=i // self.row_length, column=i % self.row_length, padx=10, pady=15)
            self.check.image = image1

        # Back button
        self.back = tk.Button(self.second_frame, text="Confirm", font=('Arial', 18), command=self.menu, relief="flat", bg="white", fg="black")
        self.back.grid(row=(len(meals) // 3) + 2, column=0, padx=100, pady=10, columnspan=3)

        def on_enter(e):
            self.back['bg'] = "#333"
            self.back['fg'] = "white"

        def on_leave(e):
            self.back['bg'] = "white"
            self.back['fg'] = "black"

        self.back.bind("<Enter>", on_enter)
        self.back.bind("<Leave>", on_leave)

        self.root.mainloop()

    def desserts(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Desserts")
        self.root.configure(bg='black')

        self.check_state = tk.IntVar()
        menu = Menu_Management.Menu_class()
        desserts = menu.get_dessert_items()
        self.dessert_selection = {}

        # Main frame to hold the canvas
        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.pack(fill='both', expand=1)

        # Canvas for scrolling
        self.my_canvas = tk.Canvas(self.main_frame, bg='black')
        self.my_canvas.pack(side='left', fill='both', expand=1)

        # Scrollbar
        self.my_scrollbar = tk.Scrollbar(self.main_frame, orient='vertical', command=self.my_canvas.yview)
        self.my_scrollbar.pack(side='right', fill='y')

        # Configure canvas to work with the scrollbar
        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Second frame inside the canvas to hold the checkbuttons
        self.second_frame = tk.Frame(self.my_canvas, bg='black')
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # Add checkbuttons inside the second frame in a grid layout with 3 images per row
        for i in range(len(desserts)):
            var = tk.IntVar()
            self.dessert_selection[f"{desserts[i]}"] = var
            image1 = PhotoImage(file=f'images/{desserts[i]}.png')

            # Position checkbuttons in a 3-column grid
            self.check = tk.Checkbutton(self.second_frame, text=f"{desserts[i]}", font=('Arial', 16), bg='black', image=image1, variable=var, compound='top')
            self.check.grid(row=i // self.row_length, column=i % self.row_length, padx=10, pady=15)
            self.check.image = image1

        # Back button
        self.back = tk.Button(self.second_frame, text="Confirm", font=('Arial', 18), command=self.menu, relief="flat", bg="white", fg="black")
        self.back.grid(row=(len(desserts) // 3) + 2, column=0, padx=100, pady=10, columnspan=3)

        def on_enter(e):
            self.back['bg'] = "#333"
            self.back['fg'] = "white"

        def on_leave(e):
            self.back['bg'] = "white"
            self.back['fg'] = "black"

        self.back.bind("<Enter>", on_enter)
        self.back.bind("<Leave>", on_leave)

        self.root.mainloop()


    def customer(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Customer")
        self.root.configure(bg='white')

        top_frame = tk.Frame(self.root, bg = "black")
        top_frame.pack(side = 'top',fill='x')

        self.label = tk.Label(top_frame, text="Select an option", font=('Courier New Bold', 22), bg='black', fg='white')
        self.label.pack(padx=20, pady=20)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=1)

        # Create a canvas but without the scrollbar
        self.my_canvas = tk.Canvas(self.main_frame)
        self.my_canvas.pack(side='left', fill='both', expand=1)

        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Create the second frame inside the canvas
        self.second_frame = tk.Frame(self.my_canvas)

        # Add the second frame to the canvas
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # Images and buttons
        self.image_1 = PhotoImage(file='images/delivery Small.png')
        self.button_delivery = tk.Button(self.second_frame, text="Starters", font=('Arial', 18), image=self.image_1, command=self.address)
        self.button_delivery.grid(row=0, column=0, pady=10, padx= 125)
        self.button_delivery.image = self.image_1

        self.image_2 = PhotoImage(file='images/dine-in Small.png')
        self.button_dine_in = tk.Button(self.second_frame, text="Meals", font=('Arial', 18), image=self.image_2, command=self.booking_tables)
        self.button_dine_in.grid(row=0, column=2, pady=10, padx = 60)
        self.button_dine_in.image = self.image_2

        self.image_3 = PhotoImage(file='images/takeaway Small.png')
        self.button_takeaway = tk.Button(self.second_frame, text="Desserts", font=('Arial', 18), image=self.image_3, command=self.payment)
        self.button_takeaway.grid(row=1, column=1, padx = 30)
        self.button_takeaway.image = self.image_3

        self.root.mainloop()

    def address(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Enter your address")
        self.root.configure(bg='gray')

        self.label = tk.Label(self.root, text="Enter your address", bg='white', fg='black', font=('Courier New Bold', 22))
        self.label.pack(padx=20, pady=20)

        self.image=PhotoImage(file='images/address Medium.png')

        self.button = tk.Button(self.root , image=self.image)
        self.button.pack()
        self.button.image=self.image

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root , text="Proceed to payment", font=('Arial', 16), command=self.payment)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def booking_tables(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Table No")
        #20=2-5(1-5) 3/4-8(6-13) 6-5(14-18) 8/10-2(19-20)

        self.label = tk.Label(self.root, text="Desired no. of diners", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.image=PhotoImage(file='images/tables Medium.png')

        self.button = tk.Button(self.root , image=self.image)
        self.button.pack()
        self.button.image=self.image

        self.buttonframe=tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)

        options=["1","2","3","4","5","6","7"]
        combo_box=ttk.Combobox(self.root,values=options)
        combo_box.pack(pady=10)
        combo_box.current(0)

        self.btn=tk.Button(self.buttonframe,text="Proceed",command=self.payment, relief="flat", bg="white", fg="black")
        self.btn.grid(row=1,column=1,sticky=tk.W+tk.E)

        def on_enter(e):
            self.btn['bg'] = "#333"
            self.btn['fg'] = "white"

        def on_leave(e):
            self.btn['bg'] = "white"
            self.btn['fg'] = "black"

        self.btn.bind("<Enter>", on_enter)
        self.btn.bind("<Leave>", on_leave)

        self.buttonframe.pack()
        self.root.mainloop()

    def adding_orders(obj):
        menu_stuff = Menu_Management.Menu_class()
        starters, meals, desserts = menu_stuff.display()

        cart = order_management.Cart_class()

        try:
            starters_selected = obj.starter_selection
            for i in starters_selected:
                if (starters_selected[i].get()):
                    cart.add(i, starters[i])
        except AttributeError:
            pass

        try:
            meals_selected = obj.meal_selection
            for i in meals_selected:
                if (meals_selected[i].get()):
                    cart.add(i, meals[i])
        except AttributeError:
            pass

        try:
            desserts_selected = obj.dessert_selection
            for i in desserts_selected:
                if (desserts_selected[i].get()):
                    cart.add(i, desserts[i])
        except AttributeError:
            pass

        return cart.checkout(Username)
    
    def payment(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.root.title("Payment")
        self.cost = int(self.adding_orders())

        self.image_path=PhotoImage(file='images/payment image.png')
        self.bg_image=tk.Label(self.root, image=self.image_path)
        self.bg_image.pack()

        self.button = tk.Button(self.root,text=f"pay {self.cost}", font = ("Courier New Bold", 22), relief="flat", bg="white", fg="black",command=self.Trigger)
        self.button.pack(pady=70)

        def on_enter(e):
            self.button['bg'] = "#333"
            self.button['fg'] = "white"

        def on_leave(e):
            self.button['bg'] = "white"
            self.button['fg'] = "black"

        self.button.bind("<Enter>", on_enter)
        self.button.bind("<Leave>", on_leave)

        self.root.mainloop()

    def close_window(self):
        self.root.destroy()
    def Trigger(self):
        trigger(self.root)


if __name__ == "__main__":
    obj = mine()
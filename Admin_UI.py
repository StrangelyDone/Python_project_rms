import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk
import csv
import Menu_Management
import order_management

class admin_UI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Customer/Admin")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')

        self.image_path = PhotoImage(file=r'images/open page 1 Large.png')
        self.bg_image = tk.Label(self.root, image=self.image_path)
        self.bg_image.pack()

        self.button = tk.Button(self.root, text="Admin", font=('Times New Roman Bold', 18), height=2, fg='black', command=self.admin_panel, bg = "white", relief = "flat")
        self.button.pack(padx=20, pady=20)

        def on_enter(e):
            self.button['bg'] = "#333"
            self.button['fg'] = "white"

        def on_leave(e):
            self.button['bg'] = "white"
            self.button['fg'] = "black"

        self.button.bind("<Enter>", on_enter)
        self.button.bind("<Leave>", on_leave)

        self.root.mainloop()

    def self_invoker(self):
        self.root.destroy()
        self.__init__()

    def admin_panel(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Admin Panel")
        self.root.configure(bg='black')

        self.label = tk.Label(self.root, text="Admin Panel", font=('Courier New Bold', 25), bg='black', fg='white')
        self.label.pack(padx=20, pady=20)

        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.pack(fill='both', expand=1)

        # Create a canvas but without the scrollbar
        self.my_canvas = tk.Canvas(self.main_frame, bg='black')
        self.my_canvas.pack(side='left', fill='both', expand=1)

        # Bind the canvas resize event but without scrollbar adjustments
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Create the second frame inside the canvas
        self.second_frame = tk.Frame(self.my_canvas, bg='black')
        # Add the second frame to the canvas
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # Images and buttons
        self.image_1 = PhotoImage(file='images/manage menu.png')
        self.button_manage_menu = tk.Button(self.second_frame, text="Starters", font=('Arial', 18), image=self.image_1, command=self.manage_menu)
        self.button_manage_menu.grid(row=0, column=0, padx=250, pady=100)
        self.button_manage_menu.image = self.image_1

        self.image_2 = PhotoImage(file='images/current orders.png')
        self.button_current_orders = tk.Button(self.second_frame, text="Meals", font=('Arial', 18), image=self.image_2, command=self.view_orders)
        self.button_current_orders.grid(row=0, column=2, padx=120, pady=100)
        self.button_current_orders.image = self.image_2

        self.back = tk.Button(self.second_frame, text="back", font=('Arial', 18), command = self.self_invoker, relief="flat", bg="white", fg="black")
        self.back.grid(row=3, column=0, columnspan=3, sticky= 'sw', padx = 40, pady = 102) #the absolute breaking point for pady

        def on_enter(e):
            self.back['bg'] = "#333"
            self.back['fg'] = "white"

        def on_leave(e):
            self.back['bg'] = "white"
            self.back['fg'] = "black"

        self.back.bind("<Enter>", on_enter)
        self.back.bind("<Leave>", on_leave)

        self.root.mainloop()

    def manage_menu(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Admin Panel")
        self.root.configure(bg='black')

        self.label = tk.Label(self.root, text="Manage Menu", font=('Courier New Bold', 25), bg='black', fg='white')
        self.label.pack(padx=20, pady=20)

        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.pack(fill='both', expand=1)

        # Create a canvas but without the scrollbar
        self.my_canvas = tk.Canvas(self.main_frame, bg='black')
        self.my_canvas.pack(side='left', fill='both', expand=1)

        # Bind the canvas resize event but without scrollbar adjustments
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        # Create the second frame inside the canvas
        self.second_frame = tk.Frame(self.my_canvas, bg='black')
        # Add the second frame to the canvas
        self.my_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # Images and buttons
        self.image_1 = PhotoImage(file='images/add item.png')
        self.add_item_button = tk.Button(self.second_frame, text="Starters", font=('Arial', 18), image=self.image_1, command=self.add_item_window)
        self.add_item_button.grid(row=0, column=0, padx=250, pady=100)
        self.add_item_button.image = self.image_1

        self.image_2 = PhotoImage(file='images/remove item.png')
        self.remove_item_button = tk.Button(self.second_frame, text="Meals", font=('Arial', 18), image=self.image_2, command=self.remove_item_window)
        self.remove_item_button.grid(row=0, column=2, padx=120, pady=100)
        self.remove_item_button.image = self.image_2

        self.back = tk.Button(self.second_frame, text="back", font=('Arial', 18), command = self.admin_panel, relief="flat", bg="white", fg="black")
        self.back.grid(row=3, column=0, columnspan=3, sticky= 'sw', padx = 40, pady = 102) #the absolute breaking point for pady

        def on_enter(e):
            self.back['bg'] = "#333"
            self.back['fg'] = "white"

        def on_leave(e):
            self.back['bg'] = "white"
            self.back['fg'] = "black"

        self.back.bind("<Enter>", on_enter)
        self.back.bind("<Leave>", on_leave)

        self.root.mainloop()

    # Window for adding item
    def add_item_window(self):
        self.add_item_pop_up = tk.Tk()
        self.add_item_pop_up.title("Add Item")
        self.add_item_pop_up.configure(bg='black')
        self.add_item_pop_up.geometry("500x375")
        self.add_item_pop_up.minsize(width=500, height=375)
        self.add_item_pop_up.maxsize(width=500, height=375)

        # Create a frame to center the add item components
        self.add_frame = tk.Frame(self.add_item_pop_up, bg='black')
        self.add_frame.pack(expand=True)

        # Add item title
        self.label = tk.Label(self.add_frame, text="Add New Item", font=('Courier New Bold', 22), bg='black', fg='white')
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        # Menu item input fields
        self.item_label = tk.Label(self.add_frame, text="Item Name:", font=('Arial', 18), bg='black', fg='white')
        self.item_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.item_entry = tk.Entry(self.add_frame, font=('Arial', 18))
        self.item_entry.grid(row=1, column=1, padx=10, pady=10)

        self.item_label = tk.Label(self.add_frame, text="price:", font=('Arial', 18), bg='black', fg='white')
        self.item_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.item_price = tk.Entry(self.add_frame, font=('Arial', 18))
        self.item_price.grid(row=2, column=1, padx=10, pady=10)

        # Dropdown for course selection
        self.course_label = tk.Label(self.add_frame, text="Course:", font=('Arial', 18), bg='black', fg='white')
        self.course_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')

        self.course_var = tk.StringVar(self.add_frame)
        self.course_var.set("Select Course")  # Default value for dropdown

        self.course_dropdown = ttk.Combobox(self.add_frame, textvariable=self.course_var, font=('Arial', 18), state='readonly')
        self.course_dropdown['values'] = ('Starters', 'Meals', 'Desserts')
        self.course_dropdown.grid(row=3, column=1, padx=10, pady=10)


        def add_menu_item():
            item_name = self.item_entry.get()
            item_type = self.course_dropdown.get()
            if self.item_price != '':
                item_price = int(self.item_price.get())
            else:
                messagebox.showerror("Error", "Enter price!")
                return
            
            print(item_type, item_name, item_price)

            menu = Menu_Management.Menu_class()
            if item_name != '':
                menu.add(item_name, item_price, item_type)
                messagebox.showinfo("Success", "Item added to menu successfully!")
            else:
                messagebox.showerror("Error", "Enter item name")

        # Add item button
        self.confirm_add_button = tk.Button(self.add_frame, text="Add Item", font=('Arial', 18), command=add_menu_item, relief = 'flat')
        self.confirm_add_button.grid(row=4, column=0, columnspan=2, pady=10)

        def on_enter(e):
            self.confirm_add_button['bg'] = "#333"
            self.confirm_add_button['fg'] = "white"

        def on_leave(e):
            self.confirm_add_button['bg'] = "white"
            self.confirm_add_button['fg'] = "black"

        self.confirm_add_button.bind("<Enter>", on_enter)
        self.confirm_add_button.bind("<Leave>", on_leave)

       
    # Window for removing item
    def remove_item_window(self):
        self.remove_item_pop_up = tk.Tk()
        self.remove_item_pop_up.title("Remove Item")
        self.remove_item_pop_up.configure(bg='black')
        self.remove_item_pop_up.geometry("500x250")
        self.remove_item_pop_up.minsize(width=500, height=250)
        self.remove_item_pop_up.maxsize(width=500, height=250)

        # Create a frame to center the remove item components
        self.remove_frame = tk.Frame(self.remove_item_pop_up, bg='black')
        self.remove_frame.pack(expand=True)

        # Remove item title
        self.label = tk.Label(self.remove_frame, text="Remove Item", font=('Courier New Bold', 22), bg='black', fg='white')
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        # Item name input field
        self.item_label = tk.Label(self.remove_frame, text="Item Name:", font=('Arial', 18), bg='black', fg='white')
        self.item_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.item_entry = tk.Entry(self.remove_frame, font=('Arial', 18))
        self.item_entry.grid(row=1, column=1, padx=10, pady=10)

        def remove_menu_item():
            item_name = self.item_entry.get().lower()

            menu = Menu_Management.Menu_class()
            a, b, c = menu.display()
            items = a + b + c

            if item_name in items:
                menu.remove(item_name)
                messagebox.showinfo("Success", "Item removed from menu")
            else:
                messagebox.showerror("Error", "Item not in menu!")
        # Remove item button
        self.confirm_remove_button = tk.Button(self.remove_frame, text="Remove Item", font=('Arial', 18), command=remove_menu_item, relief = 'flat')
        self.confirm_remove_button.grid(row=2, column=0, columnspan=2, pady=10)

        def on_enter(e):
            self.confirm_remove_button['bg'] = "#333"
            self.confirm_remove_button['fg'] = "white"

        def on_leave(e):
            self.confirm_remove_button['bg'] = "white"
            self.confirm_remove_button['fg'] = "black"

        self.confirm_remove_button.bind("<Enter>", on_enter)
        self.confirm_remove_button.bind("<Leave>", on_leave)

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

        self.style.configure("Treeview", 
                             background="black",  # Black background for table
                             foreground="white",  # White text in table
                             fieldbackground="black",  # Black background for entry area
                             rowheight=40)  # Row height for multi-line items

        self.style.configure("Treeview.Heading", 
                             background="black",  # Black background for headers
                             foreground="white",  # White text for headers
                             font=("Courier New Bold", 12))  # Header font
        
        # Scrollable Treeview (Order Table)
        self.tree = ttk.Treeview(self.table_frame, columns=("Customer", "Items", "Total", "Status"), show="headings")
        self.tree.heading("Customer", text="Customer Name")
        self.tree.heading("Items", text="Items")
        self.tree.heading("Total", text="Total Cost")
        self.tree.heading("Status", text="Status")

        self.tree.column("Customer", anchor="center", width=150)
        self.tree.column("Items", anchor="center", width=280)
        self.tree.column("Total", anchor="center", width=100)
        self.tree.column("Status", anchor="center", width=100)

        self.tree.pack(fill="both", expand=True, padx = 10)

        # Button Frame (for view and mark complete)
        self.button_frame = tk.Frame(self.root, bg="black")
        self.button_frame.pack(fill="x", pady=10)

        self.view_button = tk.Button(self.button_frame, text="View Details", font=("Arial", 14), bg="white", fg="black", command=self.view_details)
        self.view_button.pack(side="left", padx=20)

        self.mark_button = tk.Button(self.button_frame, text="Mark as Completed", font=("Arial", 14), bg="white", fg="black", command=self.mark_completed)
        self.mark_button.pack(side="right", padx=20)

        #a refresh button
        self.refresh_button = tk.Button(self.button_frame, text="Refresh", font=("Arial", 14), bg="white", fg="black", command=self.refresh)
        self.refresh_button.pack(side="bottom", padx=20)

        self.load_data()

    def refresh(self):
        self.view_orders()

    def load_data(self):
        cart = order_management.Cart_class()
        orders = cart.order_reader()
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
            orders_display.insert(tk.END, f"Customer Name: {order_data[0]}\nItems: {order_data[1]}\nTotal cost: {order_data[2]}\nStatus: {order_data[3]}")

    #order_data's format = customer name, items, total cost, status....
    def mark_completed(self):
        selected_order = self.tree.selection()
        if selected_order:
            order_data = self.tree.item(selected_order, "values")
            cart = order_management.Cart_class()
            cart.mark_as_done(order_data[0], order_data[2])
            

    def close_window(self):
        self.root.destroy()

admin_UI()

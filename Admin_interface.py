import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk
import csv

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
        self.add_item_pop_up.geometry("500x300")
        self.add_item_pop_up.minsize(width=500, height=300)
        self.add_item_pop_up.maxsize(width=500, height=300)

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

        # Dropdown for course selection
        self.course_label = tk.Label(self.add_frame, text="Course:", font=('Arial', 18), bg='black', fg='white')
        self.course_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')

        self.course_var = tk.StringVar(self.add_frame)
        self.course_var.set("Select Course")  # Default value for dropdown

        self.course_dropdown = ttk.Combobox(self.add_frame, textvariable=self.course_var, font=('Arial', 18), state='readonly')
        self.course_dropdown['values'] = ('Starters', 'Meals', 'Desserts')
        self.course_dropdown.grid(row=2, column=1, padx=10, pady=10)

        # Add item button
        self.confirm_add_button = tk.Button(self.add_frame, text="Add Item", font=('Arial', 18), command=self.add_menu_item, relief = 'flat')
        self.confirm_add_button.grid(row=3, column=0, columnspan=2, pady=10)

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

        # Remove item button
        self.confirm_remove_button = tk.Button(self.remove_frame, text="Remove Item", font=('Arial', 18), command=self.remove_menu_item, relief = 'flat')
        self.confirm_remove_button.grid(row=2, column=0, columnspan=2, pady=10)

        def on_enter(e):
            self.confirm_remove_button['bg'] = "#333"
            self.confirm_remove_button['fg'] = "white"

        def on_leave(e):
            self.confirm_remove_button['bg'] = "white"
            self.confirm_remove_button['fg'] = "black"

        self.confirm_remove_button.bind("<Enter>", on_enter)
        self.confirm_remove_button.bind("<Leave>", on_leave)


    def add_menu_item(self):
        item = self.item_entry.get()
        course = self.course_var.get()  # Get the selected course
        if item and course != "Select Course":
            with open('menu.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([item, course])
            messagebox.showinfo("Success", "Item added to the menu.")
        else:
            messagebox.showwarning("Input Error", "Please enter both item name and select a course.")

    def remove_menu_item(self):
        item_to_remove = self.item_entry.get()
        if not item_to_remove:
            messagebox.showwarning("Input Error", "Please enter the item name to remove.")
            return
        
        # Read existing items from menu.csv
        with open('menu.csv', 'r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row[0] != item_to_remove]

        # Write updated menu back to menu.csv
        with open('menu.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        messagebox.showinfo("Success", "Item removed from the menu.")

    def view_orders(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Current Orders")
        self.root.configure(bg='black')

        self.label = tk.Label(self.root, text="Current Orders", font=('Courier New Bold', 22), bg='black', fg='white')
        self.label.pack(padx=20, pady=20)

        # Create a frame to hold the Text widget and Scrollbar
        text_frame = tk.Frame(self.root, bg='black')
        text_frame.pack(pady=20)

        # Add a vertical scrollbar
        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Displaying the orders from CSV
        orders = self.read_orders()
        
        # Add the Text widget and associate it with the scrollbar
        self.orders_display = tk.Text(text_frame, font=('Arial', 18), bg='white', fg='black', height=15, width=60, yscrollcommand=scrollbar.set)
        self.orders_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Configure the scrollbar to work with the Text widget
        scrollbar.config(command=self.orders_display.yview)

        # Insert orders into the Text widget
        if orders:
            for order in orders:
                self.orders_display.insert(tk.END, f"Items: {order[0]}\n")
        else:
            self.orders_display.insert(tk.END, "No current orders.\n")

        # Button to go back
        self.back_button = tk.Button(self.root, text="Back", font=('Arial', 18), command=self.admin_panel)
        self.back_button.pack(pady=10)

        self.root.mainloop()

    def read_orders(self):
        # Reading order records from a CSV file
        orders = []
        try:
            with open('orders_admin.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    orders.append(row)
        except FileNotFoundError:
            messagebox.showerror("Error", "Order file not found.")
        return orders

    def admin_login_redirect(self):
        self.close_window()
        self.admin_login()  # Redirect to login page

    def close_window(self):
        self.root.destroy()

admin_UI()

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

        # Removed the Customer button
        self.button = tk.Button(self.root, text="Admin", font=('Times New Roman Bold', 18), height=2, fg='black', command=self.admin_login)
        self.button.pack(padx=20, pady=20)

        self.root.mainloop()

    def admin_login(self):
        # Create a new login window for admin in fullscreen mode
        self.login_window = tk.Toplevel(self.root)
        self.login_window.title("Admin Login")
        self.login_window.attributes('-fullscreen', True)
        self.login_window.configure(bg='black')

        # Username and password labels and entries
        self.username_label = tk.Label(self.login_window, text="Username:", font=('Arial', 18), bg='black', fg='white')
        self.username_label.pack(pady=10)
        self.username_entry = tk.Entry(self.login_window, font=('Arial', 18))
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(self.login_window, text="Password:", font=('Arial', 18), bg='black', fg='white')
        self.password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.login_window, show="*", font=('Arial', 18))
        self.password_entry.pack(pady=10)

        # Login button
        self.login_button = tk.Button(self.login_window, text="Login", font=('Arial', 18), command=self.check_credentials)
        self.login_button.pack(pady=10)

        # Back button to exit login
        self.back_button = tk.Button(self.login_window, text="Back", font=('Arial', 18), command=self.login_window.destroy)
        self.back_button.pack(pady=10)

    def check_credentials(self):
        # Fetch the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the credentials match
        if username == "admin" and password == "admin":
            messagebox.showinfo("Login Success", "Welcome Admin!")
            self.login_window.destroy()  # Close the login window
            self.admin_panel()  # Open the admin panel
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

    def admin_panel(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Admin Panel")
        self.root.configure(bg='black')

        # Admin panel title
        self.label = tk.Label(self.root, text="Admin Panel", font=('Courier New Bold', 22), bg='black', fg='white')
        self.label.pack(padx=20, pady=20)

        # Button to manage menu
        self.button_manage_menu = tk.Button(self.root, text="Manage Menu", font=('Arial', 18), height=2, command=self.manage_menu)
        self.button_manage_menu.pack(padx=10, pady=10)

        # Button to view current orders
        self.button_view_orders = tk.Button(self.root, text="Current Orders", font=('Arial', 18), height=2, command=self.view_orders)
        self.button_view_orders.pack(padx=10, pady=10)

        # Button to exit admin panel
        self.back_button = tk.Button(self.root, text="Exit Admin Panel", font=('Arial', 18), height=2, command=self.close_window)
        self.back_button.pack(padx=10, pady=10)

        self.root.mainloop()

    def manage_menu(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Manage Menu")
        self.root.configure(bg='black')

        # Admin manage menu title
        self.label = tk.Label(self.root, text="Manage Menu", font=('Courier New Bold', 22), bg='black', fg='white')
        self.label.pack(padx=20, pady=20)

        # Menu item input fields
        self.item_label = tk.Label(self.root, text="Item Name:", font=('Arial', 18), bg='black', fg='white')
        self.item_label.pack(pady=10)
        self.item_entry = tk.Entry(self.root, font=('Arial', 18))
        self.item_entry.pack(pady=10)

        # Dropdown for course selection (Starters, Meals, Desserts)
        self.course_label = tk.Label(self.root, text="Course:", font=('Arial', 18), bg='black', fg='white')
        self.course_label.pack(pady=10)

        self.course_var = tk.StringVar(self.root)
        self.course_var.set("Select Course")  # Default value for dropdown

        self.course_dropdown = ttk.Combobox(self.root, textvariable=self.course_var, font=('Arial', 18), state='readonly')
        self.course_dropdown['values'] = ('Starters', 'Meals', 'Desserts')
        self.course_dropdown.pack(pady=10)

        # Buttons to add/remove items
        self.add_button = tk.Button(self.root, text="Add Item", font=('Arial', 18), command=self.add_menu_item)
        self.add_button.pack(pady=10)

        self.remove_button = tk.Button(self.root, text="Remove Item", font=('Arial', 18), command=self.remove_menu_item)
        self.remove_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back", font=('Arial', 18), command=self.admin_panel)
        self.back_button.pack(pady=10)

        self.root.mainloop()

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

        # Displaying the orders from CSV
        orders = self.read_orders()
        self.orders_display = tk.Text(self.root, font=('Arial', 18), bg='white', fg='black', height=15, width=60)
        self.orders_display.pack(pady=20)

        if orders:
            for order in orders:
                self.orders_display.insert(tk.END, f"Order ID: {order[0]}, Items: {order[2]}, Total: {order[3]}, Status: {order[4]}\n")
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
            with open('orders.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    orders.append(row)
        except FileNotFoundError:
            messagebox.showerror("Error", "Order file not found.")
        return orders

    def close_window(self):
        self.root.destroy()


admin_UI()
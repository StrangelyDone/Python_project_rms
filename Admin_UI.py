import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import csv

class AdminUI:

    def __init__(self):
        self.login_window()

    def login_window(self):
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')

        self.label = tk.Label(self.root, text="Enter Username:", font=('Courier New Bold', 22), bg='black', fg='white')
        self.label.pack(pady=20)

        self.username_entry = tk.Entry(self.root, font=('Arial', 18))
        self.username_entry.pack(pady=10)

        self.label_password = tk.Label(self.root, text="Enter Password:", font=('Courier New Bold', 22), bg='black', fg='white')
        self.label_password.pack(pady=20)

        self.password_entry = tk.Entry(self.root, font=('Arial', 18), show='*')  # Hides password input
        self.password_entry.pack(pady=10)

        self.login_button = tk.Button(self.root, text="Login", font=('Arial', 18), command=self.check_login)
        self.login_button.pack(pady=20)

        self.root.mainloop()

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Check if username and password are correct
        if username == "admin" and password == "admin":
            self.root.destroy()  # Close the login window
            self.admin()  # Open the admin panel
        else:
            messagebox.showinfo("Access Denied", "Invalid username or password.")

    def admin(self):
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

        self.price_label = tk.Label(self.root, text="Price:", font=('Arial', 18), bg='black', fg='white')
        self.price_label.pack(pady=10)
        self.price_entry = tk.Entry(self.root, font=('Arial', 18))
        self.price_entry.pack(pady=10)

        # Buttons to add/remove items
        self.add_button = tk.Button(self.root, text="Add Item", font=('Arial', 18), command=self.add_menu_item)
        self.add_button.pack(pady=10)

        self.remove_button = tk.Button(self.root, text="Remove Item", font=('Arial', 18), command=self.remove_menu_item)
        self.remove_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back", font=('Arial', 18), command=self.admin)
        self.back_button.pack(pady=10)

        self.root.mainloop()

    def add_menu_item(self):
        item = self.item_entry.get()
        price = self.price_entry.get()
        if item and price:
            with open('menu.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([item, price])
            messagebox.showinfo("Success", "Item added to the menu.")
        else:
            messagebox.showwarning("Input Error", "Please enter both item name and price.")

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
        self.back_button = tk.Button(self.root, text="Back", font=('Arial', 18), command=self.admin)
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

AdminUI()

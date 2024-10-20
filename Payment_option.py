import tkinter as tk
from tkinter import messagebox, StringVar

main_window_root = None

def center_window(window, width=600, height=600):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Calculate the position to center the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    
    # Set the window geometry
    window.geometry(f'{width}x{height}+{x}+{y}')

def process_payment():
    # Get input values
    payment_method = StringVar().get()
    if payment_method == "Card Payment":
        card_number =tk.Entry(root, font=('Arial', 16), width=30).get()
        expiry_date =tk.Entry(root, font=('Arial', 16), width=10).get()
        cvv = tk.Entry(root, font=('Arial', 16), width=10, show='*').get()

        # Validate card payment fields
        if not card_number or not expiry_date or not cvv:
            messagebox.showerror("Error", "All fields are required.")
            return

        if not validate_card_number(card_number):
            messagebox.showerror("Error", "Invalid card number.")
            return

        if not validate_expiry(expiry_date):
            messagebox.showerror("Error", "Invalid expiration date format. Use MM/YY.")
            return

        if not validate_cvv(cvv):
            messagebox.showerror("Error", "Invalid CVV.")
            return

    elif payment_method == "UPI":
        upi_id = upi_id_entry.get()
        if not upi_id:
            messagebox.showerror("Error", "UPI ID is required.")
            return

    # If everything is valid
    messagebox.showinfo("Success", f"{payment_method} payment processed successfully!")
    main_window_root.destroy()
    root.destroy()  # Close the payment window

def validate_card_number(card_number):
    # Basic validation for credit card number (length check, numeric check)
    return card_number.isdigit() and len(card_number) in [13, 15, 16]

def validate_expiry(expiry_date):
    # Simple validation for expiration date (MM/YY)
    parts = expiry_date.split('/')
    return len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit() and len(parts[0]) == 2 and len(parts[1]) == 2

def validate_cvv(cvv):
    # Simple validation for CVV (3 or 4 digits)
    return cvv.isdigit() and len(cvv) in [3, 4]

def cancel_payment():
    root.destroy()  # Close the payment window

# Set up the main application window
def trigger(a):
    
    global root ,main_window_root, upi_id_entry
    main_window_root = a
    root=tk.Tk()
    root.title("Payment Interface")
    root.configure(bg='black')

    # Center the window on the screen
    center_window(root)

    # Title Label
    title_label = tk.Label(root, text="Payment Information", font=('Arial', 24), bg='black', fg='white')
    title_label.pack(pady=20)

    # Payment Method Dropdown
    payment_method_var = StringVar(root)
    payment_method_var.set("Select Payment Method")  # Default option

    payment_methods = ["Card Payment", "UPI", "Cash on Delivery"]
    payment_method_label = tk.Label(root, text="Payment Method:", font=('Arial', 16), bg='black', fg='white', relief = "flat")
    payment_method_label.pack(pady=5)

    payment_method_menu = tk.OptionMenu(root, payment_method_var, *payment_methods)
    payment_method_menu.config(font=('Arial', 16))
    payment_method_menu.pack(pady=5)

    # Card Payment Fields
    card_number_label = tk.Label(root, text="Card Number:", font=('Arial', 16), bg='black', fg='white')
    card_number_entry = tk.Entry(root, font=('Arial', 16), width=30)

    expiry_label = tk.Label(root, text="Expiration Date (MM/YY):", font=('Arial', 16), bg='black', fg='white')
    expiry_entry = tk.Entry(root, font=('Arial', 16), width=10)

    cvv_label = tk.Label(root, text="CVV:", font=('Arial', 16), bg='black', fg='white')
    cvv_entry = tk.Entry(root, font=('Arial', 16), width=10, show='*')

    # UPI Field
    upi_id_label = tk.Label(root, text="UPI ID:", font=('Arial', 16), bg='black', fg='white')
    upi_id_entry = tk.Entry(root, font=('Arial', 16), width=30)

    # Function to toggle fields based on payment method
    def toggle_fields(*args):
        selected_method = payment_method_var.get()
        if selected_method == "Card Payment":
            card_number_label.pack(pady=5)
            card_number_entry.pack(pady=5)
            expiry_label.pack(pady=5)
            expiry_entry.pack(pady=5)
            cvv_label.pack(pady=5)
            cvv_entry.pack(pady=5)
            upi_id_label.pack_forget()
            upi_id_entry.pack_forget()
        elif selected_method == "UPI":
            upi_id_label.pack(pady=5)
            upi_id_entry.pack(pady=5)
            card_number_label.pack_forget()
            card_number_entry.pack_forget()
            expiry_label.pack_forget()
            expiry_entry.pack_forget()
            cvv_label.pack_forget()
            cvv_entry.pack_forget()
        else:  # Cash on Delivery
            card_number_label.pack_forget()
            card_number_entry.pack_forget()
            expiry_label.pack_forget()
            expiry_entry.pack_forget()
            cvv_label.pack_forget()
            cvv_entry.pack_forget()
            upi_id_label.pack_forget()
            upi_id_entry.pack_forget()

    # Bind the dropdown selection to the toggle_fields function
    payment_method_var.trace("w", toggle_fields)

    # Payment Button
    pay_button = tk.Button(root, text="Pay Now", font=('Arial', 18), command=process_payment, relief="flat", bg="white", fg="black")
    pay_button.pack(pady=20)

    def on_enter(e):
        pay_button['bg'] = "#333"
        pay_button['fg'] = "white"

    def on_leave(e):
        pay_button['bg'] = "white"
        pay_button['fg'] = "black"

    pay_button.bind("<Enter>", on_enter)
    pay_button.bind("<Leave>", on_leave)

    # Cancel Button
    cancel_button = tk.Button(root, text="Cancel", font=('Arial', 18), command=cancel_payment, relief="flat", bg="white", fg="black")
    cancel_button.pack(pady=5)

    def on_enter(e):
        cancel_button['bg'] = "#333"
        cancel_button['fg'] = "white"

    def on_leave(e):
        cancel_button['bg'] = "white"
        cancel_button['fg'] = "black"

    cancel_button.bind("<Enter>", on_enter)
    cancel_button.bind("<Leave>", on_leave)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    rt = tk.Tk()
    trigger(rt)

    
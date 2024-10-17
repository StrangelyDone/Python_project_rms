import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter.scrolledtext import ScrolledText
import Menu_Management
class mine:

    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Customer/Admin")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.row_length = 4

        self.image_path=PhotoImage(file='images/open page 1 Large.png')
        self.bg_image=tk.Label(self.root, image=self.image_path)
        self.bg_image.pack()

        self.button = tk.Button(self.root , text="Customer", font=('Courier New Bold', 18), height=2, fg='black', command=self.menu)
        self.button.pack(padx=20, pady=20)

        self.button = tk.Button(self.root , text="Admin", font=('Times New Roman Bold', 18), height=2, fg='black', command=exit)
        self.button.pack(padx=20, pady=20)

        self.root.mainloop()

    def menu(self):
        self.close_window()
        self.root=tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Menu")
        self.root.configure(bg='black')

        self.label = tk.Label(self.root, text="Please explore our delightful selection of starters, meals, and desserts.", font=('Courier New Bold', 22), bg='black', fg='white')
        self.label.pack(padx=20, pady=20)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill='both', expand=1)

        self.my_canvas=tk.Canvas(self.main_frame)
        self.my_canvas.pack(side='left', fill='both', expand=1)

        self.my_scrollbar=tk.Scrollbar(self.main_frame, orient='vertical', command=self.my_canvas.yview)
        self.my_scrollbar.pack(side='right', fill='y')

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

        self.second_frame = tk.Frame(self.my_canvas)

        self.my_canvas.create_window((0,0), window=self.second_frame, anchor="nw")

        self.image_1=PhotoImage(file='images/starters Small.png')
        
        self.button_starters = tk.Button(self.second_frame , text="Starters", font=('Arial', 18), image=self.image_1, command=self.starters)
        self.button_starters.grid(row=0, column=0, padx=100)
        self.button_starters.image=self.image_1

        self.image_2=PhotoImage(file='images/meals Small.png')

        self.button_meals = tk.Button(self.second_frame , text="Meals", font=('Arial', 18),image=self.image_2, command=self.meals)
        self.button_meals.grid(row=0, column=2, padx=100)
        self.button_meals.image=self.image_2

        self.image_3=PhotoImage(file='images/desserts Small.png')

        self.button_desserts = tk.Button(self.second_frame , text="Desserts", font=('Arial', 18),image=self.image_3, command=self.desserts)
        self.button_desserts.grid(row=1, column=1)
        self.button_desserts.image=self.image_3

        #self.buttonframe.pack(fill='x')

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
        variables = {}

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
        for i in range(len(starters)):
            var = tk.IntVar()
            variables[f"{starters[i]}"] = var
            image1 = PhotoImage(file=f'images/{starters[i]}.png')

            # Position checkbuttons in a 3-column grid
            self.check = tk.Checkbutton(self.second_frame, text=f"{starters[i]}", font=('Arial', 16), bg='black', image=image1, variable=var, compound='top')
            self.check.grid(row=i // self.row_length, column=i % self.row_length, padx=10, pady=15)
            self.check.image = image1

        # Confirm selected dishes checkbutton (placed below the grid)
        self.check = tk.Checkbutton(self.second_frame, text="Confirm selected dishes", font=('Arial', 16), bg='black', fg='white', variable=self.check_state)
        self.check.grid(row=(len(starters) // 3) + 1, column=0, pady=20, columnspan=3)

        # Back button
        self.back = tk.Button(self.second_frame, text="Go back", font=('Arial', 18), command=self.menu)
        self.back.grid(row=(len(starters) // 3) + 2, column=0, padx=100, pady=10, columnspan=3)

        # Proceed button
        self.proceed = tk.Button(self.second_frame, text="Proceed", font=('Arial', 18))
        self.proceed.grid(row=(len(starters) // 3) + 3, column=0, padx=100, pady=10, columnspan=3)

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
        variables = {}

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
            variables[f"{meals[i]}"] = var
            image1 = PhotoImage(file=f'images/{meals[i]}.png')

            # Position checkbuttons in a 3-column grid
            self.check = tk.Checkbutton(self.second_frame, text=f"{meals[i]}", font=('Arial', 16), bg='black', image=image1, variable=var, compound='top')
            self.check.grid(row=i // self.row_length, column=i % self.row_length, padx=10, pady=15)
            self.check.image = image1

        # Confirm selected dishes checkbutton (placed below the grid)
        self.check = tk.Checkbutton(self.second_frame, text="Confirm selected dishes", font=('Arial', 16), bg='black', fg='white', variable=self.check_state)
        self.check.grid(row=(len(meals) // 3) + 1, column=0, pady=20, columnspan=3)

        # Back button
        self.back = tk.Button(self.second_frame, text="Go back", font=('Arial', 18), command=self.menu)
        self.back.grid(row=(len(meals) // 3) + 2, column=0, padx=100, pady=10, columnspan=3)

        # Proceed button
        self.proceed = tk.Button(self.second_frame, text="Proceed", font=('Arial', 18))
        self.proceed.grid(row=(len(meals) // 3) + 3, column=0, padx=100, pady=10, columnspan=3)

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
        variables = {}

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
            variables[f"{desserts[i]}"] = var
            image1 = PhotoImage(file=f'images/{desserts[i]}.png')

            # Position checkbuttons in a 3-column grid
            self.check = tk.Checkbutton(self.second_frame, text=f"{desserts[i]}", font=('Arial', 16), bg='black', image=image1, variable=var, compound='top')
            self.check.grid(row=i // self.row_length, column=i % self.row_length, padx=10, pady=15)
            self.check.image = image1

        # Confirm selected dishes checkbutton (placed below the grid)
        self.check = tk.Checkbutton(self.second_frame, text="Confirm selected dishes", font=('Arial', 16), bg='black', fg='white', variable=self.check_state)
        self.check.grid(row=(len(desserts) // 3) + 1, column=0, pady=20, columnspan=3)

        # Back button
        self.back = tk.Button(self.second_frame, text="Go back", font=('Arial', 18), command=self.menu)
        self.back.grid(row=(len(desserts) // 3) + 2, column=0, padx=100, pady=10, columnspan=3)

        # Proceed button
        self.proceed = tk.Button(self.second_frame, text="Proceed", font=('Arial', 18))
        self.proceed.grid(row=(len(desserts) // 3) + 3, column=0, padx=100, pady=10, columnspan=3)

        self.root.mainloop()


    def customer(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Customer")
        self.root.configure(bg='white')

        self.image_1=PhotoImage(file='images/takeaway Small.png')
        
        self.button_takeaway = tk.Button(self.root , text="Take away", font=('Arial', 18), image=self.image_1, command=exit)
        self.button_takeaway.pack()
        self.button_takeaway.image=self.image_1

        self.image_2=PhotoImage(file='images/dine-in Small.png')

        self.button_dine = tk.Button(self.root , text="Dine in", font=('Arial', 18),image=self.image_2, command=self.booking_tables)
        self.button_dine.pack()
        self.button_dine.image=self.image_2

        self.image_3=PhotoImage(file='images/delivery Small.png')

        self.button_delivery = tk.Button(self.root , text="Delivery", font=('Arial', 18),image=self.image_3, command=self.address)
        self.button_delivery.pack()
        self.button_delivery.image=self.image_3

        self.root.mainloop()

    def address(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Enter your address")
        self.root.configure(bg='white')

        self.label = tk.Label(self.root, text="Enter your address", bg='white', fg='black', font=('Courier New Bold', 22))
        self.label.pack(padx=20, pady=20)

        self.image=PhotoImage(file='images/address Medium.png')

        self.button = tk.Button(self.root , image=self.image)
        self.button.pack()
        self.button.image=self.image

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.button = tk.Button(self.root , text="Proceed to payment", font=('Arial', 16), command=exit)
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

        self.btn1=tk.Button(self.buttonframe, text="2", font=('Arial', 18), command=exit)
        self.btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.btn2=tk.Button(self.buttonframe, text="3-4", font=('Arial', 18), command=exit)
        self.btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

        self.btn3=tk.Button(self.buttonframe, text="6-5", font=('Arial', 18), command=exit)
        self.btn3.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.btn4=tk.Button(self.buttonframe, text="8-10", font=('Arial', 18), command=exit)
        self.btn4.grid(row=1, column=1, sticky=tk.W+tk.E)

        self.buttonframe.pack()

        self.root.mainloop()

    #def cost(self):
        #self.cost=print("Your meal comes to a total of")

    """def payment(self):
        self.close_window
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='white')
        self.root.title("Payment")

        self.button = tk.Button(self.root, text=self.cost, font = ("Courier New Bold", 22), bg='white')
        self.button.pack(pady=70)

        self.root.mainloop()"""

    """def admin(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Admin")
        
        self.button = tk.Button(self.root , text="Manage Menu", font=('Arial', 18), command=exit)
        self.button.pack(padx=10, pady=10)

        self.button = tk.Button(self.root , text="Order Status", font=('Arial', 18), command=exit)
        self.button.pack(padx=10, pady=10)

        self.button = tk.Button(self.root , text="Tables/Staff", font=('Arial', 18), command=exit)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()"""

    def close_window(self):
        self.root.destroy()


mine()
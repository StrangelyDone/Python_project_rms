import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter.scrolledtext import ScrolledText

class mine:

    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Customer/Admin")
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')

        self.image_path=PhotoImage(file=r'/Users/brindap/Downloads/open page 1 Large.png')
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

        #starters-5    meals-6   desserts-5
        """
        Starters:
        Veg Manchuria,70       Chicken Manchuria,100
        Fruit Salad,50          Vegetable Salad,30             Fruit Custard,50

        Meals:
        Chicken Dum Biryani,300      Pudhina Rice,170           Prawns Biryani,400
        Veg Thali,700                Curd Rice,100              Plain Rice,80

        Desserts:
        Hazel Nutella Brownie,96    Chocolate Ball,30      Choco Walnut Brownie,60
        Choco Chip Brownie,60        Choco Chip Cake,540"""

        self.image_1=PhotoImage(file=r'/Users/brindap/Downloads/starters Small.png')
        
        self.button_starters = tk.Button(self.second_frame , text="Starters", font=('Arial', 18), image=self.image_1, command=self.starters)
        self.button_starters.grid(row=0, column=0, padx=100)
        self.button_starters.image=self.image_1

        self.image_2=PhotoImage(file=r'/Users/brindap/Downloads/meals Small.png')

        self.button_meals = tk.Button(self.second_frame , text="Meals", font=('Arial', 18),image=self.image_2, command=self.meals)
        self.button_meals.grid(row=0, column=2, padx=100)
        self.button_meals.image=self.image_2

        self.image_3=PhotoImage(file=r'/Users/brindap/Downloads/desserts Small.png')

        self.button_desserts = tk.Button(self.second_frame , text="Desserts", font=('Arial', 18),image=self.image_3, command=self.desserts)
        self.button_desserts.grid(row=1, column=1)
        self.button_desserts.image=self.image_3

        self.buttonframe.pack(fill='x')

        self.root.mainloop()

    def starters(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Starters")
        self.root.configure(bg='black')
        
        self.check_state_1 = tk.IntVar()
        self.check_state_2= tk.IntVar()
        self.check_state_3 = tk.IntVar()
        self.check_state_4 = tk.IntVar()
        self.check_state_5 = tk.IntVar()
        self.check_state_6 = tk.IntVar()

        self.image_1=PhotoImage(file=r'/Users/brindap/Downloads/Veg Manchuria Small.png')

        self.check_1 = tk.Checkbutton(self.root, text="Veg Manchuria 70", font=('Arial', 16), bg='black', image=self.image_1, variable=self.check_state_1)
        self.check_1.grid(row=0, column=0, padx=45, pady=40)
        self.check_1.image=self.image_1

        self.image_2=PhotoImage(file=r'/Users/brindap/Downloads/Chicken Manchuria Small.png')

        self.check = tk.Checkbutton(self.root, text="Chicken Manchuria 100", font=('Arial', 16), bg='black', image=self.image_2, variable=self.check_state_2)
        self.check.grid(row=0, column=1, padx=30, pady=40)
        self.check.image=self.image_2

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Fruit Salad Small.png')

        self.check = tk.Checkbutton(self.root, text="Fruit Salad 50", font=('Arial', 16), bg='black', image=self.image, variable=self.check_state_3)
        self.check.grid(row=0, column=2, padx=45, pady=40)
        self.check.image=self.image

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Vegetable Salad Small.png')

        self.check = tk.Checkbutton(self.root, text="Vegetable Salad 30", font=('Arial', 16), bg='black', image=self.image, variable=self.check_state_4)
        self.check.grid(row=1, column=0, padx=90)
        self.check.image=self.image

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Fruit custard Small.png')

        self.check = tk.Checkbutton(self.root, text="Fruit Custard 50", font=('Arial', 16), bg='black', image=self.image, variable=self.check_state_5)
        self.check.grid(row=1, column=1, padx=90)
        self.check.image=self.image

        self.check = tk.Checkbutton(self.root, text="Confirm selected dishes", font=('Arial', 16), bg='black', fg='white', variable=self.check_state_6)
        self.check.grid( pady=20)

        self.back = tk.Button(self.root , text="Go back", font=('Arial', 18), command=self.menu)
        self.back.grid(padx=100, pady=10)

        self.proceed = tk.Button(self.root , text="Proceed", font=('Arial', 18), command=self.customer)
        self.proceed.grid( padx=100, pady=10)


        self.root.mainloop()

    def meals(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Starters")
        self.root.configure(bg='black')
        
        self.check_state_1 = tk.IntVar()
        self.check_state_2= tk.IntVar()
        self.check_state_3 = tk.IntVar()
        self.check_state_4 = tk.IntVar()
        self.check_state_5 = tk.IntVar()
        self.check_state_6= tk.IntVar()
        self.check_state_7=tk.IntVar()

        self.image_1=PhotoImage(file=r'/Users/brindap/Downloads/Chicken Dum Biriyani Small.png')

        self.check_1 = tk.Checkbutton(self.root, text="Chicken Dum Biriyani 300", font=('Arial', 16), bg='black', image=self.image_1, variable=self.check_state_1)
        self.check_1.grid(row=0, column=0, padx=45, pady=30)
        self.check_1.image=self.image_1

        self.image_2=PhotoImage(file=r'/Users/brindap/Downloads/Pudina rice Small.png')

        self.check = tk.Checkbutton(self.root, text="Pudhina Rice 170", font=('Arial', 16), bg='black', image=self.image_2, variable=self.check_state_2)
        self.check.grid(row=0, column=1, padx=30, pady=30)
        self.check.image=self.image_2

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Prawns biriyani Small.png')

        self.check = tk.Checkbutton(self.root, text="Prawns Biryani,400", font=('Arial', 16), bg='black', image=self.image, variable=self.check_state_3)
        self.check.grid(row=0, column=2, padx=45, pady=30)
        self.check.image=self.image

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Veg Thali Small.png')

        self.check = tk.Checkbutton(self.root, text="Veg Thali,700", font=('Arial', 16), bg='black', image=self.image, variable=self.check_state_4)
        self.check.grid(row=1, column=0, padx=45, pady=20)
        self.check.image=self.image

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Curd rice Small.png')

        self.check = tk.Checkbutton(self.root, text="Curd Rice,100", font=('Arial', 16), bg='black', image=self.image, variable=self.check_state_5)
        self.check.grid(row=1, column=1, padx=30, pady=20)
        self.check.image=self.image

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Plain rice Small.png')

        self.check = tk.Checkbutton(self.root, text="Plain Rice,80", font=('Arial', 16), bg='black', image=self.image, variable=self.check_state_6)
        self.check.grid(row=1, column=2, padx=45, pady=20)
        self.check.image=self.image

        self.check = tk.Checkbutton(self.root, text="Confirm selected dishes", font=('Arial', 16), bg='black', fg='white', variable=self.check_state_7)
        self.check.grid( pady=20)

        self.back = tk.Button(self.root , text="Go back", font=('Arial', 18), command=self.menu)
        self.back.grid(padx=100, pady=10)

        self.proceed = tk.Button(self.root , text="Proceed", font=('Arial', 18), command=self.customer)
        self.proceed.grid( padx=100, pady=10)

        self.root.mainloop()

    def desserts(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Starters")
        self.root.configure(bg='black')
        
        self.check_state_1 = tk.IntVar()
        self.check_state_2= tk.IntVar()
        self.check_state_3 = tk.IntVar()
        self.check_state_4 = tk.IntVar()
        self.check_state_5 = tk.IntVar()
        self.check_state_6 = tk.IntVar()

        self.image_1=PhotoImage(file=r'/Users/brindap/Downloads/Hazel Nutella Brownie Small.png')

        self.check_1 = tk.Checkbutton(self.root, text="Hazel Nutella Brownie,96", font=('Arial', 16), bg='black', image=self.image_1, variable=self.check_state_1)
        self.check_1.grid(row=0, column=0, padx=45, pady=30)
        self.check_1.image=self.image_1

        self.image_2=PhotoImage(file=r'/Users/brindap/Downloads/Chocolate Ball Small.png')

        self.check = tk.Checkbutton(self.root, text="Chocolate Ball,30", font=('Arial', 16), bg='black', image=self.image_2, variable=self.check_state_2)
        self.check.grid(row=0, column=1, padx=30, pady=30)
        self.check.image=self.image_2

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Choco Walnut Brownie Small.png')

        self.check = tk.Checkbutton(self.root, text="Choco Walnut Brownie,60", font=('Arial', 16), bg='black', image=self.image, variable=self.check_state_3)
        self.check.grid(row=0, column=2, padx=45, pady=30)
        self.check.image=self.image

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Choco Chip Brownie Small.png')

        self.check = tk.Checkbutton(self.root, text="Choco Chip Brownie,60", font=('Arial', 16), bg='black', image=self.image, variable=self.check_state_4)
        self.check.grid(row=1, column=0, padx=90, pady=20)
        self.check.image=self.image

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/Choco Chip Cake Small.png')

        self.check = tk.Checkbutton(self.root, text="Choco Chip Cake,540", font=('Arial', 16), bg='black', image=self.image, variable=self.check_state_5)
        self.check.grid(row=1, column=1, padx=90, pady=20)
        self.check.image=self.image

        self.check = tk.Checkbutton(self.root, text="Confirm selected dishes", font=('Arial', 16), bg='black', fg='white', variable=self.check_state_6)
        self.check.grid( pady=20)

        self.back = tk.Button(self.root , text="Go back", font=('Arial', 18), command=self.menu)
        self.back.grid(padx=100, pady=10)

        self.proceed = tk.Button(self.root , text="Proceed", font=('Arial', 18), command=self.customer)
        self.proceed.grid( padx=100, pady=10)


        self.root.mainloop()


    def customer(self):
        self.close_window()
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.title("Customer")
        self.root.configure(bg='white')

        self.image_1=PhotoImage(file=r'/Users/brindap/Downloads/takeaway Small.png')
        
        self.button_takeaway = tk.Button(self.root , text="Take away", font=('Arial', 18), image=self.image_1, command=exit)
        self.button_takeaway.pack()
        self.button_takeaway.image=self.image_1

        self.image_2=PhotoImage(file=r'/Users/brindap/Downloads/dine-in Small.png')

        self.button_dine = tk.Button(self.root , text="Dine in", font=('Arial', 18),image=self.image_2, command=self.booking_tables)
        self.button_dine.pack()
        self.button_dine.image=self.image_2

        self.image_3=PhotoImage(file=r'/Users/brindap/Downloads/delivery Small.png')

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

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/address Medium.png')

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

        self.image=PhotoImage(file=r'/Users/brindap/Downloads/tables Medium.png')

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
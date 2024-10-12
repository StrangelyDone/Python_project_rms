import csv 

class Menu :
    def __init__(self,fn='Menu.csv'):
        self.filename=fn
    def add(self,item,price,category):
        with open(self.filename,mode='a', newline='') as file:
            writer=csv.writer(file)
            writer.writerow([item,str(price),category])
    def remove(self,item):
        rows=[]
        with open(self.filename,mode='r') as file:
            reader=csv.reader(file)
            rows=[row for row in reader if row != item]
        with open(self.filename,mode='w',newline='') as file:
            writer=csv.writer(file)
            writer.writerows(rows)
    def display(self):
        starters=[]
        meals=[]
        desserts=[]
        with open(self.filename,mode='r') as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                if row[2] =="Starters":
                    starters.append(row)
                elif row[2] =="Meals":
                    meals.append(row)
                elif row[2] =="Desserts":
                    desserts.append(row)
        print("\n STARTERS")
        for x in starters:
            print(f"Item: {x[0]}, Price:  {x[1]}")
        print("\n MEALS")
        for y in meals:
            print(f"Item:  {y[0]}, Price:  {y[1]}")
        print("\n DESSERT")
        for z in desserts:
            print(f"Item: {z[0]}, Price:  {z[1]}")

if __name__ == "__main__":

    menu=Menu()
    menu.display()

    
    menu.remove(["Veg Manchuria", "70", "Starters"])

    menu.display()
    
    menu.remove(["Chicken Manchuria","100","Starters"])
    menu.remove(["Fruit Salad","50","Starters"])
    menu.remove(["Vegetable Salad","30","Starters"])
    menu.remove(["Fruit Custard","50","Starters"])
    menu.remove(["Chicken Dum Biryani","300","Meals"])
    menu.remove(["Pudhina Rice","170","Meals"])
    menu.remove(["Prawns Biryani","400","Meals"])
    menu.remove(["Veg Thali","700","Meals"])
    menu.remove(["Curd Rice","100","Meals"])
    menu.remove(["Plain Rice","80","Meals"])
    menu.remove(["Hazel Nutella Brownie","96","Desserts"])
    menu.remove(["Chocolate Ball","30","Desserts"])
    menu.remove(["Choco Walnut Brownie","60","Desserts"])
    menu.remove(["Choco Chip Brownie","60","Desserts"])
    menu.remove(["Choco Chip Cake","540","Desserts"])

    menu.display()
    
    menu.add("Veg Manchuria","70","Starters")
    menu.add("Chicken Manchuria","100","Starters")
    menu.add("Fruit Salad","50","Starters")
    menu.add("Vegetable Salad","30","Starters")
    menu.add("Fruit Custard","50","Starters")
    menu.add("Chicken Dum Biryani","300","Meals")
    menu.add("Pudhina Rice","170","Meals")
    menu.add("Prawns Biryani","400","Meals")
    menu.add("Veg Thali","700","Meals")
    menu.add("Curd Rice","100","Meals")
    menu.add("Plain Rice","80","Meals")
    menu.add("Hazel Nutella Brownie","96","Desserts")
    menu.add("Chocolate Ball","30","Desserts")
    menu.add("Choco Walnut Brownie","60","Desserts")
    menu.add("Choco Chip Brownie","60","Desserts")
    menu.add("Choco Chip Cake","540","Desserts")

    menu.display()

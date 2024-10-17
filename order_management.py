from csv import *

#the format for adding items is: "itemname,price"

class Cart_class:
    def __init__(self):
        self.items = []

    def add(self, item, price):
        self.items.append([item, price])

    def checkout(self):
        sum = 0
        for i in self.items:
            sum += i[1]

        with open("orders_user.csv", "a", newline= '') as fp:
            csv_fp = writer(fp)
    #each order of the user is seperated by this header as it gets added for every order (a complete coincidence lol)
            csv_fp.writerow(["item name", "price"])
    #assuming the above criteria for item is followed(line 3)
            csv_fp.writerows(self.items)


        with open("orders_admin.csv", "a", newline= '') as fp:
            csv_fp = writer(fp)
    #same motivation in adding the header row again and again! 
            csv_fp.writerow(["item name", "price"])
            csv_fp.writerows(self.items)

        return sum

           
if __name__ == "__main__":

    #the format for adding items is: "itemname,price,qty"
    cart1 = Cart_class()
    cart1.add("pho", 450)
    cart1.checkout()

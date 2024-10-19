from csv import *

#the format for adding items is: "itemname,price"

class Cart_class:
    def __init__(self):
        self.items = []

    def add(self, item, price):
        self.items.append([item, price])

    def checkout(self, user_name):
        sum = 0
        for i in self.items:
            sum += i[1]

        with open(f"{user_name}_orders.csv", "a", newline= '') as fp:
            csv_fp = writer(fp, delimiter=';')
            item = ''
            for i in self.items:
                item += (i[0] + ',')
            data = [item, sum]
    #each order of the user is seperated by this header as it gets added for every order (a complete coincidence lol)
            csv_fp.writerow(["item name", "price"])
    #assuming the above criteria for item is followed(line 3)
            csv_fp.writerow(data)


        with open("orders_admin.csv", "a", newline= '', ) as fp:
            csv_fp = writer(fp, delimiter=';')
    #same motivation in adding the header row again and again! 
            csv_fp.writerow(["user name", "items", "price", "status"])
            item = ''
            for i in self.items:
                item += (i[0] + ',')
            data = [user_name, item, sum, "pending"]
            
            csv_fp.writerow(data)

        return sum
                    

    #format for each thing in orders: customer, items, total, status
    #csv format: items, price, username, status
    def order_reader(self):
        orders = []
        with open("orders_admin.csv") as fp:
            csv_fp = reader(fp, delimiter=';')
            for i in csv_fp:
                if i[0] != "user name":
                    orders.append(i)
        return orders

           
if __name__ == "__main__":

    #the format for adding items is: "itemname,price,qty"
    cart1 = Cart_class()
    cart1.add("pho", 450)
    cart1.checkout()

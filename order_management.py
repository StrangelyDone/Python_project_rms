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

        with open(f"files/{user_name}_orders.csv", "a", newline= '') as fp:
            csv_fp = writer(fp, delimiter=';')
            item = ''
            for i in self.items:
                item += (i[0] + ',')
            data = [user_name, item, sum]
    #each order of the user is seperated by this header as it gets added for every order (a complete coincidence lol)
            csv_fp.writerow(["user name", "items", "price"])
    #assuming the above criteria for item is followed(line 3)
            csv_fp.writerow(data)


        with open("files/orders_admin.csv", "a", newline= '', ) as fp:
            csv_fp = writer(fp, delimiter=';')
    #same motivation in adding the header row again and again! 
            csv_fp.writerow(["user name", "items", "price", "status"])
            item = ''
            for i in self.items:
                item += (i[0] + ',')
            data = [user_name, item, sum, "pending"]
            
            csv_fp.writerow(data)

        return sum
                    

    #format for each thing in orders(the nested list below): customer, items, total, status
    def order_reader(self):
        orders = []
        with open("files/orders_admin.csv") as fp:
            csv_fp = reader(fp, delimiter=';')
            for i in csv_fp:
                if i == '':
                    continue
                try:
                    if i[0] != "user name":
                        orders.append(i)
                except IndexError:
                    pass
        return orders

    def order_reader_user(self, user_name):
        orders = []
        try:
            with open(f"files/{user_name}_orders.csv") as fp:
                csv_fp = reader(fp, delimiter=';')
                for i in csv_fp:
                    if i == '':
                        continue
                    if i[0] != "user name":
                        orders.append(i)
            return orders
        except FileNotFoundError:
            return ["no currernt orders", "no currernt orders", "no currernt orders", "no currernt orders"]
    
    def mark_as_done(self, user_name, price):
        orders = []
        with open("files/orders_admin.csv") as fp:
            csv_fp_reader = reader(fp, delimiter=';')
            for i in csv_fp_reader:
                if i == '':
                    continue
                if i[0] == user_name and i[2] == str(price):
                    i[3] = "completed"
                    orders.append(i)
                else:
                    orders.append(i)

        with open("files/orders_admin.csv", 'w', newline = '') as fp:
            csv_fp_writer = writer(fp, delimiter=';')
            csv_fp_writer.writerows(orders)

           
if __name__ == "__main__":

    username = "test123"
    cart1 = Cart_class()
    cart1.add("pho", 450)
    cart1.checkout(username)

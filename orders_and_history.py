from csv import *

#the format for adding items is: "itemname,price,qty"

class Cart:
    def __init__(self, username):
        self.username = username
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def checkout(self):
        with open(f"{self.username}_order_history.csv", "a") as fp:
            csv_fp = writer(fp)
            csv_fp.writerow(["item name", "price", "qty"])

    #assuming the above criteria for item is followed(line 3)
            data = []
            for i in self.items:
                data.append(i.split(','))
            csv_fp.writerows(data)

        with open("admin_orders.csv", "a") as fp:
            csv_fp = writer(fp)
            csv_fp.writerow(["item name", "price", "qty", "username"])

            for i in data:
                i.append(self.username)

            csv_fp.writerows(data)

           
if __name__ == "__main__":
    cart1 = Cart("user1")
    cart1.add("pho, 450, 1")
    cart1.checkout()

import login_register_pages
import Customer_UI
import Admin_UI

login_obj = login_register_pages.login_register_class()
name = login_register_pages.type_of_login

if name == 'customer':
    Customer_UI.Username = login_register_pages.user_name
    customer_obj = Customer_UI.mine()

elif name == 'admin':
    admin_obj = Admin_UI.admin_UI()

    
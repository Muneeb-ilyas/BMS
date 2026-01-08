menu_data = {
    "Chocolate Bars": [
        {"name": "Lotus Biscoff Bar", "prices": {"Small": 1500, "Medium": 3000, "Large": 4500, "Two-Bites Box": 2400}},
        {"name": "Pistachios Knafeh Bar", "prices": {"Small": 1500, "Medium": 3000, "Large": 4500, "Two-Bites Box": 2400}},
        {"name": "Salted Caramel Bar", "prices": {"Small": 1500, "Medium": 3000, "Large": 4500, "Two-Bites Box": 2400}},
        {"name": "Peanut Butter Bar", "prices": {"Small": 1500, "Medium": 3000, "Large": 4500, "Two-Bites Box": 2400}},
        {"name": "Cookie Crumble Bar", "prices": {"Small": 1500, "Medium": 3000, "Large": 4500, "Two-Bites Box": 2400}},
    ],
    "Brownies": [
        {"name": "Belgian Brownie", "prices": {"Standard": 400}},
        {"name": "Nutella Salted Caramel Brownie", "prices": {"Standard": 540}},
        {"name": "Fudge Caramel Brownie", "prices": {"Standard": 540}},
        {"name": "Lotus Fudge Brownie", "prices": {"Standard": 540}},
    ],
    "Cookies (Levain Style)": [
        {"name": "Caramel Waffle Cookie", "prices": {"Small": 450, "Large": 550}},
        {"name": "Lotus Stuffed Cookie", "prices": {"Small": 450, "Large": 550}},
        {"name": "Redvelvet Cookie", "prices": {"Small": 450, "Large": 550}},
        {"name": "Chocolate Chunk Cookie", "prices": {"Small": 450, "Large": 550}},
        {"name": "Triple Chocolate Nutella Cookie", "prices": {"Small": 450, "Large": 550}},
        {"name": "Purple S'mores Cookie", "prices": {"Small": 450, "Large": 550}},
        {"name": "Peanut Butter Chocolate Cookie", "prices": {"Small": 450, "Large": 550}},
    ],
    "Gluten & Sugar Free": [
        {"name": "Double Chocolate Cookies", "prices": {"Standard": 550}},
        {"name": "Chocolate Chunk Cookies", "prices": {"Standard": 550}},
        {"name": "Apple Crumble Cheese Cake", "prices": {"Slice": 950, "Brownie size": 650}},
        {"name": "Banana Bread", "prices": {"Large (9 inch)": 2500, "Small (6 inch)": 1500}},
        {"name": "Granola Trail Mix", "prices": {"Standard": 1800, "With Dark Choc": 2000}},
        {"name": "Brookies", "prices": {"Batch of 6": 5400}},
    ],
    "Novelty Special": [
        {"name": "Matilda Cake Slice", "prices": {"One slice": 1500}},
        {"name": "Pistachios Milk Cake Serving", "prices": {"2 persons": 1800}},
        {"name": "Viral Pistachio Knafeh Fudge Cake", "prices": {"Standard": 1800}},
        {"name": "Pistachios Tiramisu", "prices": {"Standard": 1800}},
    ],
    "Customized Cake 🎂": []
}

cart = []
file_cart = "cart.txt"
file_order = "orders.txt"
import os
import datetime
def get_new_id():
    if os.path.exists(file_order) == False:
        return 101
    
    last_id = 100
    try:
        f = open(file_order, "r")
        lines = f.readlines()
        f.close()
        
        for line in lines:
            if "Order ID:" in line:
                parts = line.split(":")
                id_part = parts[1]
                last_id = int(id_part.strip())
    except:
        pass
        
    return last_id + 1

def save_cart_data():
    f = open(file_cart, "w")
    for item in cart:
        line = item['item'] + "|" + item['details'] + "|" + str(item['qty']) + "|" + str(item['total']) + "\n"
        f.write(line)
    f.close()

def load_cart_data():
    if os.path.exists(file_cart) == False:
        return

    try:
        f = open(file_cart, "r")
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 4:
                temp = {}
                temp["item"] = parts[0]
                temp["details"] = parts[1]
                temp["qty"] = int(parts[2])
                temp["total"] = int(parts[3])
                cart.append(temp)
        f.close()
    except:
        print("Error loading cart")

def save_order(total_bill, name):
    new_id = get_new_id()
    current_time = datetime.datetime.now()
    time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    f = open(file_order, "a")
    f.write("\n==============================\n")
    f.write("Order ID: " + str(new_id) + "\n")
    f.write("Customer: " + name + "\n")
    f.write("Time: " + time_str + "\n")
    f.write("------------------------------\n")
    
    for item in cart:
        line = item['item'] + " (" + item['details'] + ") x" + str(item['qty']) + " = Rs " + str(item['total']) + "\n"
        f.write(line)
        
    f.write("------------------------------\n")
    f.write("TOTAL BILL: Rs " + str(total_bill) + "\n")
    f.write("==============================\n")
    f.close()
    
    return new_id

def show_menu_cats():
    print("\n--- WHAT WOULD YOU LIKE TO ORDER? ---")
    
    cats = []
    for k in menu_data:
        cats.append(k)
    
    count = 1
    for c in cats:
        print(str(count) + ". " + c)
        count = count + 1
        
    print(str(count) + ". View Cart")
    print(str(count + 1) + ". Edit Cart (Remove Item)")
    print(str(count + 2) + ". Checkout & Exit")
    
    return cats

def pick_item(category_name):
    items_list = menu_data[category_name]
    
    count = 1
    for itm in items_list:
        prices_dict = itm['prices']
        first_price = 0
        for p in prices_dict:
            first_price = prices_dict[p]
            break 
        
        print(str(count) + ". " + itm['name'] + " (from Rs " + str(first_price) + ")")
        count = count + 1
            
    try:
        user_input = input("Select Item (0 to back): ")
        choice = int(user_input)
        
        if choice > 0 and choice <= len(items_list):
            return items_list[choice-1]
    except:
        print("Please enter number only.")
        
    return None

def pick_size(item_dict):
    price_dict = item_dict['prices']
    size_list = []
    
    for s in price_dict:
        size_list.append(s)
        
    count = 1
    for s in size_list:
        print(str(count) + ". " + s + " - Rs " + str(price_dict[s]))
        count = count + 1
        
    try:
        user_input = input("Select Size: ")
        choice = int(user_input)
        
        if choice > 0 and choice <= len(size_list):
            selected_size = size_list[choice-1]
            final_price = price_dict[selected_size]
            return selected_size, final_price
    except:
        pass
        
    return None, None

def make_custom_cake():
    print("\n--- CUSTOMIZED CAKE ---")

    print("Available Sizes: ['1 pound', '2 pound', '3 pound']")
    size = input("Size: ").lower().strip() 
    
    price = 0
    if size == "1 pound":
        price = 1000
    elif size == "2 pound":
        price = 2000
    elif size == "3 pound":
        price = 3000
    else:
        print("Invalid size! Please choose from available sizes.")
        return

    valid_shapes = ['Circle', 'Square', 'Heart']
    shape = input("Shape ['Circle', 'Square', 'Heart']: ").strip().title()
    
    if shape not in valid_shapes:
        print(f"Invalid Shape! Please choose exactly: {valid_shapes}")
        return

    valid_flavors = ['Vanilla', 'Chocolate', 'Strawberry']
    flavor = input("Flavor ['Vanilla', 'Chocolate', 'Strawberry']: ").strip().title()
    
    if flavor not in valid_flavors:
        print(f"Invalid Flavor! Please choose exactly: {valid_flavors}")
        return
    
    try:
        q_input = input("Quantity: ")
        qty = int(q_input)
        if qty <= 0:
            print("Quantity must be positive")
            return
            
        new_item = {}
        new_item["item"] = "Customized Cake"
        new_item["details"] = f"{size}, {shape}, {flavor}" 
        new_item["qty"] = qty
        new_item["total"] = price * qty
        
        cart.append(new_item)
        save_cart_data()
        print("Ok! Customized Cake added.")
        
    except:
        print("Invalid quantity. Please enter a number.")

def show_my_cart():
    if len(cart) == 0:
        print("Cart is empty.")
        return
        
    grand_total = 0
    print("\n--- YOUR CART ---")
    
    count = 1
    for x in cart:
        print(str(count) + ". " + x['item'] + " (" + x['details'] + ") x" + str(x['qty']) + " = Rs " + str(x['total']))
        grand_total = grand_total + x['total']
        count = count + 1
        
    print("TOTAL: Rs " + str(grand_total))

def edit_my_cart():
    if len(cart) == 0:
        print("Cart is empty. Nothing to edit.")
        return

    print("\n--- REMOVE ITEM FROM CART ---")
    
    count = 1
    for x in cart:
        print(str(count) + ". " + x['item'] + " (" + x['details'] + ") - Qty: " + str(x['qty']))
        count = count + 1
        
    print("0. Back")
    
    try:
        num = int(input("Enter item number to REMOVE: "))
        
        if num == 0:
            return
            
        if num > 0 and num <= len(cart):
            index = num - 1
            
            removed_item = cart.pop(index)
            save_cart_data()
            
            print(" Removed: " + removed_item['item'])
        else:
            print("Invalid number.")
            
    except:
        print("Invalid Input")

def do_checkout():
    if len(cart) == 0:
        print("Cart is empty! Nothing to checkout.")
        return

    final_total = 0
    for x in cart:
        final_total = final_total + x['total']

    print("\nFINAL BILL")
    print("==============================")
    for x in cart:
        print(x['item'] + " (" + x['details'] + ") x" + str(x['qty']) + " = Rs " + str(x['total']))
    print("TOTAL PAYABLE: Rs " + str(final_total))
    
    c_name = input("\nEnter Customer Name: ")
    o_id = save_order(final_total, c_name)
    
    print("\n Order #" + str(o_id) + " saved successfully! Thank you " + c_name + ".")
    
    cart.clear()
    if os.path.exists(file_cart):
        os.remove(file_cart)

def main_program():
    load_cart_data()
    print("Welcome to Novelty By Khadija Iqbal")

    while True:
        cat_list = show_menu_cats()
        
        try:
            choice_str = input("\nEnter choice: ")
            
            if choice_str.isdigit() == False:
                print("X Please enter a valid number.")
                continue
                
            choice = int(choice_str)
            total_options = len(cat_list)

            if choice == total_options + 1:
                show_my_cart()

            elif choice == total_options + 2:
                edit_my_cart()

            elif choice == total_options + 3:
                do_checkout()
                break 

            elif choice >= 1 and choice <= total_options:
                selected_cat = cat_list[choice-1]
                
                if selected_cat == "Customized Cake 🎂":
                    make_custom_cake()
                else:
                    selected_item = pick_item(selected_cat)
                    
                    if selected_item != None:
                        s, p = pick_size(selected_item)
                        
                        if p != None:
                            try:
                                q_val = int(input("Quantity: "))
                                if q_val > 0:
                                    order_item = {}
                                    order_item["item"] = selected_item['name']
                                    order_item["details"] = s
                                    order_item["qty"] = q_val
                                    order_item["total"] = p * q_val
                                    
                                    cart.append(order_item)
                                    save_cart_data()
                                    print("Added to cart!")
                                else:
                                    print("Quantity must be more than 0")
                            except:
                                print("Invalid Quantity.")
                        else:
                            print("Selection cancelled.")
            else:
                print("Invalid Option.")
        except Exception as e:
            print("Something went wrong.")
            print(e)


main_program()

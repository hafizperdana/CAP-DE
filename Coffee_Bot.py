orders = []
def coffee_orders():
    def cust_order():
        welcome_message()
        placing_orders(orders)
        receipt(orders)

        name = input("\nPlease input your name: ")

        print("\nThanks, {}! Please complete the payment and take your order at the pick up counter!".format(name))

    def welcome_message():
        print("Welcome to the CeleratesCoffeeShop!")

    def error_message():
        print("\nPlease enter the corresponding letter for your response.")

    def placing_orders(orders):
        size = get_size()
        temp_type = get_temp()
        addons = get_addons()
        pastries = get_pastries()
        quantity = get_quantity()
        size_calc = 0.00
        if size == "Small":
            size_calc += 2.00
        elif size == "Medium":
            size_calc += 3.00
        elif size == "Large":
            size_calc += 4.00
        addons_calc = 0.00
        if addons == "with Milk":
            addons_calc += 0.50
        elif addons == "with Sugar":
            addons_calc += 0.25
        elif addons == "with Cream":
            addons_calc += 0.75
        elif addons == "with Whipped Cream":
            addons_calc += 1.00
        pastries_calc = 0.00
        if pastries == "and Muffin":
            pastries_calc += 2.50
        elif pastries == "and Croissant":
            pastries_calc += 3.00
        elif pastries == "and Donut":
            pastries_calc += 1.50
        total = (size_calc + addons_calc + pastries_calc) * quantity
        orders.append([quantity, size, temp_type, addons, pastries, total])
        print("\nAlright, that\'s {} {} {} {} {}!\nTotal: ${}".format(quantity, size, temp_type, addons, pastries, total))
        addorder_prompt()

    def get_size():
        res = input('\nWhat size drink can I get for you? \n[a] Small $2.00\n[b] Medium $3.00\n[c] Large $4.00\n> ')
        res = res.lower()
        if res == "a":
            return "Small"
        elif res == "b":
            return "Medium"
        elif res == "c":
            return "Large"
        else:
            error_message()
            return get_size()
        
    def get_addons():
        res = input("\nWhat kind of add-ons would you like?\n[a] Milk $0.50 \n[b] Sugar $0.25 \n[c] Cream $0.75 \n[d] Whipped Cream $1.00\n> ")
        res = res.lower()
        if res == "a":
            return "with Milk"
        elif res == "b":
            return "with Sugar"
        elif res == "c":
            return "with Cream"
        elif res == "d":
            return "with Whipped Cream"
        else:
            error_message()
            return get_addons()

    def get_temp():
        res = input("\nHow would you like your drink? \n[a] Hot \n[b] Iced \n> ")
        res = res.lower()
        if res == "a":
            return "Hot Coffee"
        elif res == "b":
            return "Iced Coffee"
        else:
            error_message()
            return get_temp()

    def get_pastries():
        res = input("\nWhat patries would you like?\n[a] Muffin $2.50 \n[b] Croissant $3.00 \n[c] Donut $1.50 \n> ")
        res = res.lower()
        if res == "a":
            return "and Muffin"
        elif res == "b":
            return "and Croissant"
        elif res == "c":
            return "and Donut"
        else:
            error_message()
            return get_pastries()

    def get_quantity():
        res = input("\nWhat is quantity for this order? > ")
        try:
            res = int(res)
            return res
        except ValueError:
            print("\nInvalid input. Please enter a value quantity.")
            return get_quantity()

    def addorder_prompt():
        res = input("\nDo you wish to add another order? \n[a] Yes \n[b] No \n> ")
        res = res.lower()
        if res == "a":
            print("\nAlright, taking your new order!")
            return placing_orders(orders)
        elif res == "b":
            print("\nAlright, processing your orders now!")
        else:
            error_message()
            return addorder_prompt()

    def receipt(orders):
        print("\nYou have placed " + str((len(orders))) + " orders. Your orders are: ")
        for order in orders:
            print(*order)
        i = 0
        grand_total = 0
        while i < len(orders):
            grand_total += orders[i][5]
            i+=1
        print("Grand Total: ${}".format(grand_total))

    return cust_order()
coffee_orders()
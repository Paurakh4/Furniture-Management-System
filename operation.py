import read
import write
import messages_display
import datetime

furniture_dict = {}
furniture_id = 1
read.file(furniture_dict, furniture_id)


def order_from_manufacturer():
    messages_display.info()
    Name_of_employee = input("Enter the name of employee: ")

    ordered_furniture = []
    loop = True
    while loop:
        messages_display.table()
        read.file_read()

        try:
            valid_num = int(input("Enter the valid number : "))
            if valid_num <= 0 or valid_num > len(furniture_dict):
                messages_display.invalid_error()
                continue
        except ValueError:
            messages_display.exception()
            continue

        print("Debug: Checking availability for furniture ID " +
              str(valid_num))
        availability = furniture_dict[valid_num][4]
        print("Debug: Current availability status: " + availability)

        try:
            order_quantity = int(input("Enter the quantity to order: "))
            if order_quantity <= 0:
                print("Quantity must be a positive number.")
                continue
        except ValueError:
            print("Invalid input for quantity. Please enter a valid number.")
            continue

        furniture_dict[valid_num][3] = str(
            int(furniture_dict[valid_num][3]) + order_quantity)
        write.value(furniture_dict)

        id_number = int(furniture_dict[valid_num][0])
        manufacturer = str(furniture_dict[valid_num][1])
        product_name = str(furniture_dict[valid_num][2])
        price = int(furniture_dict[valid_num][4])

        ordered_furniture.append(
            [id_number, manufacturer, product_name, order_quantity, price])

        print(" --" * 10)
        ask_user = input("Want to order more furniture? (y/n): ").lower()
        print(" --" * 10)
        if ask_user == 'y':
            continue
        else:
            total_price = 0
            for i in ordered_furniture:
                total_price = total_price + int(i[3]) * int(i[4])
            current_date = datetime.datetime.now()

            print("\n")
            print(" --" * 23)
            print("\t\t\t  Invoice")
            print(" --" * 23)
            print("\t\t    BRJ Furniture Stores")
            print("\t\t gmail:brjfurniture@gmail.com ")
            print("\t\t\t 9876543210")
            print(" Name: " + str(Name_of_employee))
            print(" Date and Time: " + str(current_date))
            print(" --" * 14)
            print(" Details: ")
            print(" --" * 23)
            print(" ID  Manufacturer  Product Name  Quantity  Price")
            print(" --" * 23)
            for i in ordered_furniture:
                print(" ", str(i[0]), "\t", str(i[1]), "\t", str(i[2]), "\t",
                      str(i[3]), "\t", str(i[4]))
            print(" --" * 8)
            print(" Total Amount: Rs." + str(total_price))
            print(" --" * 23)

            write.print_invoice_order(Name_of_employee, ordered_furniture,
                                      total_price)

            loop = False


def sell_to_customer():
    messages_display.info()
    Name_of_customer = input("Enter the name of customer: ")

    sold_furniture = []
    loop = True
    while loop == True:
        messages_display.table()
        read.file_read()

        try:
            valid_num = int(input("Enter the valid number : "))
            if valid_num <= 0 or valid_num > len(furniture_dict):
                messages_display.invalid_error()
                continue
        except ValueError:
            messages_display.exception()
            continue

        try:
            sell_quantity = int(input("Enter the quantity to sell: "))
            if sell_quantity <= 0 or sell_quantity > int(
                    furniture_dict[valid_num][3]):
                print(
                    "Invalid quantity. Please check stock and enter a valid number."
                )
                continue
        except ValueError:
            print("Invalid input for quantity. Please enter a valid number.")
            continue

        furniture_dict[valid_num][3] = str(
            int(furniture_dict[valid_num][3]) - sell_quantity)
        write.value(furniture_dict)

        id_number = int(furniture_dict[valid_num][0])
        manufacturer = str(furniture_dict[valid_num][1])
        product_name = str(furniture_dict[valid_num][2])
        price = int(furniture_dict[valid_num][4])

        sold_furniture.append(
            [id_number, manufacturer, product_name, sell_quantity, price])
        print(" --" * 10)
        ask_user = input("Want to sell more furniture? (y/n)").lower()
        print(" --" * 10)
        if ask_user == 'y':
            loop = True
        else:
            subtotal = 0
            for i in sold_furniture:
                subtotal = subtotal + int(i[3]) * int(i[4])
            current_date = datetime.datetime.now()
            vat = subtotal * 0.13
            shipping_cost = 50
            total_amount = subtotal + vat + shipping_cost

            print("\n")
            print(" --" * 23)
            print("\t\t\t  Invoice")
            print(" --" * 23)
            print("\t\t    BRJ Furniture Stores")
            print("\t\t gmail:brjfurniture@gmail.com ")
            print("\t\t\t 9876543210")
            print(" Name: " + str(Name_of_customer))
            print(" Date and Time: " + str(current_date))
            print(" --" * 14)
            print(" Details: ")
            print(" --" * 23)
            print(" ID  Manufacturer  Product Name  Quantity  Price")
            print(" --" * 23)
            for i in sold_furniture:
                print(" ", str(i[0]), "\t", str(i[1]), "\t", str(i[2]), "\t",
                      str(i[3]), "\t", str(i[4]))
            print(" --" * 8)
            print(" Subtotal: Rs." + str(subtotal))
            print(" VAT (13%): Rs." + str(vat))
            print(" Shipping Cost: Rs." + str(shipping_cost))
            print(" --" * 10)
            print("Total Amount: Rs." + str(total_amount))
            print(" --" * 23)

            write.print_invoice_sale(Name_of_customer, sold_furniture,
                                     subtotal, vat, shipping_cost,
                                     total_amount)

            loop = False


def display_inventory():
    messages_display.table()
    read.file_read()

import datetime


def value(furniture_dict):
    file = open("Furniture.txt", "w")
    for values in furniture_dict.values():
        file.write(
            str(values[0]) + "," + str(values[1]) + "," + str(values[2]) +
            "," + str(values[3]) + "," + str(values[4]))
        file.write("\n")
    file.close()


def print_invoice_order(Name_of_employee, ordered_furniture, total_price):
    current_date = datetime.datetime.now()
    hour = (datetime.datetime.now().hour)
    minute = (datetime.datetime.now().minute)
    second = (datetime.datetime.now().second)
    file = open(
        str(Name_of_employee) + "_" + str(hour) + "-" + str(minute) + "-" +
        str(second) + ".txt", 'w')

    file.write("\n")
    file.write("\n" + " --" * 23)
    file.write("\n\t\t\t  Invoice")
    file.write("\n" + " --" * 23)
    file.write("\n\t\t    BRJ Furniture Stores")
    file.write("\n\t\t gmail:brjfurniture@gmail.com ")
    file.write("\n\t\t\t 9876543210")
    file.write("\n Name: " + str(Name_of_employee))
    file.write("\n Date and Time: " + str(current_date))
    file.write("\n" + " --" * 14)
    file.write("\n Details: ")
    file.write("\n" + " --" * 23)
    file.write("\n ID  Manufacturer  Product Name  Quantity  Price")
    file.write("\n" + " --" * 23)
    for i in ordered_furniture:
        file.write("\n " + str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) +
                   "\t" + str(i[3]) + "\t" + str(i[4]))
    file.write("\n" + " --" * 8)
    file.write("\n Total Amount: Rs." + str(total_price))
    file.write("\n" + " --" * 23)
    file.close()


def print_invoice_sale(Name_of_customer, sold_furniture, subtotal, vat,
                       shipping_cost, total_amount):
    current_date = datetime.datetime.now()
    hour = (datetime.datetime.now().hour)
    minute = (datetime.datetime.now().minute)
    second = (datetime.datetime.now().second)
    file = open(
        str(Name_of_customer) + "_" + str(hour) + "-" + str(minute) + "-" +
        str(second) + ".txt", 'w')

    file.write("\n")
    file.write("\n" + " --" * 23)
    file.write("\n\t\t\t  Invoice")
    file.write("\n" + " --" * 23)
    file.write("\n\t\t    BRJ Furniture Stores")
    file.write("\n\t\t gmail:brjfurniture@gmail.com ")
    file.write("\n\t\t\t 9876543210")
    file.write("\n Name: " + str(Name_of_customer))
    file.write("\n Date and Time: " + str(current_date))
    file.write("\n" + " --" * 14)
    file.write("\n Details: ")
    file.write("\n" + " --" * 23)
    file.write("\n ID  Manufacturer  Product Name  Quantity  Price")
    file.write("\n" + " --" * 23)
    for i in sold_furniture:
        file.write("\n " + str(i[0]) + "\t" + str(i[1]) + "\t" + str(i[2]) +
                   "\t" + str(i[3]) + "\t" + str(i[4]))
    file.write("\n" + " --" * 8)
    file.write("\n Subtotal: Rs." + str(subtotal))
    file.write("\n VAT (13%): Rs." + str(vat))
    file.write("\n Shipping Cost: Rs." + str(shipping_cost))
    file.write("\n Total Amount: Rs." + str(total_amount))
    file.write("\n" + " --" * 23)
    file.close()

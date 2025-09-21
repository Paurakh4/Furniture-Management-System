import messages_display
import operations

# Display welcome message
messages_display.welcome_text()
loop = True
while loop == True:
    # Display menu options
    messages_display.option()
    try:
        user_input = int(input("\n  Enter the option here: "))
    except ValueError:
        messages_display.main()
        continue
    if user_input == 1:
        messages_display.order_furniture()
        operations.order_from_manufacturer()
    if user_input == 2:
        messages_display.sell_furniture()
        operations.sell_to_customer()
    if user_input == 3:
        messages_display.display_inventory()
        operations.display_inventory()
    if user_input != 4:
        print(" ")
    else:
        messages_display.exit()
        loop = False

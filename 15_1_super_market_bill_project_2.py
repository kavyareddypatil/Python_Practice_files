from datetime import datetime
name = input("Enter your name : ").title()
lists = '''
Rice       Rs 20/kg
Sugar      Rs 10/kg
Flour      Rs 30/kg
Green gram Rs 50/kg
Oil        Rs 35/liter
Paneer     Rs 50/kg
'''
price = 0
price_list = []
total_price = 0
final_price = 0
i_list = []
q_list = []
p_list = []

items = {"rice" : 20, "sugar" : 10, "flour" : 30, "green gram" : 50, "oil" : 35, "paneer" : 50}

while True:
    choice = input("Enter your choice (1 for list of items and 2 for exit ): ")
    if choice == "2":
        print("Thank you for shopping.")
        break
    elif choice == "1":
        print(lists)

        while True:
            option = input("Enter  1 for shopping or enter 2 for exit : ")
            if option == "2":
                print("Thank you for shoping.")
                break
            elif option == "1":
                item = input("Enter an Item : ").lower().strip()

                while True:
                    item_quantity = input("Enter item quantity : ")
                    if item_quantity.isdigit():
                        quantity = int(item_quantity)
                        break
                    else:
                        print("Please enter valid quantity.")
                if item in items:
                    price = quantity * items[item]
                    price_list.append((item,quantity,items[item],price))
                    total_price +=price
                    i_list.append(item)
                    q_list.append(quantity)
                    p_list.append(price)
                else:
                    print("Selected item is not available. Sorry for inconvenience.")
        if total_price > 0:
            tax = (total_price * 18) / 100
            final_amount = tax + total_price
            print("=" * 25, "KPN Supermarket","=" * 25)
            print(" " * 28, "Tirupati")
            print("Name : ",name," " * 30, "Date :",datetime.now().date())
            print("-" * 68)
            print("SNO", " " * 8,"Items"," " * 8,"Quantity"," " * 6,"Price"," " * 6)
            for i in range(len(price_list)):
                print(i," " * 10,i_list[i]," " * 8,q_list[i]," "*8,p_list[i]," "*8)
            print("-" * 75)
            print(" " * 50, "Total Amount:", "Rs",total_price)
            print("Tax Amount"," " * 50, "Rs", final_amount)
            print("-" * 75)
            print(" " * 20,"Thank you & visit again")
            print("-" * 75)









def display_menu():
    print("\n--- Hotel Menu ---")
    print("1. Pizza - Rs.12")
    print("2. Burger - Rs.8")
    print("3. Pasta - Rs.10")
    print("4. Salad - Rs.6")
    print("5. Exit")


def take_order():
    menu = {
        1: {"name": "Pizza", "price": 12},
        2: {"name": "Burger", "price": 8},
        3: {"name": "Pasta", "price": 10},
        4: {"name": "Salad", "price": 6}
    }
   
    total_bill = 0  
   
    while True:
        display_menu()  
        try:
            choice = int(input("Enter the item that you want to order (1-5): "))
           
            if choice == 5:
                print(f"Your total bill is: Rs.{total_bill}")
                print("Thank you for ordering! Goodbye!")
                break  
           
            elif choice in menu:
                quantity = int(input(f"How many {menu[choice]['name']}s would you like to order? "))
                item_total = quantity * menu[choice]["price"]
                total_bill += item_total
                print(f"Added {quantity} {menu[choice]['name']}(s) to your order. Total for this item: Rs.{item_total}")
            else:
                print("Invalid choice! Please select a valid menu item.")
       
        except ValueError:
            print("Please enter a valid number.")


def hotel_food_order():
    print("Welcome to the Hotel Food Ordering System!")
    take_order()


hotel_food_order()


output
Welcome to the Hotel Food Ordering System!

--- Hotel Menu ---
1. Pizza - Rs.12
2. Burger - Rs.8
3. Pasta - Rs.10
4. Salad - Rs.6
5. Exit
Enter the item that you want to order (1-5): 1
How many Pizzas would you like to order? 20
Added 20 Pizza(s) to your order. Total for this item: Rs.240

--- Hotel Menu ---
1. Pizza - Rs.12
2. Burger - Rs.8
3. Pasta - Rs.10
4. Salad - Rs.6
5. Exit
Enter the item that you want to order (1-5): 2
How many Burgers would you like to order? 50
Added 50 Burger(s) to your order. Total for this item: Rs.400

--- Hotel Menu ---
1. Pizza - Rs.12
2. Burger - Rs.8
3. Pasta - Rs.10
4. Salad - Rs.6
5. Exit
Enter the item that you want to order (1-5): 3
How many Pastas would you like to order? 2
Added 2 Pasta(s) to your order. Total for this item: Rs.20

--- Hotel Menu ---
1. Pizza - Rs.12
2. Burger - Rs.8
3. Pasta - Rs.10
4. Salad - Rs.6
5. Exit
Enter the item that you want to order (1-5): 4
How many Salads would you like to order? 100
Added 100 Salad(s) to your order. Total for this item: Rs.600

--- Hotel Menu ---
1. Pizza - Rs.12
2. Burger - Rs.8
3. Pasta - Rs.10
4. Salad - Rs.6
5. Exit
Enter the item that you want to order (1-5): 
import os
from helper import Transaction


def show_menu():
    """Show menu"""
    print("1. Check Transaction")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Cancel Purchase")
    print("5. Total Price")
    print("6. Save Transaction")
    print("7. Exit\n")
    choice = input("Enter choice: ")
    if choice == "1":
        os.system('clear')
        transaction.check_order()
        show_menu()
    elif choice == "2":
        os.system('clear')
        print("-" * 60)
        print("Add New Item to Transaction")
        print("-" * 60)
        print("1. Continue Adding Items")
        print("2. Go Back")
        choice = int(input("Enter choice: "))
        if choice == 1:
            os.system('clear')
            print("-" * 60)
            print("Add New Item to Transaction")
            print("-" * 60)
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = int(input("Enter item price: "))
            transaction.add_data(name, quantity, price)
            again = input("Add another item? (y/n): ")
            while again == "y":
                name = input("Enter item name: ")
                quantity = int(input("Enter item quantity: "))
                price = int(input("Enter item price: "))
                transaction.add_data(name, quantity, price)
                again = input("Add another item? (y/n): ")
            os.system('clear')
            transaction.check_order()
            show_menu()
        elif choice == 2:
            show_menu()
    elif choice == "3":
        os.system('clear')
        print("-" * 60)
        print("Modify Item in Transaction")
        print("-" * 60)
        print("1. Continue Editing Items")
        print("2. Go Back")
        choice = int(input("Enter choice: "))
        if choice == 1:
            os.system('clear')
            print("-" * 60)
            print("Modify Item in Transaction")
            print("-" * 60)
            transaction.check_order()
            name = input("Enter item name to modify: ")
            column = input("Enter column to modify: ")
            value = input("Enter new value: ")
            os.system('clear')
            transaction.update_item_column(name, column, value)
            transaction.check_order()
            show_menu()
        elif choice == 2:
            show_menu()
    elif choice == "4":
        os.system('clear')
        print("-" * 60)
        print("Cancel Purchase")
        transaction.check_order()
        print('1. Delete Item')
        print('2. Reset Transaction')
        print('3. Go Back')
        choice = int(input('Enter choice: '))
        if choice == 1:
            os.system('clear')
            print("-" * 60)
            print("Delete Item")
            transaction.check_order()
            item = str(input('Enter item name to delete: '))
            transaction.delete_item(item)
        elif choice == 2:
            os.system('clear')
            transaction.reset_transaction()
        elif choice == 3:
            os.system('clear')
            show_menu()
        else:
            print("Invalid choice")
        show_menu()
    elif choice == "5":
        os.system('clear')
        transaction.total_price()
        show_menu()
    elif choice == "6":
        os.system('clear')
        transaction.save_transaction()
        show_menu()
    elif choice == "7":
        os.system('clear')
        print("Thank you for shopping!")
    else:
        os.system('clear')
        print("Invalid choice\n\n")
        show_menu()


def main():
    """Main function"""
    global transaction
    transaction = Transaction("dimas")
    os.system('clear')
    print("-" * 60)
    print("Welcome to the shopping application!")
    print("-" * 60)
    show_menu()


if __name__ == "__main__":
    main()

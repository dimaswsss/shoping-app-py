import pandas as pd
import os


class Transaction:
    def __init__(self, buyer_name):
        self.buyer_name = buyer_name
        self.df = pd.DataFrame(columns=['name', 'quantity', 'price@quantity'])

    def add_data(self, item_name: str, item_quantity: int, item_price: int):
        try:
            self.df = pd.concat([self.df, pd.DataFrame.from_records([
                {'name': item_name, 'quantity': item_quantity, 'price@quantity': item_price}
            ])], ignore_index=True)
            print("-" * 60)
            print("Item added successfully!")
            print("-" * 60, "\n\n")
            return self.df
        except:
            return "Error! Please check your input!\n\n"

    def update_item_column(self, item_name: str, column_name: str, value):
        print("-" * 60)
        try:
            self.df.loc[self.df['name'] == item_name, column_name] = value
            print("Item updated successfully!")
            return self.df
        except:
            return "Error! Please check your input!"

    def delete_item(self, item_name: str):
        os.system('clear')
        print("-" * 60)
        try:
            self.df.drop(self.df[self.df['name'] == item_name].index, inplace=True)
            print("Item deleted successfully!")
            self.check_order()
            return self.df
        except:
            return "Error! Please check your input!"

    def reset_transaction(self):
        print("-" * 60)
        print("Reset transaction")
        print("-" * 60)
        try:
            self.df.drop(self.df.index, inplace=True)
            print("Transaction reset successfully!")
            print("-" * 60, "\n\n")
            return self.df
        except:
            return "Error!"

    def check_order(self):
        print("-" * 60)
        print("Current transaction")
        print("-" * 60)
        try:
            print(self.df)
            print("-" * 60, "\n\n")
            return self.df
        except:
            return "Error!"

    def total_price(self):
        print("-" * 60)
        print("Total price")
        print("-" * 60)
        print(f"You have {len(self.df)} items in your transaction")
        try:
            total_price = sum(self.df['quantity'] * self.df['price@quantity'])
            if total_price > 500_000:
                total_price *= .90
            elif total_price > 300_000:
                total_price *= .92
            elif total_price > 200_000:
                total_price *= .95
            print(f"Total price: {total_price}")
            print("-" * 60, "\n\n")
            return total_price
        except:
            return "Error!"

    def save_transaction(self):
        print("-" * 60)
        print("Save transaction")
        print("-" * 60)
        try:
            self.df.to_csv(f'{self.buyer_name}.csv', index=False)
            print("Transaction saved successfully!")
            print("-" * 60, "\n\n")
            return self.df
        except:
            return "Error!"


def show_menu():
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
    global transaction
    transaction = Transaction("dimas")
    os.system('clear')
    print("-" * 60)
    print("Welcome to the shopping application!")
    print("-" * 60)
    show_menu()

main()

import pandas as pd
import os


class Transaction:
    def __init__(self, buyer_name):
        self.buyer_name = buyer_name
        self.df = pd.DataFrame(columns=['name', 'quantity', 'price@quantity'])

    def add_data(self, item_name: str, item_quantity: int, item_price: int):
        """Add item data to the transaction"""
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
        """Update a specific column of an item in the transaction"""
        print("-" * 60)
        try:
            self.df.loc[self.df['name'] == item_name, column_name] = value
            print("Item updated successfully!")
            return self.df
        except:
            return "Error! Please check your input!"

    def delete_item(self, item_name: str):
        """Delete an item from the transaction"""
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
        """Reset the entire transaction"""
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
        """Display the current transaction"""
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
        """Calculate and display the total price of the transaction"""
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
        """Save the transaction to a CSV file"""
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

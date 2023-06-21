import pandas as pd
import os


class Transaction:
    def __init__(self, name_buyer):
        self.name_buyer = name_buyer
        self.df = pd.DataFrame(columns=['name', 'quantity', 'price@quantity'])

    def add_data(self, item: str, quantity: int, price: int):
        try:
            self.df = pd.concat([self.df, pd.DataFrame.from_records([
                {'name': item, 'quantity': quantity, 'price@quantity': price}
            ])], ignore_index=True)
            print("-" * 60)
            print("Item added successfully!")
            print("-" * 60, "\n\n")
            return self.df
        except:
            return "Error! Please check your input!\n\n"

    def update_item_column(self, item: str, column: str, value):
        print("-" * 60)
        print("Update item in transaction")
        print("-" * 60)
        try:
            self.df.loc[self.df['name'] == item, column] = value
            print("Item updated successfully!")
            return self.df
        except:
            return "Error! Please check your input!"

    def delete_item(self, item: str):
        os.system('clear')
        print("-" * 60)
        try:
            self.df.drop(self.df[self.df['name'] == item].index, inplace=True)
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
            self.df.to_csv(f'{self.name_buyer}.csv', index=False)
            print("Transaction saved successfully!")
            print("-" * 60, "\n\n")
            return self.df
        except:
            return "Error!"


def pilihan():
    print("1. Cek Transaksi")
    print("2. Tambahkan Barang")
    print("3. Update Barang yang Ingin Dibeli")
    print("4. Batal Membeli")
    print("5. Total Belanjaan")
    print("6. Simpan")
    print("7. Exit\n")
    choice = input("Masukkan pilihan: ")
    if choice == "1":
        os.system('clear')
        transaction.check_order()
        pilihan()
    elif choice == "2":
        os.system('clear')
        print("-" * 60)
        print("Add new item to transaction")
        print("-" * 60)
        print("1. Lanjutkan membeli barang")
        print("2. Kembali")
        choice = int(input("Masukkan pilihan: "))
        if choice == 1:
            os.system('clear')
            print("-" * 60)
            print("Add new item to transaction")
            print("-" * 60)
            name = input("Masukkan nama barang: ")
            quantity = int(input("Masukkan jumlah barang: "))
            price = int(input("Masukkan harga barang: "))
            transaction.add_data(name, quantity, price)
            again = input("Tambahkan barang lagi? (y/n): ")
            while again == "y":
                name = input("Masukkan nama barang: ")
                quantity = int(input("Masukkan jumlah barang: "))
                price = int(input("Masukkan harga barang: "))
                transaction.add_data(name, quantity, price)
                again = input("Tambahkan barang lagi? (y/n): ")
            os.system('clear')
            transaction.check_order()
            pilihan()
        elif choice == 2:
            pilihan()
    elif choice == "3":
        os.system('clear')
        print("-" * 60)
        print("Modify item in transaction")
        print("-" * 60)
        print("1. Lanjutkan edit barang")
        print("2. Kembali")
        choice = int(input("Masukkan pilihan: "))
        if choice == 1:
            os.system('clear')
            print("-" * 60)
            print("Modify item in transaction")
            print("-" * 60)
            transaction.check_order()
            name = input(f"Masukkan nama barang yang ingin diubah: ")
            column = input("Masukkan kolom yang ingin diubah: ")
            value = input(f"Masukkan nilai baru: ")
            transaction.update_item_column(name, column, value)
            transaction.check_order()
            pilihan()
        elif choice == 2:
            pilihan()
    elif choice == "4":
        os.system('clear')
        print("-" * 60)
        print("Batal Membeli")
        transaction.check_order()
        print('1. Hapus barang')
        print('2. Reset transaksi')
        print('3. Kembali')
        choice = int(input('Masukkan pilihan: '))
        if choice == 1:
            os.system('clear')
            print("-" * 60)
            print("Delete Item")
            transaction.check_order()
            item = str(input('Masukkan nama barang yang ingin dihapus: '))
            transaction.delete_item(item)
        elif choice == 2:
            os.system('clear')
            transaction.reset_transaction()
        elif choice == 3:
            os.system('clear')
            pilihan()
        else:
            print("Pilihan tidak tersedia")
        pilihan()
    elif choice == "5":
        os.system('clear')
        transaction.total_price()
        pilihan()
    elif choice == "6":
        os.system('clear')
        transaction.save_transaction()
        pilihan()
    elif choice == "7":
        os.system('clear')
        print("Terima kasih telah berbelanja")
    else:
        os.system('clear')
        print("Pilihan tidak tersedia\n\n")
        pilihan()


def main():
    global transaction
    transaction = Transaction("dimas")
    os.system('clear')
    print("-" * 60)
    print("Selamat datang di aplikasi belanja!")
    print("-" * 60)
    pilihan()

main()

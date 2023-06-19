tmp_item = []


def add_item(name: str, quantity: int, price_per_quantity: int):
    tmp_item.append([name, quantity, price_per_quantity])
    return f"success add item, name: {name}, quantity: {quantity}, price@quantity: {price_per_quantity}"


def update_item(name, new_name):
    for row in tmp_item:
        if row[0] == name:
            row[0] = new_name
    return f"success change name item with name: {name} to {new_name}"


def delete_item(name):
    for row in tmp_item:
        if row[0] == name:
            row.clear()
    return f"success remove item with name: {name}"


def reset_transaction():
    tmp_item.clear()
    return "success clear all transaction"


def check_order():
    for row in tmp_item:
        print(f'{row[0]}  {row[1]}  {row[2]}  {row[1] * row[2]}')
    return 'that\'s all'


print(add_item('mobil', 10, 20_000))
print(add_item('motor', 11, 10_000))
# print(tmp_item)
# print(update_item('mobil', 'car'))
# print(tmp_item)
# print(delete_item('car'))
# print(tmp_item)
# print(reset_transaction())
# print(tmp_item)
print(check_order())


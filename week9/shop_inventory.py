def restock(stock: dict, item: str, qty: int) -> dict:
    new_stock = stock.copy()
    new_stock[item] = new_stock.get(item, 0) + qty
    return new_stock

def sell(stock: dict, item: str, qty: int):
    new_stock = stock.copy()

    if new_stock.get(item, 0) and new_stock[item] >= qty:
        new_stock[item] -= qty
        return new_stock, True

    return new_stock, False

def low_stock(stock: dict, limit: int):
    low_stocks = []

    for item, value in stock.items():
        if value < limit:
            low_stocks.append(item)

    return low_stocks

def total_items(stock: dict) -> int:
    total = 0

    for value in stock.values():
        total += value

    return total

stock = {"rice": 10, "beans": 5}

# print(restock(stock, "gari", 8))    # {"rice": 10, "beans": 5, "gari": 8}
# print(restock(stock, "rice", 5))    # {"rice": 15, "beans": 5}
# print(sell(stock, "rice", 4))       # ({"rice": 6, "beans": 5}, True)
# print(sell(stock, "beans", 9))      # ({"rice": 10, "beans": 5}, False)
# print(sell(stock, "yam", 1))        # ({"rice": 10, "beans": 5}, False)
# print(low_stock(stock, 6))          # ["beans"]
# print(total_items(stock))           # 15


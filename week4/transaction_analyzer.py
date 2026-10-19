transactions = []

def filter_transactions(transactions, condition):
    return filter(lambda transaction: condition, transactions)

def get_income(transactions):
    return filter(lambda transaction: transaction["type"] == "income", transactions)

def get_expenses(transactions):
    return filter(lambda transaction: transaction["type"] == "expense", transactions)

def get_status(transactions):
    pass

def find_largest_expenses(transactions):
    largest_amt, item = 0, ""

    for expense in get_expenses(transactions):
        if expense["amount"] > largest_amt:
            largest_amt = expense["amount"]
            item = expense["name"]

    return f"{item} ({largest_amt})"

def get_balance(transactions):
    expense_amt = calculate_total_expenses(transactions)
    total = calculate_total_income(transactions)
    return total - expense_amt

def calculate_total_expenses(transactions):
    total = 0
    for transaction in get_expenses(transactions):
        total += transaction["amount"]
    return total

def calculate_total_income(transactions):
    total = 0
    for transaction in get_income(transactions):
        total += transaction["amount"]
    return total

balance = get_balance(transactions)
print(f"Total income: {calculate_total_income(transactions)}")
print(f"Total expenses: {calculate_total_expenses(transactions)}")
print(f"Balance: {balance}")
print(f"Largest expenses: {find_largest_expenses(transactions)}")
print(f"Number of expenses: {len(list(get_expenses(transactions)))}")
print(f"Status: {"Positive" if balance > 0 else "Negative"} balance")

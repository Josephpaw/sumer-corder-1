# The amount of money we have to spend.
funds = 2500


# A dictionary of our items we are spending our budget on
budgets = {}

# A dictionary of the expenese of each budgeted item
expenses = {}


def AddBudget(name, amount):
    global funds
    if name in budgets:
        raise ValueError("Cannot add, budget for item exists")
    if amount > funds:
        raise ValueError("No can do, you are too broke.😂")
    budgets[name] = amount 
    funds -= amount
    expenses[name] = 0 
    return funds

def Spend(name, amount):
    if name not in expenses:
        raise ValueError("Item not in budget")
    expenses[name] += amount
    budgeted = budgets[name]
    Spent = expenses[name]
    return budgeted - Spent 

def printBudget():
    for name in budgets:
        budgeted = budgets[name]
        spent = expenses[name]
        remainingbudget = budgeted - spent
        print(f'{name:15s}, {budgeted:10.2f}, {spent:10.2f} ' 
              f'{remainingbudget:10.2f}')



print("Total Funds: ",funds)
AddBudget("books", 100)
AddBudget("rent", 800)
AddBudget("car Note", 200)

Spend("books", 50)
Spend("rent", 800)
Spend("car Note", 200)

printBudget()

from models import Expense
import json

dataJSONPath = r'C:\Users\leona\Desktop\Python\ExpenseTracker\data.json'

def save_expenses(expenses):
  with open(dataJSONPath,'w') as jsonFile:
      json.dump([i.to_dict() for i in expenses], jsonFile, indent=2)

def load_expenses() -> list[Expense]:
  retList = list()

  with open(dataJSONPath, 'r') as file:
    savedExpenses = json.loads(file)

    for i in savedExpenses:
      retList.append(Expense.from_dict(i))
  return retList
"""
storage.py
Storage functionality layer.

This module provides the funtionality to save and load from and to memory.

This module does not handle:
- Correct expense construction.
"""
from models import Expense
import json

dataJSONPath = r'C:\Users\leona\Desktop\Python\ExpenseTracker\data.json'

def save_expenses(expenses):
  """
  Save to system memory a list of Expense objects in JSON format.
  """
  with open(dataJSONPath,'w') as jsonFile:
      json.dump([i.to_dict() for i in expenses], jsonFile, indent=2)

def load_expenses() -> list[Expense]:
  """
  Return an Expense list loaded from system memory from a list of \
  dictionaries in JSON format containing raw data.

  Returns:
    list[Expense]: List containing Expense objects loaded from system memory
  """
  retList = list()

  with open(dataJSONPath, 'r') as file:
    savedExpenses = json.loads(file.read())

    for i in savedExpenses:
      retList.append(Expense.from_dict(i))
  return retList
from storage import load_expenses, save_expenses
from models import Expense


class Tracker:
  def __init__(self):
    self._expenses = load_expenses()

  def add_expense_from_data(self, amount:float, category:str, description:str, date:str|None = None):
    self.add_expense(Expense(amount, category, description, date))

  def add_expense(self, expenseData: Expense):
    if isinstance(expenseData, Expense):
      self._expenses.append(expenseData)
      save_expenses(self._expenses)
    else:
      raise TypeError(f"The expense to add is of the incorrect type, it is {type(expenseData)} when it should be Expense type")


  def get_all(self) -> list[Expense]:
    return list(self._expenses)

  def get_total(self) -> float:
    return round(sum(expense.amount for expense in self._expenses), 2)

  def get_by_category(self, filterCategory:str) -> list[Expense]:
    if isinstance(filterCategory, str):
      filterCategory = filterCategory.strip().lower()
      return [expense for expense in self._expenses if expense.category == filterCategory]
    else:
      raise TypeError("The argument is not of string type")
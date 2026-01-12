"""
tracker.py
Expense tracker abstraction.

This module provides a high-level interface for tracking expense records. \
It encapsulates the record details and exposes a stable API to the rest of \
the application.

This module does not handle:
- Saving and loading records to and from the file system.
- Validation beyond model-level constraints.
"""
from storage import load_expenses, save_expenses
from models import Expense


class Tracker:
  """
  Tracker responsible for managing internal expense records.

  It provides a thin layer over the storage-on-system functionality by adding \
  the possibility to expand the expense record, summarize and filter by category.
  """

  def __init__(self):
    self._expenses = load_expenses()

  def add_expense_from_data(self, amount:float, category:str, description:str, date:str|None = None):
    """
    Add a single expense item by providing raw data to the expense record and \
    save it to system memory.

    Args:
      amount(float|int): Amount spent in each transaction.
      category(str): Class to which this expense belongs to.
      description(str): Detailed information about each expense.
      date(str|none): Date of each expense if not defined, the \
        current date will be used.
    """
    self.add_expense(Expense(amount, category, description, date))

  def add_expense(self, expenseData: Expense):
    """
    Add a single expense item by providing an Expense type object to the expense \
    record and save it to system memory.

    Args:
      expenseData(Expense): A fully constructed Expense instance to be added to the tracker.

    Raises:
      TypeError: Risen when expenseData argument is not of type Expense
    """
    if isinstance(expenseData, Expense):
      self._expenses.append(expenseData)
      save_expenses(self._expenses)
    else:
      raise TypeError(f"The expense to add is of the incorrect type, it is {type(expenseData)} when it should be Expense type")


  def get_all(self) -> list[Expense]:
    """
    Return a shallow copy of all the expenses saved in system memory

    Returns:
      list[Expense]: All expenses saved in system memory
    """
    return list(self._expenses)

  def get_total(self) -> float:
    """
    Get the sum of all recorded expenses' amounts

    Returns:
      float: Sum of all expenses recorded in system memory.
    """
    return round(sum(expense.amount for expense in self._expenses), 2)

  def get_by_category(self, filterCategory:str) -> list[Expense]:
    """
    Return a list containing all expenses that match the given category.

    Args:
      filterCategory(str): String to match in all saved expenses.
    Returns:
      list[Expense]: List containing all filtered expenses. Will return an empty \
        list if no record found matching the provided argument.
    Raises:
      TypeError: Risen if the argument is not of string type.
    """
    if isinstance(filterCategory, str):
      filterCategory = filterCategory.strip().lower()
      return [expense for expense in self._expenses if expense.category == filterCategory]
    else:
      raise TypeError("The argument is not of string type")
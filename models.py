"""
models.py
Expense abstraction.

This module encapsulates the expense object abstraction.

This module does not handle:
- Saving and loading records to and from the file system.
"""
from datetime import datetime

class Expense:
  """
  The expense class is an abstraction of an individual expense record. To create \
  a fully created object, information about the amount, an arbitrary category and \
  a description must be provided, as well as an optional date.
  """

  def __init__(self, amount:float, category:str, description:str, date:str | None = None):
    self._validate_amount(amount)
    self._validate_category(category)
    self._validate_description(description)

    self.amount = round(float(amount),2)
    self.category = category.strip().lower()
    self.description = description.strip()
    self.date = date or datetime.now().strftime("%Y-%m-%d")

  def _validate_amount(self, amount):
    if not isinstance(amount, float) and not isinstance(amount, int):
      raise TypeError('"Amount" is not a number')
    if amount <= 0:
      raise ValueError('"Amount" must be greater than 0')
  def _validate_category(self, category):
    if not category:
      raise ValueError('"Category" cannot be empty')
  def _validate_description(self, description):
    if not description:
      raise ValueError('"Description" cannot be empty')

  def to_dict(self) -> dict:
    """
    Return a dictionary containing the raw data for a single instance.

    Returns:
      dict: A dictionary containing the expense instance information about amount, \
        category, description and date
    """
    return {"amount":      self.amount,
            "category":    self.category,
            "description": self.description,
            "date":        self.date,}

  @classmethod
  def from_dict(cls, data: dict) -> "Expense":
      """
      Create an Expense object from a dictionary containing raw data.

      Args:
        data(dict): Dictionary containing the raw data to be used for Expense object \
        creation.

      Returns:
        Expense: Object repesenting an expense
      """
      return cls(amount =     data["amount"],
                category =    data["category"],
                description = data["description"],
                date =        data["date"],)
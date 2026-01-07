from datetime import datetime

class Expense:
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
    return {"amount":      self.amount,
            "category":    self.category,
            "description": self.description,
            "date":        self.date,}
  @classmethod
  def from_dict(cls, data: dict) -> "Expense":
      return cls(amount =     data["amount"],
                category =    data["category"],
                description = data["description"],
                date =        data["date"],)
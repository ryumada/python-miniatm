from atm_card import ATMCard

class Customer:
  def __init__(self, idCard, custPin = 1234, custBalance = 10000):
    self.idCard = idCard
    self.pin = custPin
    self.balance = custBalance

  # ------------------------------- check methods ------------------------------ #
  def checkId(self):
    return self.idCard

  def checkPin(self):
    return self.pin

  def checkBalance(self):
    return self.balance

  # ------------------------------- todo methods ------------------------------- #
  def withdrawBalance(self, nominal):
    self.balance -= nominal
  
  def depositBalance(self, nominal):
    self.balance += nominal

  def updatePin(self, new_pin):
    self.pin = new_pin

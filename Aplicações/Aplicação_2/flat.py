#Objeto que contém as informações da conta, como o valor total e o período da conta

class Bill:
  def __init__ (self, amount, period):
    self.amount = amount
    self.period = period


#Objeto que contém as informações do colega de quarto, como o nome, os dias na casa e o valor da conta

class Flatmate:
  def __init__ (self, name, days_in_house):
    self.name = name
    self.days_in_house = days_in_house

  def pays(self, bill, flatmate2):
    weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
    to_pay = bill.amount * weight
    return to_pay
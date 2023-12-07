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

#Objeto que cria um arquivo PDF contendo as informações sobre os colegas de quarto, tais como nome, conta e o período da conta

class PdfReport:
	def __init__(self, filename):
		self.filename = filename

	def generate(self, flatmate1, flatmate2, bill):
		pass
	

the_bill = Bill (amount = 120, period = "March 2021")
john = Flatmate (name = "John", days_in_house = 20)
marry = Flatmate (name = "Marry", days_in_house = 25)


print("John pays: ", john.pays(bill=the_bill, flatmate2=marry))
print("Marry pays: ", marry.pays(bill=the_bill, flatmate2=john))
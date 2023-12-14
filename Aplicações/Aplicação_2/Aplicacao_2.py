#pip install fpdf

from reports import PdfReport
from flat import Bill, Flatmate

amount = float (input("Digite o valor da conta: R$ "))
period = input ("Digite o período da conta (ex.: Dezembro 2020): ")

name1 = input ("Digite seu nome: ")
days_in_house1 = int(input(f"Quantos dias {name1} ficou na casa durante o período da conta?"))

name2 = input ("Digite o nome do colega de quarto: ")
days_in_house2 = int(input(f"Quantos dias {name2} ficou na casa durante o período da conta?"))


the_bill = Bill (amount, period)
fmate1 = Flatmate (name1, days_in_house1)
fmate2 = Flatmate (name2, days_in_house2)


print(f"Valor a pagar de {fmate1.name}: ", fmate1.pays(bill=the_bill, flatmate2=fmate2))
print(f"Valor a pagar de {fmate2.name}: ", fmate2.pays(bill=the_bill, flatmate2=fmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=fmate1, flatmate2=fmate2, bill=the_bill)
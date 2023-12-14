import webbrowser
import os
from fpdf import FPDF


#Objeto que cria um arquivo PDF contendo as informações sobre os colegas de quarto, tais como nome, conta e o período da conta

class PdfReport:
  def __init__(self, filename):
    self.filename = filename

  def generate(self, flatmate1, flatmate2, bill):

    flatmate1_pay=str(round(flatmate1.pays(bill, flatmate2),2))
    flatmate2_pay=str(round(flatmate2.pays(bill, flatmate1),2))

    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()

    #Adicionar ícone
    pdf.image("files/house.png", w=30, h=30)

    # Insere o Título
    # Fonte Times, tamanho 24, negrito
    pdf.set_font(family='Times', size=24, style ='B')
    pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1) #ln faz o texto seguinte ficar embaixo

    #Insere a legenda e o valor
    pdf.set_font(family="Times", size=14, style='B')
    pdf.cell(w=100, h=25, txt="Period", border=0)
    pdf.cell(w=150, h=25, txt=bill.period, border=0, ln=1)

    #Insere o nome e o valor devido ao primeiro colega de quarto
    pdf.set_font(family="Times", size=12)
    pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
    pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

    #Insere o nome e o valor devido ao primeiro colega de quarto
    pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
    pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0)

    #Alterando o diretório para a pasta "files", gera e abre o arquivo PDF
    os.chdir("files")
    pdf.output(self.filename)
    webbrowser.open(self.filename)
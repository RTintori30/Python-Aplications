Título: Conta de Colegas de Quarto

Descrição: Uma aplicação que recebe o valor de uma conta durante um período específico e os dias em que cada colega de quarto estiveram na casa, além de retornar quanto cada pessoa precisa pagar. Também gera um relatório em PDF com o nome de cada um, o período e quanto cada precisa pagar.

Objetos: Conta:
		valor
		periodo
	 
	Colega_de_Quarto:
		nome
		dias_na_casa
		pagar(conta)
	
	RelatorioPdf:
		nome_do_arquivo
		gerar(colega1, colega2, conta)




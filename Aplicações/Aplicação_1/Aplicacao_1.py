from random import randint
import turtle

class Point:
	
	#Função __init__ é executada sempre que vc cria a instância de um objeto
	def __init__(self, x,y): #"self" em uma classe é a variável que contém a instância do objeto que está sendo criado por aquela classe
		self.x = x
		self.y = y

	#Definindo função para saber se determinado ponto está dentro do retangulo:
	#Função "falls_in_rectangle" só será executada quando você cahamar o método específico
	def falls_in_rectangle(self, rectangle):
		if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y:
			return True
		else:
			return False


class Rectangle:

	def __init__(self, point1, point2):
		self.point1 = point1
		self.point2 = point2
	
	def area (self):
		return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)

#Abaixo se trata de uma herança, onde GuiRectangle é a criança, Rectangle é o pai
class GuiRectangle(Rectangle): # GuiRectangle terá os mesmos atributos da Classe Rectangle
	def draw(self, canvas):
		canvas.penup()
		canvas.goto(self.point1.x, self.point1.x)

		canvas.pendown()
		canvas.forward(self.point2.x - self.point1.x)
		canvas.left(90)
		canvas.forward(self.point2.y - self.point1.y)
		canvas.left(90)
		canvas.forward(self.point2.x - self.point1.x)
		canvas.left(90)
		canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):

	def draw(self,canvas):
		canvas.penup()
		canvas.goto(self.x, self.y)
		canvas.pendown()
		canvas.dot()


#Criando o objeto retangulo
rectangle = GuiRectangle (
	Point (randint (0, 400), randint (0, 400)), #referente a point1 ( 1 valor aleatório de 0 a 400 referente a "x" e o mesmo para "y" ) 
	Point (randint (10, 400), randint (10, 400))) #referente a point2 ( 1 valor aleatório de 10 a 400 referente a "x" e o mesmo para "y" )

print (f"Coordenadas do Retangulo: {rectangle.point1.x}, {rectangle.point1.y} e {rectangle.point2.x}, {rectangle.point2.y}")

user_point = GuiPoint(float(input("Eixo X: ")), float(input("Eixo Y: ")))

print ("Seu ponto está dentro do retângulo: ", user_point.falls_in_rectangle (rectangle))
print ("Área do retângulo: ", rectangle.area() )

myturtle = turtle.Turtle()
rectangle.draw(canvas = myturtle)
user_point.draw(canvas = myturtle)
turtle.done()
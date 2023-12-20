class Rectangle:

    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    #Metodo que calcula e retorna a area de um retangulo.
    def area(self):
        return self.width * self.height
    
    #Metodo que calcula e retorna o perímetro de um retangulo.
    def perimeter(self):
        return 2 * (self.width + self.height)

    #Metodo que calcula a distancia do centro de um triangulo a um ponto dado    
    def distance_to_point(self, x, y):
        dist = ((self.x - x)**2 + (self.y - y)**2) **0.5
        return dist
    
    #Método que calcula o tempo que gasta do centro do retangulo até determinado ponto dado.
    def time_to_point(self, x, y, speed):
        time = self.distance_to_point(x,y) / speed
        return time

#Instância que chama e printa o resultado do metodo "area" 
resultado = Rectangle (10, 20, 5, 7)
print (resultado.area())

#Instância que chama e printa o resultado do metodo "time_to_point" 
resultado2 = Rectangle (width=3, height=4, x=1, y=2)
print(resultado2.time_to_point(x=2, y=3, speed=20))
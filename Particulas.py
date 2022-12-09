from Algoritmos import distanciaEuclidiana

class Particula:
    def __init__(self, id = 0, origen_x = 0, origen_y = 0, destino_x = 0, destino_y = 0, velocidad = 0, red = 0, green = 0, blue = 0, distancia = 0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distanciaEuclidiana(origen_x, origen_y, destino_x, destino_y)

    def __str__(self):
        return(
            'id = ' + str(self.__id) + '\n' +
            'origen_x = ' + str(self.__origen_x) + '\n' +
            'origen_y = ' + str(self.__origen_y) + '\n' +
            'destino_x = ' + str(self.__destino_x) + '\n' +
            'destino_y = ' + str(self.__destino_y) + '\n' +
            'velocidad = '+ str(self.__velocidad) + '\n' + 
            'red = '+ str(self.__red) + '\n'+ 
            'green = '+ str(self.__green) + '\n' + 
            'blue = '+ str(self.__blue) + '\n' + 
            'distancia = '+ str(self.__distancia)+ '\n'
        )
    
    def to_dict(self):
        return{
            "id":self.__id,
            "origen_x":self.__origen_x,
            "origen_y":self.__origen_y,
            "destino_x":self.__destino_x,
            "destino_y":self.__destino_y,
            "velocidad":self.__velocidad,
            "red":self.__red,
            "green":self.__green,
            "blue":self.__blue,
        }

    @property
    def id(self):
        return self.__id

    @property
    def origen_x(self):
        return self.__origen_x

    @property
    def origen_y(self):
        return self.__origen_y

    @property
    def destino_x(self):
        return self.__destino_x

    @property
    def destino_y(self):
        return self.__destino_y

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def blue(self):
        return self.__blue

    @property
    def green(self):
        return self.__green

    @property
    def distancia(self):
        return self.__distancia

    def __lt__(self, Particula)->bool:
        return self.id < Particula.id
    
    def consultarVelocidad(Particula):
        return Particula.__velocidad

    def consultarDistancia(Particula):
        return Particula.__distancia

class Puntos:
    def __init__(self, x:int=0, y:int=0, red:int=0, green:int=0, blue:int=0):
        self.x = x
        self.y =y
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self) -> str:
        return f"Punto(x: {self.x}, y: {self.y})"
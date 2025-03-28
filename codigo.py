class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto(x={self.x}, y={self.y})"
    
#Añadir método constructor
@classmethod
def crear(cls, x=0, y=0):
    return cls(x, y)

#Sobreescribir método __str__
def __str__(self):
    return f"({self.x},{self.y})"

#Indica el cuadrante en el que se encuentra el punto
def cuadrante(self):
    if self.x > 0 and self.y > 0:
        return "Primer cuadrante"
    elif self.x < 0 and self.y > 0:
        return "Segundo cuadrante"
    elif self.x < 0 and self.y < 0:
        return "Tercer cuadrante"
    elif self.x > 0 and self.y < 0:
        return "Cuarto cuadrante"
    elif self.x == 0 and self.y != 0:
        return "Sobre el eje Y"
    elif self.x != 0 and self.y == 0:
        return "Sobre el eje X"
    else:
        return "En el origen"
    
#Añadir método vector (calcula vector entre dos puntos)
def vector(self, otro_punto):
    return Punto(otro_punto.x - self.x, otro_punto.y - self.y)

#Añadir método distancia (calcula la distancia entre dos puntos)
def distancia(self, otro_punto):
    import math
    distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
    print(f"La distancia entre los puntos es: {distancia}u")
    return distancia
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
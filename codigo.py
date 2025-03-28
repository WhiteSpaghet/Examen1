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

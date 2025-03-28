from punto import Punto
from rectangulo import Rectangulo

def main():
    # Crear puntos A, B, C y D
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)

    # Imprimir puntos
    print(f"Punto A: {A}")
    print(f"Punto B: {B}")
    print(f"Punto C: {C}")
    print(f"Punto D: {D}")

    # Consultar cuadrantes
    print(f"El punto A pertenece al cuadrante: {A.cuadrante()}")
    print(f"El punto C pertenece al cuadrante: {C.cuadrante()}")
    print(f"El punto D pertenece al cuadrante: {D.cuadrante()}")

    # Consultar vectores AB y BA
    print(f"Vector AB: {A.vector(B)}")
    print(f"Vector BA: {B.vector(A)}")

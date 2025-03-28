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
    print(f"El punto B pertenece al cuadrante: {B.cuadrante()}")
    print(f"El punto C pertenece al cuadrante: {C.cuadrante()}")
    print(f"El punto D pertenece al cuadrante: {D.cuadrante()}")

    # Consultar vectores AB y BA
    print(f"Vector AB: {A.vector(B)}")
    print(f"Vector BA: {B.vector(A)}")

     # Consultar distancias
    print(f"Distancia entre A y B: {A.distancia(B)}")
    print(f"Distancia entre B y A: {B.distancia(A)}")

    # Determinar el punto más lejano del origen
    distancias = {
        "A": A.distancia(D),
        "B": B.distancia(D),
        "C": C.distancia(D)
    }
    punto_mas_lejano = max(distancias, key=distancias.get)
    print(f"El punto más lejano del origen es: {punto_mas_lejano}")

    # Crear un rectángulo con los puntos A y B
    rectangulo = Rectangulo(A, B)

    # Consultar base, altura y área del rectángulo
    print(f"Base del rectángulo: {rectangulo.base()}")
    print(f"Altura del rectángulo: {rectangulo.altura()}")
    print(f"Área del rectángulo: {rectangulo.area()}")

if __name__ == "__main__":
    main()
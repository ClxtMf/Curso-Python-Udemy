
import math

def calcular_area_do_circulo(raio):
    # Calcula a área do círculo utilizando a fórmula: área = pi * raio^2
    area = math.pi * (raio ** 2)
    return area

def main():
    # Solicita ao usuário o raio do círculo como um número de ponto flutuante
    raio = float(input("Digite o raio do círculo: "))

    # Calcula a área do círculo chamando a função calcular_area_do_circulo
    area = calcular_area_do_circulo(raio)

    # Exibe o resultado para o usuário
    print("A área do círculo com raio", raio, "é:", area)

if __name__ == "__main__":
    main()

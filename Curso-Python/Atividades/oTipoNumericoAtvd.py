
import math

"""
Exemplo do conteúdo visto acima!
"""


def main():
    # Solicita ao usuário dois números inteiro
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))

    # Realiza algumas operações com os números
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2
    divisao_inteira = num1 // num2
    resto_divisao = num1 % num2
    potencia = num1 ** num2
    raiz_quadrada_num1 = math.sqrt(num1)
    absoluto_num2 = abs(num2)

    # Exibe os resultados das operações
    print("Resultados das Operações:")
    print("Soma:", soma)
    print("Subtração:", subtracao)
    print("Multiplicação:", multiplicacao)
    print("Divisão:", divisao)
    print("Divisão Inteira:", divisao_inteira)
    print("Resto da Divisão:", resto_divisao)
    print("Potência:", potencia)
    print("Raiz Quadrada do Primeiro Número:", raiz_quadrada_num1)
    print("Valor Absoluto do Segundo Número:", absoluto_num2)


if __name__ == "__name__":
    main()

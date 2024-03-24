"""
representados pelo tipo de dados int. Eles podem ser positivos, negativos ou zero, e não têm limite de tamanho,
o que significa que você pode trabalhar com números inteiros tão grandes quanto a memória do seu sistema permite
"""

# Atribuição de números inteiros a variáveis
numero1 = 10
numero2 = -20
numero3 = 30

#  Adição
soma = numero1 + numero2
print("O resultado da soma é:", soma)  # Resultado: 10 + (-20) = -10

# Subtração
subtracao = numero1 - numero3
print("O resultado da subtração é:", subtracao)  # Resultado: 10 - 30 = -20

multiplicacao = numero2 * numero3
print("O resultado da multiplicação é:", multiplicacao)  # Resultado: -20 * 30 = -600

# Divisão (retorna um número de ponto flutuante)
divisao = numero1 / numero3
print("O resultado da divisão é: ", divisao)  # Resultado: 10 / 30 = 0.3333333333333333

# Divisão inteira (descarta a parte fracionária)
divisao_inteira = numero1 // numero3
print("O resultado da divisão inteira é:", divisao_inteira)  # Resultado: 10 // 30 = 0

# Resto da divisão (módulo)
resto_divisao = numero1 % numero2
print("O resultado do módulo é:", resto_divisao)  # Resultado: 10 % (-20) = -10

# Potência
potencia = numero1 ** 2
print("O resultado da potência é:", potencia)  # Resultado: 10 ** 2 = 100

# Conversão dos tipos

# Conversão de string para inteiro
texto = "100"
inteiro = int(texto)  # Resultado: 100
print(inteiro)

# Conversão de float para inteiro (parte decimal é truncada)
flutuante = 10.5
interio_flutuante = int(flutuante)  # Resultado: 10
print(interio_flutuante)

# Operações avançadas

# Utilização de funções matemáticas

import math

raiz_quadrada = math.sqrt(25)  # Resultado: 5.0
print(raiz_quadrada)

# Valor absoluto
absoluto = abs(-10)  # Resultado: 10
print(absoluto)



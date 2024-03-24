"""
são representados pelo tipo de dados float. Esses números são usados para representar
valores decimais e são extremamente úteis em uma variedade de contextos, especialmente
em cálculos matemáticos e científicos.
"""

# Declaração de variáveis

# Operações de números de ponto flutuante a variáveis

numero1 = 3.14
numero2 = -0.5
numero3 = 10.0

# Operações aritméticas

# Adição
soma = numero1 + numero2
print("O resultado da soma é:", soma)  # Resultado: 3.14 + (-0.5) = 2.64

# Subtração
subtracao = numero1 - numero2
print("O reultado da subtração é:", subtracao)  # Resultado: 3.14 - (-0.5) = 3.64

# Multiplicação
multiplicacao = numero1 * numero3
print("O resultado da multiplicação é:", multiplicacao)  # Resultado: 3.14 * 10.0 = 31.4

# Divisão
divisao = numero3 / 2
print("O resultado da divisão é:", divisao)  # Resultado: 10.0 / 2 = 5.0

# Potência
potencia = numero3 ** 2
print("O resultado da potência é:", potencia)  # Resultado: 10.0 elevado a 2 = 100.0

# Conversão de Tipos

# Conversão de inteiro para float
inteiro = 5
flutuante = float(inteiro)  # Resultado: 5.0

# Conversão de string para float
texto = "3.14"
flutuante_texto = float(texto)  # Resultado: 3.14

# Operações Avançada

# Utilização de funções matemáticas
import math

# Trigonometria
seno = math.sin(0.5)  # Resultado: seno de 0.5 radianos

# Valor absoluto
absoluto = abs(-10.5)  # Resultado: 10.5

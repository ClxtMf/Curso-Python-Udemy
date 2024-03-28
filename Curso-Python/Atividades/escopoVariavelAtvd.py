"""
Suponha que você tenha uma função para calcular o total de vendas a partir de uma lista de valores
e outra função para calcular o lucro líquido com base no total de vendas e em alguns custos fixos.
Essas funções precisam acessar variáveis como o total de vendas e os custos fixos.
"""

total_vendas = 0
custos_fixos = 100


def calcular_total_vendas(vendas):
    global total_vendas
    total_vendas = sum(vendas)


def calcular_lucros():
    global total_vendas
    global custos_fixos
    lucro = total_vendas - custos_fixos
    return lucro


# Exemplos de uso da funções
total_vendas = [500, 750, 1000, 1200]
calcular_total_vendas(total_vendas)
lucros_do_mes = calcular_lucros()

print("Total de vendas do mês:", total_vendas)
print("Lucro de mês:", lucros_do_mes)

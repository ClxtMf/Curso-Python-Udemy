"""
representado pelos valores True e False, que são usados para representar os estados de verdadeiro e falso, respectivamente.
Os valores booleanos são frequentemente usados em expressões lógicas e de controle de fluxo para tomar decisões em programas.
"""

# Exemplos de tipos booleanos com python
# Declaração de variáveis

verdadeiro = True
falso = False

# Expressões lógicas
# Operadores de comparação

x = 5
y = 10

maior_que = x > y
print("O resultado séra:", maior_que)  # False, pois 5 não é maior que 10

menor_que = x < y
print("O resultado séra:", menor_que)  # True, pois 5 é menor que 10

igual = x == y
print("O resultado séra:", igual)  # False, pois 5 não é igual a 5

diferente = x != y
print("O resultado séra:", diferente)  # True, pois 5 é difirente de 10

# Operadores lógicos
e_logico = True and False  # False, pois ambos os valores devem ser verdadeiros
ou_logico = True or False  # True, pois pelo menos um valor é verdadeiro
nao_logico = not True  # False, pois inverte o valor booleano

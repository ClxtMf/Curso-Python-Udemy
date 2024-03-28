"""
O escopo de variável refere-se à região do código onde a variável é acessivel.
O escopo determina onde uma variável pode ser referenciada e modifica ao longo do programa.
Existem dois principais tipos de escopo em python: escopo local e escopo global.
Aqui está uma explicação de cada um deles, juntamente com os exemplos:
"""

# Escopo local
"""
Variáveis definidas dentro de uma função têm escopo local. Isso siginifica que elas só podem ser
acessadas detro da função. Se uma variável local tiver o mesmo nome de uma variável global, a variável
local terá precedência detro da função. Aqui está um exemplo:
"""

def minha_funcao():
    x = 10 # variável local
    print("Dentro da função, x é:", x)

minha_funcao()
# print(x)  # Isso geraria um erro, pois x é uma variável local e ão está acessivel aqui.


# Escopo global
"""
Variáveis definidas fora de todas as funções têm escopo global. isso significa que elas podem ser
acessadas em qualquer lugar do programa, incluido dentro de funções. Se uma vaiável global for modificada
dentro de uma função, a modificação refletirá no valor da variável global. Aqui
está um exemplo: 
"""

y = 20 # variável global

def minha_funcao2():
    print("Dentro da função, y é:", y)

minha_funcao2()
print("Fora da função, y é:", y)
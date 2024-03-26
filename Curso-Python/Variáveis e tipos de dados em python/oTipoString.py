"""
uma string é uma sequência de caracteres entre aspas simples (''), aspas duplas ("") ou até mesmo aspas triplas ('' ou "").
As strings são utilizadas para representar texto e são uma parte fundamental da linguagem de programação.
"""

# Declaração de variáveis

nome = "python"

mensagem = 'Olá, mundo!'

paragrafo = """Este é um exemplo
de um parágrafo
em Python."""

# Acesso a caracteres

# Em Python, é possível acessar caracteres individuais de uma string utilizando indexação. O índice do primeiro caractere é 0.

palavra = "python"

primeiro_caractere = palavra[0]  # "P"
segundo_caractere = palavra[1]  # "y"
ultimo_caractere = palavra[-1]  # "n" (índice negativo acessa do final para o início)

# Concatenação de strings

cumprimento = "Olá, " + nome + "!"


# Operações com strings

# Comprimento string: `len(string)`
# Verificar se uma substring está presente na string: `substring in string`
# Repetir uma string: `string * n`
# Dividir uma string em substring: `string.split(delimiter)`
# Juntar substrings em única strig: `delimiter.join(substrings)`
# Converter uma string para maiúsculas ou minúsculas: `string.upper()` , `string.lower()`


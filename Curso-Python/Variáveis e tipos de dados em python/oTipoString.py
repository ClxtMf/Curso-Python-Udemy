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


# Comprimento da String: len(string)

texto = "Python é uma linguagem de programação"
comprimento = len(texto)
print("O comprimento da string é:", comprimento)  # Saída: O comprimento da string é: 34

# Verificar se uma Substring está Presente na String: substring in string

texto = "Python é uma linguagem de programação"
substring = "linguagem"
if substring in texto:
    print("A substring está presente na string.")
else:
    print("A substring não está presente na string.")
# Repetir uma String: string * n

texto = "Olá, "
repeticoes = 3
resultado = texto * repeticoes
print("O resultado da repetição é:", resultado)  # Saída: Olá, Olá, Olá,

# Dividir uma String em Substrings: string.split(delimiter)

frase = "Python é uma linguagem de programação"
palavras = frase.split(" ")
print("As palavras da frase são:", palavras)  # Saída: As palavras da frase são: ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']

# Juntar Substrings em uma Única String: delimiter.join(substrings)

palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
frase = " ".join(palavras)
print("A frase formada é:", frase)  # Saída: A frase formada é: Python é uma linguagem de programação

# Converter uma String para Maiúsculas ou Minúsculas: string.upper(), string.lower()

texto = "Python é uma linguagem de programação"
texto_maiusculo = texto.upper()
texto_minusculo = texto.lower()
print("Texto em maiúsculas:", texto_maiusculo)
print("Texto em minúsculas:", texto_minusculo)

# Estrutura condicional (if-else)

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Loops

contador = 0
while contador < 5:
    print("Contagem:", contador)
    contador += 1

# Compreensão de Lista (List Comprehension)

numeros = [1, 2, 3, 4, 5]
pares = [numero for numero in numeros if numero % 2 == 0]
print("Números pares:", pares)  # Resultado: [2, 4]

# Funções que retornam valores booleanos

def eh_par(numero):
    return numero % 2 == 0


print(eh_par(input("Digite um número: ")))

# Métodos que retornam valores booleanos
texto = "python"
print(texto.islower())  # True, pois todas as letras estão minúsculas
print(texto.isupper())  # False, pois todas as letrsa estão maiúsculas

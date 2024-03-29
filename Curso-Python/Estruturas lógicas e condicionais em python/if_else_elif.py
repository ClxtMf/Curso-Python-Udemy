"""
Os tipos `if`, `else` e `elif` são usados para controle de fluxo condicional, permitindo que o programa
execute diferentes blocos de códigos dependendo de condições especificas.
"""

# If:
"O tipo `if` é usado para executar um bloco de código se uma condiçõa for verdadeira."

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você  é maior de idade.")

# Else:
"O tipo `else` é usado em conjunto com `if` para executar um bloco de código se a condição `if` for falsa."

idade1 = int(input("Digite sua idade: "))

if idade1 >= 18:
    print("Você é maior de idade.")

else:
    print("Você é menor de idade.")

# elif:
"""
O tipo elif (abreviação de "else if") é usado para verificar múltiplas condições após um if.
Ele permite verificar várias condições e executar um bloco de código correspondente à primeira condição verdadeira encontrada.
Pode haver zero ou mais blocos elif após o if.
"""

nota = int(input("Digite sua nota: "))

if nota >= 90:
    print("Nota: A")
elif nota >= 80:
    print("Nota: B")
elif nota >= 70:
    print("Nota: C")
else:
    print("Nota: D")
    
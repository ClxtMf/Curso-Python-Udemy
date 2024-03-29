def verificar_ingresso():
    idade = int(input("Por favor, digite sua idade: "))

    if idade >= 18:
        print("Você é elegível para comprar ingressos para o evento.")
        categoria = input("Digite a categoria de ingresso desejada (VIP ou Normal): ").lower()

        if categoria == "VIP":
            preco = 100
        elif categoria == "Normal":
            preco = 50
        else:
            print("Categoria inválida. Por favor, tente novamente.")
            return

        quantidade = int(input("Digite a quantidade de ingressos desejada: "))
        total = preco * quantidade
        print("Total a pagar:", total)
    else:
        print("Desculpe, você precisa ter 18 anos ou amis para comprar ingressos para o evento.")


verificar_ingresso()

pedidos = []

while True:
    print("Bem-Vindo, escolha uma opção do cárdapio: ")
    print("1 - Comida")
    print("2 - Bebida")
    print("3 - Doces")
    print("4 - Ver pedidos")
    print("5 - Finalizar o pedido")
    print("6 - Remover item do pedido")
    print("\n")
    try:
        op = int(input("Digite sua escolha: "))
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")
        continue

    if op == 1:
        print("1 - Hamburgue - R$ 10.00 \n Pão, Carne de hamburgue, queijo musarela, alface e tomate")
        print("2 - fatia de Pizza - R$ 8.00 \n Frango, azeitona, queijo musarela, tomate, cebola e oregano")
        print("3 - Empada de Frango - R$ 3.50")
        print("4 - Torta de Frango - R$ 4.00")
        print("5 - Pão de Queijo R$ 1.00 Unidade")
        print("6 - Coxinha de Frango - R$ 3.50")

        op1 = int(input("digite sua escolha de comida: "))
        if op1 == 1:
            pedidos.append(("Hamburgue",10.00))
            print("Hamburguer adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é um hamburguer, aguarde e logo estara pronto! ")
                break

        elif op1 == 2:
            pedidos.append(("Fatia de pizza",8.00))
            print("Fatia de Pizza adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é uma fatia de Pizza, aguarde e logo estara pronto! ")
                break

        elif op1 == 3:
            pedidos.append(("Empada de Frango",3.50))
            print("Empada de Frango adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é uma empada de Frango, aguarde e logo estara pronto! ")
                break

        elif op1 == 4:
            pedidos.append(("Torta de Frango",4.00))
            print("Torta de Frango adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é uma torta de Frango, aguarde e logo estara pronto! ")
                break

        elif op1 == 5:
            pedidos.append(("Pão de Queijo",1.00))
            print("Pão de queijo adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é um pão de queijo, aguarde e logo estara pronto! ")
                break

        elif op1 == 6:
            pedidos.append(("Coxinha de frango",3.50))
            print("Coxinha de frango adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é uma coxinha, aguarde e logo estara pronto! ")
                break


    elif op == 2:
        print("1 - Guaraná - R$ 3.50")
        print("2 - Guaraná Zero - R$ 3.50")
        print("3 - Coca - Cola - R$ 3.50")
        print("4 - Cola - Cola Zero - R$ 3.50")
        print("5 - Fanta Uva - R$ 3.50")
        print("6 - Fanta Laranja - R$ 3.50")
        print("7 - Suco de Goiaba - R$ 2.00")
        print("8 - Suco de Manga - R$ 2.00")
        print("9 - Suco de Maracujá - R$ 2.00")

        op2 = int(input("Digite sua escolha de bebida: "))

        if op2 == 1:
            pedidos.append(("Guaranà",3.50))
            print("Guaraná adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é um guaraná, aguarde e logo estara pronto! ")
                break

        elif op2 == 2:
            pedidos.append(("Guaraná zero",3.50))
            print("Guaraná zero adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é um guaraná zero, aguarde e logo estara pronto! ")
                break

        elif op2 == 3:
            pedidos.append(("Cola - Cola",3.50))
            print("Coca - Cola adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é uma Coca - Cola, aguarde e logo estara pronto! ")
                break

        elif op2 == 4:
            pedidos.append(("Cola - Cola zero",3.50))
            print("Coca - Cola Zero adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é uma Coca - Cola Zero, aguarde e logo estara pronto! ")
                break

        elif op2 == 5:
            pedidos.append(("Fanta Uva",3.50))
            print("Fanta Uva adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é uma Fanta Uva, aguarde e logo estara pronto! ")
                break

        elif op2 == 6:
            pedidos.append(("Fanta Laranja",3.50))
            print("Fanta Laranja adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é uma Fanta Laranja, aguarde e logo estara pronto! ")
                break

        elif op2 == 7:
            pedidos.append(("Suco de Goiaba",2.00))
            print("Suco de Goiaba adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é um suco de Goiaba, aguarde e logo estara pronto! ")
                break

        elif op2 == 8:
            pedidos.append(("Suco de Manga",2.00))
            print("Suco de Manga adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é um Manga, aguarde e logo estara pronto! ")
                break

        elif op2 == 9:
            pedidos.append(("Suco de Maracujá",2.00))
            print("Suco de Maracujá adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é um Suco de Maracujá, aguarde e logo estara pronto! ")
                break


    elif op == 3:
        print("1 - Brigadeiro - R$ 2.00")
        print("2 - Beijinho - R$ 2.00")
        print("3 - Pudim - R$ 5.00")
        print("4 - Bolo de Chocolate - R$ 6.00")

        op3 = int(input("Digite sua escolha de doce: "))

        if op3 == 1:
            pedidos.append(("Brigadeiro",2.00))
            print("Brigadeiro adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é um brigadeiro, aguarde!")
                break

        elif op3 == 2:
            pedidos.append(("Beijinho",2.00))
            print("Beijinho adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é um beijinho, aguarde!")
                break

        elif op3 == 3:
            pedidos.append(("Pudim",5.00))
            print("Pedido adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é um Pudim, aguarde!")
                break

        elif op3 == 4:
            pedidos.append(("Bolo de Chocolate",6.00))
            print("Bolo de chocolate adicionado ao pedido.")
            pergunta = input("Digite sim para finalizar sua escolha ou não para volta ao cárdapio de opções: ").lower()
            if pergunta == "sim":
                print("Seu pedido é um bolo de chocolate, aguarde!")
                break

    elif op == 4:
        if len(pedidos) == 0:
            print("\nseu pedido ainda está vazio.")
        else:
            print("\nItens do seu pedido:")
            total = 0
            for nome, preco in pedidos:
                print("-", nome,"-R$ {:.2f}".format(preco))
                total += preco
            print("\nTotal parcial: R$ {:.2f}".format(total))

    elif op == 5:
        if len(pedidos) == 0:
            print("Você não fez nenhum pedido.")
        else:
            print("\nPedidos final:")
            total = 0
            for nome, preco in pedidos:
                print("-", nome,"-R$ {:.2f}".format(preco))
                total += preco

            print("\nTotal a pagar: R$ {:.2f}".format(total))
            print("\nObrigado pelo pedido!")
        break

    elif op == 6:
        if len(pedidos) == 0:
            print("\nSeu pedido está vazio.")
        else:
            print("\nItens do seu pedido:")

            for i,(nome,preco) in enumerate(pedidos, start=1):
                print(i,"-", nome,"-R$ {:.2f}".format(preco))

            try:
                remover = int(input("\nDigite o número do item que deseja remover: "))

                if 1 <= remover <= len(pedidos):
                    item_removido = pedidos.pop(remover - 1)
                    print("Item removido:", item_removido[0])
                else:
                    print("Número inválido.")

            except ValueError:
                print("Digite apenas números.")

















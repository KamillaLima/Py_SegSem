import fun as f
#PROGRAMA PRINCIPAL
while True:
    print("----MENU-----\n "
          "0-SAIR \n"
          " 1-Método de pesquisa sequencial\n"
          " 2-Ordenação  crescente da lista\n"
          " 3-Ordenação decrescente da lista\n"
          " 4-Escolher ordem da lista \n"
          " 5- Método de Pesquisa Binária ")
    lista = [5, 76, 45, 98, 8, 6, 34, 2, 1, 6]
    opcao = int(input("Digite a opção desejada"))
    if opcao == 0 :
        break

    elif opcao == 1 :
        valor = float(input("Informe um valor : "))
        if f.pesquisaMPS(lista,valor):
            print("Esse valor pertence a lista")
        else:
            print("Esse valor não pertence a lista")

    elif opcao == 2:
        f.ordenaListaCres(lista)
        print(lista)

    elif opcao == 3:
        f.ordenaListaDecres(lista)
        print(lista)

    elif opcao == 4:
        escolha = int(input("[1] - Ordem CRESCENTE\n"
                            "[-1] - Ordem DECRESCENTE"))
        while escolha != 1 and escolha != -1:
            escolha = int(input("[1] - Ordem CRESCENTE\n"
                                "[-1] - Ordem DECRESCENTE"))
        f.ordenaListaTipo(lista,escolha)

    elif opcao == 5 :
        f.ordenaListaCres(lista)
        valor = float(input("Informe um valor : "))
        if f.pesquisaMPB(lista,valor):
            print("Esse valor pertence a lista")
        else:
            print("Esse valor não pertence a lista")

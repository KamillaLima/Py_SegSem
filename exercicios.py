#KAMILLA DE LIMA RODRIGUES   1TDSA     RM96112

from random import randint

#exercicio 1:
def contadorPalavras(frase):
    fraseNova = frase.replace(",", " ").replace("."," ").split()
    return len(fraseNova)




#exercicio 2
def vefCPF(cpf,voltas):
    cpfNum = 0
    for i in range(0,len(cpf),1):
        soma = int(cpf[i])*voltas
        cpfNum += soma
        voltas-=1
    return cpfNum


def vefDigito(cpf,voltas):
    restoDiv = vefCPF(cpf,voltas) % 11
    if restoDiv < 2:
        dig = 0
    else:
        dig = 11 - restoDiv
    return dig



#exercicio 4
def gerarCPF():
    cpf = str(randint(100000000, 999999999))
    prim = vefDigito(cpf,10)
    cpf = cpf + str(prim)
    seg = vefDigito(cpf,11)
    return cpf + str(seg)






#exercicio 5
def calcularMedia (*valores):
    soma = 0
    val = 0
    for i in range(0,len(valores),1):
        soma=soma+valores[i]
        val+=1
    return soma/val


#exercicio 6
def maiorVal(*valores):
    volta= 0
    for i in range(0,len(valores),1):
        if volta == 0:
            maior = valores[i]
        else:
            if maior < valores[i]:
                maior = valores[i]
        volta+=1
    return maior


def titulo(msg):
    print("-"*12 + msg + "-"*12)
def menuPrincipal():
    print()
    print("ESCOLHA UMA DAS OPÇÕES ABAIXO: \n"
          "[1]-Separar palavras\n"
          "[2]-Validar CPF\n"
          "[3]-Imprimindo 2 digitos finais \n"
          "[4]-Gerar CPF\n"
          "[5]-Calcular média\n"
          "[6]-Maior valor\n"
          "[7]-Sair\n")
    print()



#######MENU PRINCIPAL########################
while True:
    menuPrincipal()
    opcao = int(input("Informe a opção desejada: "))
    match(opcao):
        case 1:
            titulo("Separando palavras")
            print(f"Essa frase contem {contadorPalavras(input('Informe a frase: '))} palavras")

        case 2:
            titulo("Validando CPF")
            cpf = input("Informe os 9 primeiros digitos do CPF: ")
            dig_um = vefDigito(cpf,10)
            cpf = str(cpf) +str(dig_um)
            dig_dois = vefDigito(cpf,11)
            cpf =str(cpf) +str(dig_dois)
            fim = input("Informe os últimos dois digitos: ")
            digitosFinais = str(dig_um) + str(dig_dois)
            print("CPF VÁLIDO") if fim == digitosFinais else print("CPF INVÁLIDO")

        case 3:
            titulo("Imprimindo os 2 dígitos finais ")
            print(f"{dig_um} e {dig_dois}")

        case 4:
            titulo("Gerando CPF aleatório e válido")
            print(gerarCPF())
        case 5:
            titulo("Calculando média")
            print(f"A média entre os valores informados é de : {calcularMedia(124,56,12,78)}")

        case 6:
            titulo("Maior valor")
            print(f'O maior valor entre os informados é de : {maiorVal(453,44,545454,5,4,2,4,6,75,3)}')

        case 7:
            print("FIM DO PROGRAMA")
            break

        case _ :
            print("OPÇÃO INCORRETA")

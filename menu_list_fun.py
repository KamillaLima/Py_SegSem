#Preencher uma lista com 10 elementos float.

def mostrarMenu():
    print("""
               ~~~~~~~~ MENU ~~~~~~~~
               [0] - Sair do programa
               [1] - Preencher a lista
               [2] - Exibir a lista 
               [3] - Somar elementos
               [4] - Média da lista
               [5] - ELementos acima da média
               [6] - Maior e menor item da lista
               [7] - Exibir apenas os itens negativos
               [8] - Indice ímpar
       """)

def  preencheLista(l): #l é chamado de parametro formal,que é utilizado apenas na função
    for cont in range(0, 10, 1):
        elemento = float(input(f"Digite o {cont} elemento: "))
        l.append(elemento)


def exibeLista(l):
    for i in range(0, len(l), 1):
        print(f"Elemento {i + 1} = {l[i]}")


def somaElementos(l):
    soma = 0
    for i in range(0, len(l), 1):
        soma += l[i]
    return soma
    #NUNCA colocar print ou input dentro de uma função !

def calcularMedia(l):
    return somaElementos(l) / 10 #realizo a soma dos elementos da lista atraves da função somaElementos(l) e
#em seguida ja faço a media
#No menu,eu nao preciso chamar a função somaElementos antes de calcularMedia,posso preencher a lista e ja chamar
#a calcularMedia sem problemas


def acimaMedia(l):
    MediaAcima = 0
    for item in range(0,10,1):
        if l[item] > calcularMedia(l):
            MediaAcima +=1
    return MediaAcima

def maiorItem(l):
    for item in range(0,10,1):

        if item==0:
            maior= l[item]
            menor = l[item]

        if maior < l[item]:
            maior = l[item]

        if menor > l[item]:
            menor = l[item]
    return maior,menor
#o return vem em formato de tupla

def elementoNegativo(l):
    elemNeg = []
    for item in range(0, 10, 1):
        if l[item] < 0:
            elemNeg.append(l[item])
    return elemNeg


def indiceImpar(l):
    indiceImpar = []
    for item in range(0,10,1):
        if (item % 2) !=0:
            indiceImpar.append(l[item])
    return indiceImpar


def estaNaLista(l):
    for itens in range(0, 10, 1):
        if numero == l[itens]:
            print(f"O numero {numero} está presente!")
        else:
            print(f"O número {numero} não está presente")


#PROGRAMA PRINCIPAL
lista = []
while True:
    mostrarMenu()
    opcao = int(input("Digite a opção:"))
    if opcao == 0:
        print("Volte sempre :)")
        break
    elif opcao==1:
        preencheLista(lista) # lista é chamada de parametro real,que é utilizado no programa principal
    elif opcao==2:
        exibeLista(lista)
    elif opcao==3:
        SOMA = somaElementos(lista)
        print(f"A soma dos elementos é de {SOMA}")
        #outra forma:
        #print(f"Soma = {somaElementos(lista)}")
    elif opcao == 4:
        print(f'A média é de : {calcularMedia(lista)}')

    elif opcao == 5:
        print(f"{acimaMedia(lista)} elemento(s) estão acima da média")
    elif opcao == 6:
        print(f"O maior item da lista é {maiorItem(lista)[0]} e o menor item da lista é {maiorItem(lista)[1]}")

    elif opcao == 7:
        print(f"Os elementos negativos presentes na lista são : {elementoNegativo(lista)}")

    elif opcao == 8 :
        print(f"Os elementos presentes nos indices impares são {indiceImpar(lista)}")

    elif opcao == 9 :
        numero = float(input("Informe o valor que você gostaria de saber se está incluido: "))
        estaNaLista(lista)

#
# EXERCÍCIOS:
# 9 - Verificar se um elemento passado por parâmetro está na lista
# 10 - Guardar numa segunda lista boleana True caso o elemento esteja acima da média, caso contrário False

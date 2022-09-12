#DEFINIÇÃO DOS SUBALGORITMOS
"""" Método de pesquisa sequencial
PROTÓTIPO: pesquisaMPS(l : lista,elem : float ):Boolean"""


def pesquisaMPS(l,elem):
    encontrou = False
    for i in range(10):
        if l[i] == elem:
            encontrou = True
            break
    return encontrou


"""Efetua a ordenação da lista
PROTÓTIPO: ordenaLista"""
def ordenaListaCres(l):
    for travado in range(9):
        for proximo in range(travado+1,10,1):
            if l[travado] > l[proximo]:
                aux = l[travado]
                l[travado] = l[proximo]
                l[proximo] = aux
    return l
def ordenaListaDecres(l):
    for travado in range(9):
        for proximo in range(travado+1,10,1):
            if l[travado] < l[proximo]:
                aux = l[travado]
                l[travado] = l[proximo]
                l[proximo] = aux
    return l

def ordenaListaTipo(l,tipo):
    if tipo == 1:
        return ordenaListaCres(l)
    if tipo == -1:
        return ordenaListaDecres(l)


"""Método de pesquisa binário
PROTÓTIPO : pesquisaMPB(l:lista,elem : float) : Boolean"""
def pesquisaMPB(lista,elem):
    inicio = 0
    fim = 9
    encontrou = False
    for i in range(inicio,fim+1 , 1):
        quebra = (inicio + fim)//2
        if elem == lista[quebra]:
            encontrou = True
            break
        elif elem > lista[quebra]:
            inicio = quebra + 1
        else: #entao o elem será menor do que o lista[quebra]
            fim = quebra - 1
    return encontrou


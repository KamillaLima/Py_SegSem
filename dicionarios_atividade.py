#Bianca Teixeira  92831
#Kamilla Lima 96112
#1TDSA

def cadastrarDisc(d,lista):
    while True:
        disciplina = input("Disciplina......: ")
        while vefCampoVazio(disciplina)==False or disciplina.isnumeric() == True:
            disciplina = input("Disciplina......: ")
        if disciplina == ".":
            break
        d["Disciplina"] = disciplina
        media = float(input("Média anual.....: "))
        while vefCampoVazio(media)==False or vefMedia(media) == True:
            media = float(input("Média anual.....: "))
        d["Media"] = media
        if vefStatus(media):
            d["Status"] = "APROVADO"
        else:
            d["Status"]="REPROVADO"
        lista.append(d.copy())
        print(f'Status..........: {d["Status"]}')
        print()

def vefCampoVazio(campo):
    return campo!=""

def vefMedia(valor):
    return valor <0 or valor>10

def vefStatus(nota):
    return nota >=6


def mostrarResultados():
    print("ola mundo")

disciplinas = []
pessoa={}
while True:
    print("\nCADASTRO DISCIPLINAS")
    print("0-SAIR")
    print("1-Cadastrar as disciplinas")
    print("2-Listar o registro completo\n")

    opcao = int(input("Opção desejada: "))
    match(opcao):
        case 0:
            print("PROGRAMA FINALIZADO!")
            break
        case 1:
            print("Cadastrar as disciplinas\n")
            cadastrarDisc(pessoa,disciplinas)
        case 2:
            print("\nLISTANDO O REGISTRO")
            for i in range(0,len(disciplinas),1):
                print(f'Disciplina......... {disciplinas[i]["Disciplina"]}')
                print(f'Média Anual........ {disciplinas[i]["Media"]}')
                print(f'Status............. {disciplinas[i]["Status"]}')
                print()

        case _:
            print("Escolha uma opção! ")
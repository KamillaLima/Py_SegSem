"""while True:
    opcao = int(input("Digite uma opção: "))
    match (opcao):
        case 1 :
            print("valorum")
            menuDois = int(input("Opcao no menu um:"))
            match (menuDois):
                case 1:
                    print("primeiro valor")
                case 2:
                    print("valor dois")
                case _ :
                    print("Inválido")
        case 2 :
            print("valordois")
        case 3:
            print("valortres")
        case _ :
            print("opção inválida")

#diferente do java,eu nao preciso colocar um break


nome = "kamilla "
print(nome or "digite algo")
#se a variavel nome estiver nome="" será exibido "digite algo"

a = ""
b= 0
c = True
d = "ola mundo"
print(a or b or c or d )
# Se o a NAO estiver vazio,será printado APENAS a variavel A
# Se o b NAO for zero,será printado APENAS a variavel B
# se o c NAO for falso,será printado APENAS a variavel C
# se o d NAO estiver vazio,será printado APENAS a variavel D

idade = int(input("Informe a sua idade:"))
print("maior de idade") if idade>=18 else print("Idade inválida")
# coloca o primeiro if e antes dele coloca a mensagem pra ser exibida caso ele seja true

venda = 100
desconto = venda * 0.5 if venda>400 else venda *0.2
# essa variavel desconto esta sendo usada tanto no if quanto no else,entao nesse comando nao preciso repetir ela
print(desconto)

"""
"""1. Dada uma frase, contar quantas palavras existem nela
    obs: 
    Amanha é sábado (3)
    Amanha é.sábado (3)
    Amanha,é.sábado (3)
    Amanha                é sabado (3)"""


# palavra = "                     Amanha,é            .sabado     92323 ,ddddd".replace(",", " ").replace("."," ").strip().split()
# print(len(palavra))
#




"""
Exercício:
1. Fazer uma função chamada 'isReal(string)' que retorne True caso a string seja do tipo float e false caso nao seja
"""
# def isReal(String):
#     Arrumado = String.replace(".","")
#     if Arrumado.isnumeric() :
#         return True
#     else:
#         return False
#
#
# print(isReal("237"))
"""
2. Dado um salário, informar se a pessoa paga imposto de renda (utilizar o operador ternário)
"""
# salario = float(input("Informe o seu salário atual"))
# print("você deverá pagar impostos") if salario*12>=28559.70 else print("Você não deverá pagar impostos de renda")


"""3. Dado um salário, informar se a pessoa paga INSS (utilizar o operador ternario)"""

# salario = float(input("Informe o seu salário atual: "))
# print("voce deve pagar INSS") if salario >=1212.00 else print("voce NAO deverá pagar o INSS")


"""4. Dado um salario, mostrar quanto a pessoa paga de INSS (utilizar o operador ternario)
   [pesquisar os indices da tabela de INSS]"""

# salario = float(input("Informe o seu salário atual: "))

"""5. Dados dois valores e um sinal (+, -, /, //, *, %), fazer o calculo devido (utilizar o match).
    Restrições: Em caso de divisao o segundo valor nao pode ser zero"""

# valorUm = int(input("Informe o primeiro valor:"))
# valorDois = int(input("Informe o segundo valor:"))
#
#
# ope = int(input("Informe qual das operações voce deseja realizar:\n"
#             "[1] +\n"
#             "[2] - \n"
#             "[3] /\n"
#             "[4] // \n"
#             "[5] * \n"
#             "[6] %\n"))
# match(ope):
#     case 1:
#         resultado = valorUm + valorDois
#         print(resultado)
#     case 2 :
#         resultado = valorUm - valorDois
#         print(resultado)
#     case 3 :
#         resultado = valorUm / valorDois
#         print(resultado)
#     case 4:
#         resultado = valorUm // valorDois
#         print(resultado)
#     case 5 :
#         resultado = valorUm * valorDois
#         print(resultado)
#     case 6:
#         resultado = valorUm % valorDois
#         print(resultado)
#     case _ :
#         print("OPERAÇÃO INCORRETA")


"""6. Dados os 4 dígitos da placa de um carro, exibir o dia do rodizio do mesmo (utilizar o match):
    Finais 1 e 2: Segunda
    Finais 3 e 4: Terça
    Finais 5 e 6: Quarta
    Finais 7 e 8: Quinta
    Finais 9 e 0: Sexta"""

placa = (input("Informe a placa: "))
val= int(placa[-1]) if len(placa) == 4 else print("PLACA INCORRETA")
match(val):
    case 1 :
        print("SEGUNDA")
    case 2:
        print("SEGUNDA")

    case 3:
        print("TERÇA")
    case 4:
        print("TERÇA")

    case 5:
        print("QUARTA")
    case 6:
        print("QUARTA")

    case 7:
        print("QUINTA")
    case 8:
        print("QUINTA")

    case 9:
        print("SEXTA")
    case 0:
        print("SEXTA")


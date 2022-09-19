#comandos principais
pessoa = {};
pessoa = {"nome":"Kamilla","idade":18,"sexo":"F","email":"Kamillalima868@gmail.com , kamilla38@gmail.com" }
print(pessoa["nome"]) #printa apenas o que esta dentro da chave nome
print(pessoa)#printa o dicionario por completo
pessoa["telefone"] = "11992240799" #adicionando o campo telefone no meu dicionário
del pessoa["sexo"] #deletando a chave e o value no campo sexo
print(pessoa.values()) # serão printados os values,no caso:Kamilla,19,kamillalima868@gmail.com
print(pessoa.keys()) # serão printadas as chaves,no caso:nome,idade,sexo,email
print(pessoa.items()) # printa tanto o value quanto a key,os valores são dividos em tupplas
pessoa["nome"] = "Kamilla de Lima Rodrigues"  # alterando um valor já existente no dicionário
for k,v in pessoa.items() :
    print(f"{k}----------{v}")
    #printando a chave e valor






####usando funçõe
# pessoa1 = {}
# def preenchInfo(pessoa1):
#     pessoa1["nome"] = str(input("Informe o nome completo: "))
#     pessoa1["idade"] = int(input("Informe sua idade: "))
#     pessoa1["sexo"] = str(input("Informe o seu sexo: "))
#     pessoa1["email"] = str(input("Informe o seu email: "))
#
#
# def exibeInfo(pessoa1):
#     for k,v in pessoa1.items():
#         print(f"{k}------------{v}")
#
#
# ####programa principal###################################
# preenchInfo(pessoa1)
# exibeInfo(pessoa1)

# # -------- DESAFIO: Consistir os dados - não permitir brancos - e numericos onde deve ter
def preencheDic(dic):
    dic["nome"]= str(input("Informe o seu nome completo: ")).strip()
    while dic["nome"] == "" or dic["nome"].isnumeric()==True:
        dic["nome"]= str(input("Informe o seu nome completo corretamente: ")).strip()

    idade = str(input("Informe sua idade: ")).strip()
    while idade== "" or  idade.isnumeric() == False:
       idade = str(input("Informe sua idade corretamente: "))
    dic["idade"] = int(idade)


def salvarUsuario(l,dic):
    preencheDic(dic)
    l.append(dic.copy())



usuarios = []
usuario = {}
opcao = "S"

while True:
    print("CADASTRANDO USUÁRIOS NO SISTEMA: ")
    salvarUsuario(usuarios, usuario)
    opcao = input("Deseja cadastrar ooutro usuário?[S] ou [N]").upper()
    if opcao=="N": break

print("Os usuários cadastrados em nosso sistema são: ")
for i in range(0, len(usuarios), 1):
    print(f"Nome = {usuarios[i]['nome']}",end="   ")
    print(f"Idade = {usuarios[i]['idade']}\n")
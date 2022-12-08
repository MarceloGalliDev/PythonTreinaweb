from dono import Dono
from cachorro import Cachorro_5

print(20*"-")
print("1. Cadastrar usuário")
print("2. Cadastrar usuário")
print("3. Cadastrar usuário")
print("4. Cadastrar usuário")
print("5. Cadastrar usuário")
print("6. Cadastrar usuário")
print("7. Cadastrar usuário")
print("8. Cadastrar usuário")
print(20*"-")

opcao = int(input("Escolha a opção: "))
global dono

if opcao == 1:
    nome_usuario = input("Digite o nome do usuário: ")
    dono = Dono(nome_usuario)
elif opcao == 2:
    nome_cachorro = input("Digite o nome do cachorro: ")
    idade_cachorro = input("Digite a idade do cachorro: ")
    cor_cachorro = input("Digite a cor do cachorro: ")
    qtd_bolinhas_cachorro = input("Digite a quantidade de bolinhas do cachorro: ")
    cachorro = Cachorro_5(nome_cachorro, idade_cachorro, cor_cachorro, qtd_bolinhas_cachorro, dono=dono)


    
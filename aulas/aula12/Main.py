import Pessoa
import os
def limpar():os.system('cls')

res = 0
alterar = 0
limpar()
def pergunta():
    res = int(input("Deseja cadastrar uma nova pessoa? 1 - SIM ou 0 - NÂO: "))
    return res

cadastro = []
def cadastrar():
    res = pergunta()
    while(res == 1):
        nome = str(input("Digite o nome da pessoa: "))
        idade = int(input("Digite a idade da pessoa: "))
        cargo = str(input("Digite o cargo da pessoa: "))
        salario = float(input("Digite o salario da pessoa: "))
    
        cadastro.append(Pessoa.Pessoa(nome,idade,cargo,salario))
        res = pergunta()
    
cadastrar()
def mostrar():
    print("{:<4}{:<10}{:<7}{:<10}{:<7}"
          .format("Nº","Nome","Idade","Cargo","Salário"))
    y = 1
    for x in cadastro:
        print("{:<4}{:<10}{:<7}{:<10}{:<7}"
              .format(y,
                  x.get_nome(),
                  x.get_idade(),
                  x.get_cargo(),
                  x.get_salario()
              ))
        y =+1
mostrar()
def alterar():
    linha = int(input("Digite a linha que deseja alterar: "))
    opcao = int(input("Escolha as opções: \n1 - Nome\n2- Idade\n3 - cargo\n4 - Salario\n"))
    if(opcao==1):
        nome = str(input("Digite o novo nome: "))
        cadastro[linha].set_nome(nome)
    elif(opcao==2):
        idade = str(input("Digite a nova idade: "))
        cadastro[linha].set_idade(idade)
    elif(opcao==3):
        cargo = str(input("Digite o novo cargo: "))
        cadastro[linha].set_cargo(cargo)
    elif(opcao==4):
        salario = str(input("Digite o novo salário: "))
        cadastro[linha].set_salario(salario)
    else:
        print("Valor Incoreto!")
alterar()
def remover():
    linha = int(input("Digite a linha que deseja remover: "))
    res = int(input(f"Certeza que deseja remover a linha {linha}?\n1 - Sim \n0 - Não\n"))
    if(res==1):
        cadastro.pop(linha)
        print("Linha removida com sucesso!")
mostrar()
remover()
mostrar()

def interface():
    opcao = int(input("Escolha as opções: \n1 - Cadastrar\n2- Alterar\n3 - Remover\n4 - Mostrar\n5 - Encerrar\n"))
    if(opcao==1):
        cadastrar()
    elif(opcao==2):
        alterar()
    elif(opcao==3):
        remover()
    elif(opcao==4):
        mostrar()
    elif(opcao==5):
        return
    else:
        print("Valor Incoreto!")
interface()
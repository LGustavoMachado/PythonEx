from random import randint      #IMPORTEI PARA FAZER O SORTEIO DOS NÚMEROS

dados = {}              #Dicionario
lista = []              #Lista
len(lista)
def menu (): #FUNCAO MENU

    print("=" *20, "MENU","="*20)
           
    #OPCÕES
    print("1 - Nova inscrição")
    print("2 - Visualizar inscrição")           
    print("3 - Encerrar")
    opcao = int(input("\nDigite a opção:"))
    len(lista) #MEDE MINHA LISTA
    return opcao

def inscricao (): #FUNCAO INSCRICAO
    numero = randint(100,1000)  #SORTEI DOS NÚMEROS
    dados['Voucher'] = numero   #O NUMERO SORTEADO
    dados['nome'] = input ('Digite seu nome: ')
    dados['e-mail'] = input('Digite seu email: ')
    dados['telefone'] = input('Digite seu telefone: ')
    dados['curso'] = input('Digite o Curso: ')
    lista.append(dados.copy())  #ESTOU COLOCANDO O DICIONARIO NA LISTA

def visual(): #FUNCAO VISUAL
    for usuario in lista:
       print()
       for dado, valor in usuario.items():
           print(f"{dado}: {valor}")

def erro(): #FUNCAO ERRO
        print("Erro... Digite um número válido!!")
        
    
    
while True: #ENQUANTO FOR VERDADEIRO ELE IMPRIMIRÁ AS FUNCAO
    opcao = menu() #Chamei a funcao menu

    if(opcao == 1):  #Se a opcao digitada for 1, vai chamar a funcao inscricao
        inscricao()  #Por estar em um looping, irá mostrar Menu novamente
    elif(len(lista) < 1 and opcao == 2):#Se a lista estiver sem dicionarios imprime nenhuma "Nenhuma inscrição" e mostra novamente o menu!
        print("Nenhuma inscrição!!") 
        menu()
    elif(opcao == 2):
        visual()    #Se for igual a 2 e tiver algo no menu irá chamar a funcao Menu
    elif(opcao == 3):   
        print("Encerrando...") #Funcao 3, da o break(para), parando o looping
        break
    else:   
        erro() #Aqui perde um número válido, caso não for igual a 1,2 e 3
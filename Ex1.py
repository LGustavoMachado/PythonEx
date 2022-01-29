sair = " "        #Aqui estou declarando que a variavel está vazia
#Enquanto 0 não for ==, ele vai repetir!
while(0 != sair):
    print("Classificação de ensino")
    aluno = input("Nome do aluno: ")    
    idade = int(input("Idade do aluno: "))
#Entrada de nome do aluno e idade
    
    print("\n" * 25)    #Aqui mostra o que foi digitado
    print("Nome da criança: ",aluno,"\nIdade: ", idade, "\n")

    if(idade >= 1 and idade <= 5): #Se aluno tiver entre 1 e 5, ele escreverá essa mensagem
        print("O aluno(a) ", aluno, " tem ", idade, " anos e está no ensino infantil.\n" )
    elif(idade >= 6 and idade <= 10): #Entre 6 e 10
        print("O aluno(a) ", aluno, "tem", idade, " anos e está no ensino fundamental I.\n")
    elif(idade >= 11 and idade <= 14):#Entre 11 e 14
        print("O aluno(a) ", aluno, "tem", idade, " anos e está no ensino fundamental II.\n")
    elif(idade >= 15):#acima de 15 anos
        print("O aluno(a) ", aluno, "tem", idade, " anos e está no ensino médio.\n")
    else:
        print("Ops!! Ocorreu um erro, tente novamente\n") #Caso a pessoa declare que tem menos que 0 
    
    # Entrada perguntando se deseja sair, se a pessoa digitar 0, vai sair do looping do While true, porque o while se tornará falso.
    sair = int(input("Deseja continuar? 0 - Sair    1 - Continuar"))
    
print("Finalizando...")







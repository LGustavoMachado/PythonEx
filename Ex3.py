def fasesresult (fase):   #função recebe a fase como parametro e retorna a matriz
    for l  in range(0, 2):
        for c in range(0, 4):
            print("[",fase[l][c],"]", end =" ")
        print()
    return fase 

def regras (): #Função das regras
    print("\n\n\nBem vindo ao jogo do Hotel dos Animais.\nRegras do jogo:")
    print("• O rato não pode ficar ao lado do gato.")
    print("• O cão não pode ficar ao lado do osso.")
    print("• O gato não pode ficar ao lado do cão.")
    print("• O queijo não pode ficar ao lado do rato.\n")
    fase = [[1,2,3,4], [5,6,7,8]]  #Posicao, para especificar as posiçoes
    print("Especificando posições:") 
    fasesresult(fase);  

def fase1 (): #Funcao da fase 1 com funcao "fasesresult enviando a matriz "fase"
    print("Bem vindos a fase 1!")
    print("Na fase 1 você deve ALOCAR o RATO e o GATO na seguinte matriz que representa os quartos.")
    print("Os quartos com [*] estão ocupados")
    fase = [["*","*"," ","G"],["R"," ","*","*"]]
    fasesresult(fase);
    posicaoGato = int(input("Em qual posição quer o Gato? "))
    if(posicaoGato == 3):   #Se a posição do gato for igual ao lugar 3 ele entre no if
        fase[0][2] = "G"    #entra na linha 0 , posição 2
        fasesresult(fase); #imprime as posições
    else:       #Caso não for igual a 3, voce perdeu o jogo
        print("\n\nVocê perdeu!")
        loopFases(); #Repete o loop, para o jogador tentar novamente
    posicaoRato = int(input("Em qual posição quer o Rato? "))
    if(posicaoRato == 6): #Aqui acontece se a posicao do rato for igual 6
        fase[1][1] = "R"
        fasesresult(fase);
    else: # Se não for igual a 6, você perde e o jogo se reinicia novamente.
        print("\n\nVocê perdeu!")
        loopFases();
    return posicaoGato

def fase2():    #Funcão da fase 2, se repete igual a da primeira
    print("\nMuito bem, voce passou para segunda fase!\n")
    print ("Nessa segunda fase. Você alocará 2 cães e 1 osso.")
    fase = [[" ","*","*","*"],["*","C"," "," "]]
    fasesresult(fase);  #Aqui sempre estou imprimindo as posições
    posicaoCachorro1 = int(input("Em qual posição quer o primeiro cachorro? "))#entrad
    if(posicaoCachorro1 == 7 or posicaoCachorro1 == 8):#posicao do cachorro por ser 2
        if(posicaoCachorro1 == 7): #Aqui verifico se ele é 7 e coloca ele no lugar 7
            fase[1][2] = "C"
        else:       #Caso não for igual a 7, só resta o lugar 8
            fase[1][3] = "C"
    else:
        print("\n\nVocê perdeu!")
        loopFases();
    fasesresult(fase);
    posicaoCachorro2 = int(input("Em qual posição quer o segundo cachorro? "))
    #Caso a pessoa digite a mesma vaga, vai dizer que ja foi preenchida e pergunta novamente
    while(posicaoCachorro2 == posicaoCachorro1): 
        print("Está vaga já foi preenchida!")
        print("Digite novamente!")      #Aqui eu pergunto novamente a posição porque está dentro do looping
        posicaoCachorro2 = int(input("Em qual posição quer o segundo cachorro? "))
    if(posicaoCachorro2 == 7 or posicaoCachorro2 == 8):
        if(posicaoCachorro2 == 7):
            fase[1][2] = "C"
        else:
            fase[1][3] = "C"
    else:
        print("\n\nVocê perdeu!")
        loopFases();
    fasesresult(fase);
    posicaoOsso = int(input("Em qual posição quer o osso? "))
    if(posicaoOsso == 1):
        fase[0][0] = "O"
    else:
        print("\n\nVocê perdeu!")
        loopFases();
    fasesresult(fase);
def fase3(): # Funcao fase 3
    print("\nParabéns, você passou para a terceira fase!!!\n")
    print("Na terceira fase você terá que alocar 1 Gato, 1 Rato e 1 Osso.")
    fase = [[" ","*","*","*"],[" ","G"," ","*"]]
    fasesresult(fase); #uso a funcao para imprimir a matriz
    posicaoGatoFase3 = int(input("Em qual posição quer o Gato? "))
    if(posicaoGatoFase3 == 7):
        fase[1][2] = "G"
    else:
        print("\n\nVocê Perdeu!")
        loopFases();
    fasesresult(fase);
    posicaoRatoFase3 = int(input("Em qual posição quer o Rato? "))
    if(posicaoRatoFase3 == 1):
        fase[0][0] = "R"
    else:
        print("\n\nVocê perdeu!")
        loopFases();
    fasesresult(fase);
    posicaoOssoFase3 = int(input("Em qual posição quer o Osso?"))
    if(posicaoOssoFase3 == 5):
        fase[1][0] = "O"
    else:
        print("\n\nVocê perdeu!")
        loopFases();
    fasesresult(fase);   

def fase4():
    print("\nParabéns, você passou para a quarta fase!!\n")
    print("Bem vindo a quarta fase!!!\nAqui você deverá alocar 2 Queijos e 1 Osso.")
    fase = [[" "," "," ","*"], ["*", "R", "*", "*"]]
    fasesresult(fase);
    posicaoQueijo1Fase4 = int(input("Em qual posição deseja colocar o primeiro Queijo? "))
    if(posicaoQueijo1Fase4 == 1 or posicaoQueijo1Fase4 == 3):
        if(posicaoQueijo1Fase4 == 1):
            fase[0][0] = "Q"
        else:
            fase[0][2] = "Q"
    else:
        print("\n\nGame Over!!")
        loopFases();
    fasesresult(fase);
    posicaoQueijo2Fase4 = int(input("Em qual posição deseja colocar o segundo Queijo? "))
    while(posicaoQueijo2Fase4 == posicaoQueijo1Fase4):
        print("Você já escolheu esse lugar. Tente novamente!")
        posicaoQueijo2Fase4 = int(input("Em qual posição deseja colocar o segundo Queijo? "))

    if(posicaoQueijo2Fase4 == 1 or posicaoQueijo2Fase4 == 3):
        if(posicaoQueijo2Fase4 == 1):
            fase[0][0] = "Q"
        else:
            fase[0][2] = "Q"
    else:
        print("\n\nGame Over!!")
        loopFases();
    fasesresult(fase);
    posicaoOsso1Fase4 = int(input("Em qual posição desejar colocar o osso? "))
    if(posicaoOsso1Fase4 == 2):
        fase[0][1] = "O"
    else:
        print("\n\nGame Over!!!")
        loopFases();
    fasesresult(fase);   
    print("\nParabéns!!!!! Você zerou o jogo do hotel dos animais!!!\n")

def loopFases():   #Aqui é minha função para deixa no looping infinito
    while True: #Enquanto for verdadeiro vai chamar essas funções
        regras(); 
        fase1();
        fase2();
        fase3();
        fase4();        #Caso a pessoa queria parar ou continuar irá perguntar
        opcao = int(input("Deseja jogar novamente? Digite 1 - SIM     2 - NÃO : "))
        if(opcao == 2):# se a opcao for igual a 2, ele vai encerrar o looping com um break (para).
            print("Encerrando...")
            break
loopFases();# Aqui estou chamando a função loopFases.


        
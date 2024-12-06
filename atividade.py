   #LER ENTRADAS DO USUÁRIO
alunos=[]#
n1 = n2 = n3 = n4 = media = 0
nome=""
faltas=0
situacao=""
while True:
    escolha_menu = int(input("Escolha uma das opções do menu:"))#Variável que guarda a escolha do usuário
    if escolha_menu == 1:#se a escolha para realizar
        situacao = ""
        cont = 0#variavel que controla a repetição
        escolha_usuario= int(input("Digite a quantidade de alunos que você quer cadastrar:"))#variavel que guarda quantas vezes o código vai rodar
        while cont < escolha_usuario:
            nome= input("Digite o nome do aluno:")#ARMAZENA o nome do aluno
            n1=float(input("Digite a 1° nota:"))#as 4 notas do aluno
            n2=float(input("Digite a 2° nota:"))
            n3=float(input("Digite a 3° nota:"))
            n4=float(input("Digite a 4° nota:"))

            faltas= int(input(f"Digite a quantidade de faltas o {nome} tem:"))
            #calculo da média
            media= (n1+n2+n3+n4)/4
            print(media)
            if media >=8:
                situacao="aprovado acima da média"
            elif media >=5:
                recuperacao= float(input("digite a nota da recuperação:"))
                if recuperacao >=(10-media):
                    situacao= "aprovado na recuperação!"
                else:
                    situacao= "reprovaddo na recuperacao"
            else:
                situacao= "reprovado pela média!"
            #enviar os dados do aluno para a lista alunos
            alunos.append([nome, faltas, media, situacao])
            cont =+ 1
            #RELATORIO
        
    elif escolha_menu == 2: #relatorio
        alunos.append([nome, faltas, media, situacao])
        cont += 1
        print(alunos)
    elif escolha_menu == 3:# se o usuario escolheu encerrar 
        break #quebra a execucao do enquanto
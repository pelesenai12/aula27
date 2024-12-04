    #ler entradas do usuarios
cont = 0#variavel controla a repeticao
alunos = []
escolha_usuario= int(input("degite a quantidade de alunos que voce deseja cadastra:"))#variavel que guarda quantas vezes o codigo vai rodar
while cont < escolha_usuario:

    nome = input()#armazenar o nome do aluno
    nota1 = float(input())#ler 4 notas do aluno
    nota2 = float(input())
    nota3 = float(input())
    nota4 = float(input())

    faltas = int(input(f"degite a quantidade de faltas o {nome} tem:"))#calculo da media
    #calculo de
    media = (nota1+nota2+nota3+nota4)/4
    print(media)
    #logica da situação
    if faltas >31:
        situacao = "reprovado por falta"
    elif media >=8:
        situacao = "aprovado"
    elif media >=5:#recuperação
        recuperacao = float(input())#ler a nota da recuperação
        if recuperacao >= (10-media):
            situacao = "aprovado na recuperação"
        else:
            situacao = "reprovado na recuperação"
    else:
        situacao = "reprovado por media"
    #enviar os dados do aluno para a lista (alunos)  
    alunos.append([nome, faltas, media, situacao])
    cont =+ 1
#relatorio
print(alunos)

        


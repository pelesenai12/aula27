#declaracao as funcao
def saudacoes (hora_do_dia):#exibir a saudacao correspondente a hora
    #bom dia
    if (hora_do_dia >=0) and (hora_do_dia <=12):
        print("bom dia!!!!")  
        #condicao para dar boa noite
    elif(hora_do_dia >=13) and (hora_do_dia <=18):
        print("boa tarde!")
    else:
        print("boa noite!")
#fora da funcao 
#peco para o usuarioi dizer a hora atual
resposta=int(input("digite que horas sao:\n"))

saudacoes(resposta)
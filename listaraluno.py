def listaraluno ():
    id = int(input("informe o id do aluno: "))
    
    arquivo = open("sempescoco.csv", "r")

    conteudo = arquivo.readlines()
    exist = False
    for i in range(2,len(conteudo)):
        perereca = conteudo[i].split(";")
        if (int(perereca[0]) == id):
            exist = True
            print( "id:"+ perereca[0])
            print( "nome:"  + perereca[1])
            print("matricula:"+perereca[2])
            print( "idade:"+ perereca[3])
            print("nota:"+perereca[4])
            
    if not exist:
        print("alumo nao existe")

    arquivo.close()
   
listaraluno()
def editar():
    id = int(input("informe o id do aluno: "))
    
    arquivo = open("sempescoco.csv", "r")

    conteudo = arquivo.readlines()
    exist = False
    for i in range(2,len(conteudo)):
        perereca = conteudo[i].split(";")
        if (int(perereca[0]) == id):
            exist = True
            perereca[1] = input("digite o nome do aluno")
            perereca[2] = input("numero da matricula")
            perereca[3] = input("qual e a idadede")
            perereca[4] = input("qual e a nota do aluno")

            conteudo[i] = perereca[0] + ";" + perereca[1] + ";" + perereca[2] + ";" + perereca[3] + ";" + perereca[4] + "\n"
    
    if not exist:
        print("alumo nao existe")

    arquivo.close()
    arquivo = open("sempescoco.csv", "w")

    arquivo.writelines(conteudo)      

editar()
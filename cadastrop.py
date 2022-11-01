from re import S


def cadastro():
    a = open("sempescoco.csv","r") 

    conteudo = a.readlines()

    print(conteudo[-1])# ultimo elemento = 3

    V = conteudo[-1] 
    
    print(V.split(';'))

    a.close()

    n = input("digite o nome do aluno")
    m = input("numero da matricula")
    i = input("qual e a idadede")
    r = input("qual e a nota do aluno")


    a = open ("sempescoco.csv","a+")

    a.write( n )
    a.write( ";" )
    a.write( m )
    a.write( ";" )
    a.write( i )
    a.write( ";" )
    a.write( r )
    a.write( "\n" )
    

    a.close()



   
    
cadastro() 


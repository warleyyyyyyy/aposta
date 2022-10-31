def cadastro():

    n = input("digite o nome do aluno")
    m = input("numero da matricula")
    i = input("qual e a idadede")
    r = input("qual e a nota do aluno")


    a = open ("sempescoco.csv","a")

    a.write( n )
    a.write( ";" )
    a.write( m )
    a.write( ";" )
    a.write( i )
    a.write( ";" )
    a.write( r )
    a.write( "\n" )

cadastro()


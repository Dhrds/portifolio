#exercicio
while True:
    print('---------------escolha o exercicio---------------')
    print('''1-exercicio
2-exercicio
3-exercicio
4-sair
''')
    while True:
        try:
         opc=int(input())
        except ValueError :
            print('valor errado')
        else:
            break
        #------------------------------
    match opc :
     case 1 :
        lista_idade = []
        lista_sexo = []
        lista_name = []
        sexo = str()
        idade=int()
        for i in range (3):
         print('*****cadastro de alunos*****') 
         name=str(input('digite seu nome  '))         
         lista_name.append(name) 
#---------------------------------------------
         
         while sexo != 'm'  or sexo != 'f' :
          sexo=str(input('digite seu sexo (M/F)  '))  
          if sexo == 'm' or sexo == 'f' :
            break     
         lista_sexo.append(sexo) 

#--------------------------------------------------
         while True:
            try:
              idade=int(input('digite sua idade  '))      
              lista_idade.append(idade) 
            except ValueError :
                print('valor errado')
            else:
                break

#--------------------------------------
        print('quantidade de alunos masculinos  ', lista_sexo.count('m'))
        print('quantidade de alunos femininos  ', lista_sexo.count('f'))
        print('media das idades  ',sum(lista_idade)/len(lista_idade))
        print('A maior idade informada é  ',max(lista_idade))
        #----------------------------------------------------
     case 2 :
       while True:
        try :
         f=int(input('informe um numero '))
         t=int(1)
         conta=int(1)
         for i in range (f):
            t=t*conta
            conta += 1
         print('resultado  ',t)
        except ValueError :
            print('valor errado')
        else:
            break
        #--------------------------------------------
     case 3 :
        opcao=int()
        curso=[]
        sexolist=[]
        sexo3=str()
        while True :
            try:
             print('''=======escolha seu curso=======
             1-ciência da computação
             2-sistema da informaçao
             3-engenharia da computaçao
             4-engenharia mecatronica
             (-1) ENCERRAR
             ''')
             opcao=int(input())
             if ( opcao < 0):
                break
            except ValueError :
                print('valor errado')
            else:            
                curso.append(opcao)
#-------------------------------------------------------
                nome=str(input('informe seu nome  '))
                while True :
                   sexo3=str(input('informe seu sexo m/f  '))
                   if sexo3 == 'f' or sexo3 =='m' :
                       sexolist.append(sexo3)
                       break
  #--------------------------------------------
        print('''numeros de candidatos por vagas
        1-ciência da computação 60/''',curso.count(1),'''
        2-sistema da informaçao 40/''',curso.count(2),'''
        3-engenharia da computaçao 35/''',curso.count(3),'''
        4-engenharia mecatronica 70/''',curso.count(4),'''
        ''')
        #------------------------------------------------
        sexof=float((sexolist.count('f')*100)/len(sexolist))
        print('porcentagem de candidatos femininos ',sexof,'%')
        #------------------------------------------
        import statistics
        if  statistics.mode(curso) == 1 :
         print('curso mais escolido foi ciência da computação')
        if  statistics.mode(curso) == 2 :
          print('curso mais escolido foi sistema da informaçao')
        if  statistics.mode(curso) == 3 :
          print('curso mais escolido foi engenharia da computaçao')
        if  statistics.mode(curso) == 4 :
          print('curso mais escolido foi engenharia mecatronica')      
     case 4 :
        break

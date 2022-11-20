print('========ola=======')
n6=str(input('sair?'))
while (n6 != 'sair'):
    n1 = int(input('''escolha 1 numero de 1 a 100
'''))
    n2 = int(input('''escolha 2 numero de 1 a 100
'''))
    import random
    n3 =int(random.randint(1,100))
    print(n3)
    n4 =int(n1-n3)
    n5 =int(n2-n3)
    if (n4<0):
     n4 = n4*(-1) 
    if (n5<0):
     n5 = n5*(-1) 
    if (n4<n5):
     print('jogador 1 ganhou')
    else :
     print('jogador 2 ganhou')
    
print('fim')
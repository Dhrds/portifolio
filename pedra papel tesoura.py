from unittest import case

jg = str
while (jg != 'sair'):
 print('''=pedra papel tesoura=
 ''')
 jg = str(input('''sua vez
 '''))
 import random
 pc = int(random.randint(1,3))
 match pc :
  case 1 :
   print('pedra') 
   if (jg == 'pedra'):
    print('empate')
   if (jg == 'tesoura'):
    print('perdeu')
   if (jg == 'papel'):
    print('ganhou')
  case 2 :
   print('papel')
   if (jg == 'pedra'):
    print('perdeu')
   if (jg == 'tesoura'):
    print('ganhou')
   if (jg == 'papel'):
    print('empate')
  case 3 :
   print('tesoura')
   if (jg == 'pedra'):
    print('ganhou')
   if (jg == 'tesoura'):
    print('empate')
   if (jg == 'papel'):
    print('perdeu')







#dado booleano 
var_verdadeiro = True #significa que esta var e verdadeira

var_falso = False #significa que esta var e falsa
 
#se var_verdadeiro for true 
if var_verdadeiro == True: 
  #imprimir isso
  print('var_verdadeira é verdadeira')

#comparaçoes: == != > < >= <=
#comparaçoes: and or

1 == 1 and 1 == 2
#falso pois o and so funciona quando ambos sao verdadeiro

1 == 1 or 1 == 2
#verdade pois apenas um precisa ser verdade

a = int(input())
b = int(input())

if a > b:
  print(a, 'é maior que', b )

#se nao
else:
  print('nao deu certo o if')

#mini menu
opcao = input('escolha uma opçao: ')  

if opcao == '1':
  print('gabriel')

#se nao se
elif opcao == '2':
  print('felipe')

elif opcao == '3':
  print('maia')    

else:
  print('opçao invalida')  
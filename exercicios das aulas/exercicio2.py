#pedir as informaçoes ao usuario 
#ler a idade do recruta
idade = int(input('Digite sua idade: '))

#ler o peso do recruta 
peso = int(input('Digite seu peso: '))

#ler a altura do recruta 
altura = float(input('Digite sua altura: '))

#se idade >= 18 e peso >= 60kg e altura >= 1.70 
if idade >= 18 and peso >= 60 and altura >= 1.70:
  #imprimir que esta apto
  print('voce esta apto a se alistar')

else:
  print('requisitos nao alcançados ' '\n'
        'requisitos minimos''\n'
        '18 anos''\n'
        '60kg''\n'
        '1.70 de aoltura')


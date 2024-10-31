#variavel serve para guardar uma informaçao(valores, funçao, objeto, classe...)
nome = 'Gabriel'  #conteudo da variavel str 
 
#pritnt vai imprimir o conteudo da variavel
print(nome)


tipo = type(nome) #tag que mostra o tipo da variavel. 

#essa impressao vai imprimir o tipo da variavel var
print(tipo)

#variaveis podem ter varios tipos
nome = 'Gabriel'  #esta variavel contem um texto
idade = int(19)  #esta variavel contem um valor inteiro
altura = float(1.82)  #esta variavel contem um valor de ponto flutuante

#Ao utilizar virgula no print, os valores estao sendo concatenados
print(nome, 'tem', idade,'anos', 'e mede', altura,'cm')

#input serve para que o usuario determine o valor de uma variavel
nome = input('escreva seu nome: ') #o usuario vai digitar o nome
idade = input('escreva sua idade: ') #o usuario vai digitar sua idade
altura = input('escreva sua altura: ') #o usuario vai digitar sua altura

print(nome, 'tem', idade,'anos', 'e mede', altura,'cm')

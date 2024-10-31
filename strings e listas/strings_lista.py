lista_nomes = ['diego', 'maria', 'joao', 'gabriel']

# vai transformar a lista completa em str e imprimir
print(lista_nomes)

# vai imprimir o indice indicado da lista 
print(lista_nomes[0])

frase = 'oi, tudo ben?'

# imprime os indices de 0 a 6 na var frase
print(frase[0:6])

lista_nomes2 = ['diogo', 'mariana', 'cosmo', 'vanda']


# append adiciona ao final da lista
lista_nomes2.append('geralda')
lista_nomes2.append('antonio')

print(lista_nomes2)

lista_nomes3= ['diogo', 'mariana', 'cosmo', 'vanda', 'diogo']

# remove um item especifico da lista 
lista_nomes3.remove('vanda')

# remove o ultimo da lista como uma pilha 
lista_nomes3.pop()

# adiciona no indice que vc quer 
lista_nomes3.insert(1, 'creosvaldo')

# alterar diretamente no indice 

lista_nomes3[0] = 'robervania'

# vai contar e adicionar a var cont_joao quantos joao tem nessa lista
cont_joao = lista_nomes3.count['joao']

# imrprimir cont_joao
print(cont_joao)

print(lista_nomes3)

# limpa a lista
# lista_nomes.clear()


# len mostra o tamanho da lista 
# esta contando a lista frase 
print(len(frase))
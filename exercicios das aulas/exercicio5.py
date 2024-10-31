# Passo 1: Leia a quantidade de convidados
qtd_conv = int(input())

# Passo 2: Crie uma lista vazia para armazenar os nomes dos convidados
lista_con = []

# Passo 3: Pergunte o nome de cada convidado e adicione à lista
for i in range(qtd_conv):
  nome = input(f"Digite o nome do convidado {i + 1}: ")
  lista_con.append(nome)


# Passo 4: Imprima a lista de convidados
print(lista_con)
"""
Sequencias em python sempre começam com o índice zero. 
"""
nome = 'kevin'
print(len(nome))

print(nome[0]) #retorna o primeiro elemento da sequencia nome.

print(nome[-1]) # retorna o último elemento da sequencia nome.


"""
0   1  2  3  4
k   e  v  i  n
-5 -4 -3 -2 -1
"""

print(nome[0:4]) #slice faz um fatiamento, até o índice 4, mas não o inclui.

print(nome[1:-1])

print(nome[1:]) # retorna todos os índices depois do índice 1.

print(nome[:4]) # retorna todos os índices antes do índice 4.

print(nome[1:4:2]) #retorna os índices de 1 ao 4, sem incluir o 4, porém, de 2 em 2

#Debaixo dos panos o python está fazendo:
print(nome.__getitem__(slice(1, 4, 2)))

print(nome[::2]) # pega toda a sequencia de 2 em 2.

print(nome[::-1]) #retorna toda a sequencia de traz pra frente.


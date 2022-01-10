nome = 'kevin dias'

print(type(nome)) 

"""o resultado é classe str, que pode ser usada para instanciar um inteiro ou ponto flutuante por exemplo."""

print(str(1))




"""
Strings no python não são sequências de bytes em memória, são objetos de alto nível que implementam toda a complexidade do unicode.
"""

print('kevín'.encode())


"""
Como strings são objetos, possuímos métodos neles.
"""
print(nome.upper()) #strings com letra maiúscula
print(nome.capitalize()) #primeira letra maiúscula
print(nome.title()) #primeira letra de cada palavra em maiúsculo
print(nome.replace('k', 'q')) #retorna uma nova strings, substituindo o valor desejado.
print(nome.split('e')) # retorna uma lista sem o valor desejado
print(' '.join(['kevin', 'dias'])) # para juntar strings da melhor forma utilizamos .join()
print(len(nome)) #retorna o comprimento da string.

"""
Strings são imutáveis.
"""




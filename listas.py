"""
Para criar uma lista abra colchetes e insira os elementos dentro dela
"""

l = ['A', 'B', 'C']
print(l)
"""
Listas também são objetos
"""
print(type(l)) #é do tipo list

"""
Listas são sequencias mutáveis.
"""
l.append('D') #append adiciona novos itens na lista.
print(l)

l.sort(reverse=True) # retorna a lista ao contrário.
print(l)

"""
Podemos usar slice na lista
"""
print(l[0])

"""
Tipos mutáveis dentro de uma lista
"""
l2 = [1, 2, [4, 5, 6]]

m = l2[-1]
m.append(42)
print(m)

print(l2) # minha lista l2 também muda, mas não exatamente ela, o que mudou foi o objeto referenciado no ultimo indice na lista l2.
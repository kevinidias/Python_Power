"""
Para declara uma tupla uso ()
ou declaro tuple()
"""
t = ('A', 'B', 'C')
print(t)
"""
Tupla são sequencias imutáveis,significa que qualquer operação realizada irá gerar um novo objecto gerando o resultado.
"""

t2 = t + ('D', 'E')
print(t) # continua com os mesmo dados.
print(t2) # novo objecto gerado com t + os dados inseridos.

"""
Tuplas não possuem muitos métodos disponíveis. .count . index
"""
"""
Tuplas suportam armazenar qualquer tipo de objeto. string, int, float...
"""

t3 = ('A', 'B', 1, 3.14, (2j, len), [1, 2, 3]) # 1 tupla com 5 elementos sendo os 2 últimos sequencias.
print(t3)

"""
A vírgula é o mais importante na tupla.
"""
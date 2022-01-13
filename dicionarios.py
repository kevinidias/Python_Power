"""
Armazenam pares de chave e valor.
"""

d = {'nome': 'Kevin', 'cidade': 'paraíba', 'lat': 22.9, 'long': 55}
print(d)

"""
Dicionários não tem ordem. Chaves são objetos imutáveis.
"""

"""
Para acessar uma chave do dicionário usamos colchetes.
"""
print(d['nome'])

"""
Para atualizar essa chave, caso tentarmos usar uma chave que não existe é executado o KeyError.
"""
d['nome']='Kevin Dias'
print(d)

"""
Para verificar se a chave existe.
"""
print('kevinn' in d)

"""
Para verificar se o valor existe.
"""

print('paraíba' in d.values())


"""
Se quisermos retornar uma chave que não existe sem erro usamos. get que retorna None.
Para configurar uma mensagem caso um determinado valor não exista podemos passar outro argumento além da chave específica que nesse exemplo é 'd'
"""

print(d.get('d'))
print(d.get('d', 'Valor não existe'))

"""
Para saber a quantidade de chaves em um dicionário.
"""
print(len(d))

"""
Para saber todas as chaves do dicionário.
"""
print(d.keys())

"""
Para saber todos os valores do dicionário.
"""
print(d.values())

"""
Para ambos.
"""

print(d.items())

"""
Para deletar.
"""

del d['cidade']
print(d)

"""
Para adicionar/atualizar.
"""
d.update(Estado='RJ')
print(d)
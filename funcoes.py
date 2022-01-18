"""
comando def
"""

def f():
    return 42

print(f())

"""
Python executa o módulo de cima para baixo.
Toda função em python retorna algo, caso  não seja 
especificado o retorno é None,
"""

def f(a, b, c, *args, **kwargs): #parametros
    print(a, b, c, args, kwargs)
"""
Args é sempre uma tupla que agrupa os argumentos posicionais que não tem correspondencia na assinatura da função.
"""

"""
Kwargs é sempre um dicionário que agrupa os argumentos posicionais que não tem correspondencia na assinatura da função.
"""

f( 'A', 'B', 'C', 'D', 'E', z='z', w='w') 

def filter(**kwargs):
    for k, v in kwargs.items():
        print(k.split('__'), v)

filter(name__startswith='Kev', age__lt=25, city__endswith='sul')



def f(*args, **kwargs):
    print(args, kwargs)


t = 'A', 'B', 'C'
d = dict(z='Z', w='W')

f(*t, **d) # tupla e dicionário.
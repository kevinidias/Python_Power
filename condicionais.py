nome = 'kevin'


"Vogais maiúsculas"
for c in nome:
    if c in ('aeiou'):
        print(c.upper())
    elif c == 'n':
        print('@')
    else:
        print(c)

"""
True and True = True

True and False = False

True or True = True

True or False = True

False or False = False
"""
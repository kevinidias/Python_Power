row = 'Kevin', 'Rio de Janeiro', 23.5, 27.9

def f(t):
    nome, cidade, lat, long = t
    print(nome, cidade, lat, long)


if __name__ == '__main__':
    f(row)
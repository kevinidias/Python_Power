"""
While
Enquanto algo é verdadeiro ele executa o corpo do loop.
"""

nome = 'kevin'

print(nome, len(nome))

i = 0

while i < len(nome):
    print(nome[i])
    i += 1


"""
Sempre que temos um loop que precisa contar quantos passos ele irá dar é melhor usar o For
"""

for i, c in enumerate(nome): #índice e nome
    if c == 'e':
        continue # pula a condição e continua o loop
        break # assim que achar a condição para o loop
    print(i, c)
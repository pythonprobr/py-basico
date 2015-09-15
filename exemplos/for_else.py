palavra = input('Escreva uma palavra com x:')

for letra in palavra:
    if letra == 'x':
        break
else:
    print('Palavra sem "x"!')

print('Voce escreveu:', palavra)


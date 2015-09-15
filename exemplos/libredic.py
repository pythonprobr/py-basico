import sys

NOME_ARQ = 'pt_BR.dic'

arq = open(NOME_ARQ, encoding='iso8859-1')

for linha in arq:
    #octetos = linha.encode('utf-8', errors='replace')
    #sys.stdout.buffer.write(octetos)
    #linha = linha.rstrip()
    print(linha, end='')

#print(sys.stdout.encoding)

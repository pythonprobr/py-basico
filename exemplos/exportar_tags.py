import sys

import tag

def exportar(nome, lista):
	print(tag.tag(nome, *lista))


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Informe o nome da tag.')
        sys.exit(1)

    else:
        exportar(sys.argv[1], sys.argv[2:])

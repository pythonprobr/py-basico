"""
===========================================================
Exemplo de geração de elementos XML com uma função flexível
===========================================================

No caso mais simples, a função ``tag`` produz uma tag vazia::

    >>> tag('br')
    '<br />'
    >>> tag('img')
    '<img />'

Também é possível gerar tags com lista_atr::

    >>> tag('img', src='brasil.png')
    '<img src="brasil.png" />'
    >>> tag('input', name='cpf')
    '<input name="cpf" />'
    >>> tag('input', type='text', name='cpf')
    '<input name="cpf" type="text" />'

Pode-se gerar tags com conteúdo::

    >>> tag('p', 'Bom dia.')
    '<p>Bom dia.</p>'
    >>> tag('p', 'Bom dia.', class_='aviso')
    '<p class="aviso">Bom dia.</p>'

Se mais de um conteúdo é passado, múltiplas tags são geradas::

    >>> tag('p', 'Bom dia.', 'Boa tarde.', 'Boa noite.')
    '<p>Bom dia.</p>\\n<p>Boa tarde.</p>\\n<p>Boa noite.</p>'

"""

def tag(nome, *conteudos, **atributos):
    if atributos:
        lista_atr = []
        for chave, valor in sorted(atributos.items()):
            if chave.endswith('_'):
                chave = chave[:-1]
            lista_atr.append('{}="{}"'.format(chave, valor))
        lista_atr = ' ' + ' '.join(lista_atr)
    else:
        lista_atr = ''
    if conteudos:
        saida = []
        for item in conteudos:
            saida.append('<{0}{1}>{2}</{0}>'.format(nome, lista_atr, item))
        return '\n'.join(saida)
    else:
        return '<{0}{1} />'.format(nome, lista_atr)


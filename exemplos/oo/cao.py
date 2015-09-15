# coding: utf-8

"""
Cães são instâncias de mamíferos, porque ``Cao`` é uma
subclasse de ``Mamifero``::

    >>> rex = Cao('Rex')
    >>> isinstance(rex, Cao)
    True
    >>> isinstance(rex, Mamifero)
    True
    >>> issubclass(Cao, Mamifero)
    True


"""


class Mamifero(object):
    """vertebrados dotados de glândulas mamárias"""


class Cao(Mamifero):
    qt_patas = 4
    carnivoro = True
    nervoso = False

    def __init__(self, nome):
        self.nome = nome

    def latir(self, vezes=1):
        """
            >>> rex = Cao('Rex')
            >>> rex.latir()
            Rex: Au!
            >>> rex.nervoso = True
            >>> rex.latir()
            Rex: Au! Au!

        """
        # quando nervoso, late o dobro
        vezes = vezes + (self.nervoso * vezes)
        print(self.nome + ':' + ' Au!' * vezes)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Cao(%r)' % self.nome

    def __eq__(self, outro):
        return (isinstance(outro, Cao) and
            self.__dict__ == outro.__dict__)

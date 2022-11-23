class Conjunto:
    def __init__(self, *args) -> None:
        """Adiciona os elementos no conjunto conforme os valores recebidos.

        Args:
            args (list, number): os args passados devem ser do tipo lista ou um número.
        """
        elementos = []

        # se for passado apenas um parâmetro e este for do tipo lista
        if len(args) == 1 and type(args[0]) == list:
            for elemento in args[0]:
                elementos.append(elemento)

        else:
            for arg in args:
                # se o tipo desse elemento for uma lista
                if type(arg) == list:
                    elementos.append(Conjunto(arg))
                else:
                    elementos.append(arg)

        self.__elementos = elementos

    @property
    def elementos(self) -> list:
        """Permite o usuário a acessar os elementos (privados) do conjunto. 

        Returns:
            list: Elementos do conjunto em uma lista
        """
        return self.__elementos

    def __str__(self) -> str:
        """Retorna os elementos do conjunto formatados no padrão {elemento_1, elemento_2, ..., elemento_n}

        Returns:
            str: Elementos formatados conforme padrão citado acima
        """
        if len(self) > 0:
            ret = "{"
            for elemento in self.elementos:
                ret += str(elemento) + ", "
            ret = ret[:-2]
            ret += "}"
            return ret
        else:
            return "{} - CONJUNTO VAZIO"

    def __getitem__(self, posicao):
        """Método mágico que possibilita pegar o elemento de uma posição específica de um Conjunto, sem precisar passar (Conjunto.elementos).

        Args:
            posicao (int): Posição solicitada.

        Returns:
            int: elemento na posição solicitada.
        """
        return self.elementos[posicao]

    def __iter__(self):
        """Método mágico que possibilita iterar os elementos de um Conjunto sem precisar passar (Conjunto.elementos).
        """
        i = 0
        while i < len(self.elementos):
            yield self.elementos[i]
            i += 1

    def __len__(self) -> int:
        """Método mágico que possibilita saber o tamanho da lista de elementos de um Conjunto sem precisar passar (Conjunto.elementos)."""
        return len(self.elementos)

    def __eq__(self, conjunto) -> bool:  # igualdade usando '=='
        """Método mágico que possibilita verificar igualdade entre dois conjuntos usando apenas dois sinais de igualdade '=='.

        Args:
            conjunto (Conjunto): Conjunto a ser comparado com o Conjunto self.

        Returns:
            bool: retorna se o Conjunto passado após as igualdades '==' é igual ao Conjunto self.
        """
        return self.isEqual(conjunto)

    def __add__(self, conjunto):  # união usando '+'
        """Método mágico que possibilita realizar a união entre dois conjuntos usando apenas o sinal '+'.

        Args:
            conjunto (Conjunto): Conjunto a ser unido com o Conjunto self.

        Returns:
            bool: retorna o Conjunto resultante da união entre o Conjunto passado e o self.
        """
        return uniao(self, conjunto)

    def __sub__(self, conjunto):  # diferença usando '-'
        """Método mágico que possibilita realizar a diferença entre dois conjuntos usando apenas o sinal '-'.

        Args:
            conjunto (Conjunto): Conjunto a ser diferenciado com o Conjunto self.

        Returns:
            bool: retorna o Conjunto resultante da diferença entre o Conjunto passado e o self.
        """
        return diferenca(self, conjunto)

    def __mul__(self, conjunto):  # produto cartesiano usando '*'
        """Método mágico que possibilita realizar o produto cartesiano entre dois conjuntos usando apenas o sinal '*'.

        Args:
            conjunto (Conjunto): Conjunto que será usado para fazer o produto cartesiano com o Conjunto self.

        Returns:
            bool: retorna o Conjunto resultante do produto cartesiano entre o Conjunto passado e o self.
        """
        return produtoCartesiano(self, conjunto)

    def possui(self, elemento) -> bool:  # pertinência
        """Método usado para verificar se um elemento está contido no Conjunto self.

        Args:
            elemento (numeric | list): elemento que será verificado a pertinência.

        Returns:
            bool: retorna verdadeiro caso o elemento passado como parâmetro esteja contido no Conjunto self.
        """
        if elemento in self.elementos:
            return True
        return False

    def isSubconjunto(self, conjunto) -> bool:  # subconjunto
        """Método usado para verificar se o Conjunto self é subconjunto do conjunto passado como parâmetro.

        Args:
            conjunto (Conjunto | list): Conjunto ou lista que representa o conjunto que será verificado.

        Returns:
            bool: retorna verdadeiro caso o elemento passado como parâmetro seja subconjunto do Conjunto self.
        """
        # se o parâmetro passado for um conjunto
        if type(conjunto) == Conjunto:
            elementos = conjunto.elementos

            for elemento in self.elementos:
                if elemento not in elementos:
                    return False
            return True
        # se o parâmetro passado for uma lista representando um conjunto
        elif type(conjunto) == list:
            return self.isSubconjunto(Conjunto(conjunto))
        else:
            return False

    def isEqual(self, conjunto) -> bool:  # igualdade usando função
        """Método usado para verificar se o Conjunto self é igual ao conjunto passado como parâmetro.

        Args:
            conjunto (Conjunto | list): Conjunto ou lista que representa o conjunto que será verificado.

        Returns:
            bool: retorna verdadeiro caso o elemento passado como parâmetro seja igual ao Conjunto self.
        """
        # se o parâmetro passado for um conjunto
        if type(conjunto) == Conjunto:
            if self.isSubconjunto(conjunto) and conjunto.isSubconjunto(self):
                return True
            return False
        # se o parâmetro passado for uma lista que representa um conjunto
        elif type(conjunto) == list:
            return self.isEqual(Conjunto(conjunto))


def uniao(a, b) -> Conjunto:  # união usando função
    """Método usado para retornar a união dos dois Conjuntos passados como parâmetro.

        Args:
            a (Conjunto | list): Conjunto ou lista que representa um dos conjuntos da união.
            b (Conjunto | list): Conjunto ou lista que representa um dos conjuntos da união.

        Returns:
            Conjunto: retorna o Conjunto resultante da união entre os Conjuntos passados como parâmetro. 
    """
    retornoUniao = []

    for elemento in a:
        if elemento not in retornoUniao:
            retornoUniao.append(elemento)

    for elemento in b:
        if elemento not in retornoUniao:
            retornoUniao.append(elemento)

    return Conjunto(retornoUniao)


def intersecao(a, b) -> Conjunto:  # interseção
    """Método usado para retornar a interseção dos dois Conjuntos passados como parâmetro.

        Args:
            a (Conjunto | list): Conjunto ou lista que representa um dos conjuntos da interseção.
            b (Conjunto | list): Conjunto ou lista que representa um dos conjuntos da interseção.

        Returns:
            Conjunto: retorna o Conjunto resultante da interseção entre os Conjuntos passados como parâmetro. 
    """
    retornoIntersecao = []
    for elemento in a:
        if elemento in b:
            retornoIntersecao.append(elemento)
    return Conjunto(retornoIntersecao)


def diferenca(a, b) -> Conjunto:  # diferença usando função
    """Método usado para retornar a diferença entre o primeiro e o segundo Conjunto passado como parâmetro.

        Args:
            a (Conjunto | list): Conjunto ou lista que representa um dos conjuntos da diferença.
            b (Conjunto | list): Conjunto ou lista que representa um dos conjuntos da diferença.

        Returns:
            Conjunto: retorna o Conjunto resultante da diferença entre os Conjuntos passados como parâmetro. 
    """
    retornoDiferenca = []
    for elemento in a:
        if not b.possui(elemento):
            retornoDiferenca.append(elemento)
    return Conjunto(retornoDiferenca)


def conjuntoDasPartes(A):
    """Método usado para retornar o conjunto das partes do Conjunto passado como parâmetro.

        Args:
            a (Conjunto | list): Conjunto ou lista que representa o Conjunto que será usado para os cálculos.

        Returns:
            Conjunto: retorna o Conjunto resultante do conjunto das partes do Conjunto passado como parâmetro. 
    """
    B = len(A)
    elementos = [elemento for elemento in A]
    ps = []
    for i in range(2 ** B):
        w = f'{i:0{B}b}'
        q = [elementos[j] for j, bit in enumerate(w) if bit == '1']
        ps.append(Conjunto(q))
    return Conjunto(ps)


def produtoCartesiano(A, B):
    """Método usado para retornar o produto cartesiano dos dois Conjunto passados como parâmetro.

        Args:            
            A (Conjunto | list): Conjunto ou lista que representa um dos Conjuntos que será usado para os cálculos do produto cartesiano.
            B (Conjunto | list): Conjunto ou lista que representa um dos Conjuntos que será usado para os cálculos do produto cartesiano.

        Returns:
            Conjunto: retorna o Conjunto resultante do produto cartesiano entre os Conjuntos passados como parâmetro. 
    """
    lista_retorno = []
    for elemento_de_a in A:
        for elemento_de_b in B:
            lista_retorno.append(Conjunto([elemento_de_a, elemento_de_b]))
    return Conjunto(lista_retorno)

class Conjunto:
    def __init__(self, elementos: list = []) -> None:  # usar args pra aceitar
        """Adiciona os elementos no conjunto conforme os valores recebidos 

        Args:
            elementos (list, optional): _description_. Defaults to []. ALTERAR APOR *args

        Raises:
            ValueError: Caso o usuário passe algo diferente de uma lista como parâmetro do conjunto 
        """
        self.__elementos = elementos

        if not isinstance(elementos, list):
            raise ValueError('Passe apenas listas como parâmetro do conjunto')

    @property
    def elementos(self) -> list:
        """Permite o usuário a acessar os elementos (privados) do conjunto 

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
            for elemento in self.__elementos:
                ret += str(elemento) + ", "
            ret = ret[:-2]
            ret += "}"
            return ret
        else:
            return "{} - CONJUNTO VAZIO"

    def __getitem__(self, posicao):
        """Método mágico que possibilita pegar o elemento de uma posição específica de um Conjunto, sem precisar passar (Conjunto.elementos)

        Args:
            posicao (int): Posição solicitada 

        Returns:
            int: elemento na posição solicitada
        """
        return self.__elementos[posicao]

    def __iter__(self):
        i = 0
        while i < len(self.elementos):
            yield self.elementos[i]
            i += 1

    def __len__(self) -> int:
        return len(self.__elementos)

    def __eq__(self, conjunto) -> bool:  # igualdade usando '=='
        return self.isEqual(conjunto)

    def __add__(self, conjunto):
        return uniao(self, conjunto)  # união usando '+'

    def __sub__(self, conjunto):
        return diferenca(self, conjunto)  # diferença usando '-'

    def __mul__(self, conjunto):
        # produto cartesiano usando '*'
        return produtoCartesiano(self, conjunto)

    def possui(self, elemento) -> bool:  # pertinência
        if elemento in self.__elementos:
            return True
        return False

    def isSubconjunto(self, conjunto) -> bool:  # subconjunto
        elementos = conjunto.elementos

        for elemento in self.__elementos:
            if elemento not in elementos:
                return False
        return True

    def isEqual(self, conjunto) -> bool:  # igualdade usando função
        if self.isSubconjunto(conjunto) and conjunto.isSubconjunto(self):
            return True
        return False


def uniao(a, b) -> Conjunto:  # união usando função
    retornoUniao = []

    for elemento in a:
        if elemento not in retornoUniao:
            retornoUniao.append(elemento)

    for elemento in b:
        if elemento not in retornoUniao:
            retornoUniao.append(elemento)

    return Conjunto(retornoUniao)


def intersecao(a, b) -> Conjunto:  # Interseção
    retornoIntersecao = []
    for elemento in a:
        if elemento in b:
            retornoIntersecao.append(elemento)
    return Conjunto(retornoIntersecao)


def diferenca(a, b) -> Conjunto:  # diferenca usando função
    retornoDiferenca = []
    for elemento in a:
        if not b.possui(elemento):
            retornoDiferenca.append(elemento)
    return Conjunto(retornoDiferenca)


def conjuntoDasPartes(A):
    B = len(A)
    elementos = [elemento for elemento in A]
    ps = []
    for i in range(2 ** B):
        w = f'{i:0{B}b}'
        q = [elementos[j] for j, bit in enumerate(w) if bit == '1']
        ps.append(Conjunto(q))
    return Conjunto(ps)


def produtoCartesiano(A, B):
    lista_retorno = []
    for elemento_de_a in A:
        for elemento_de_b in B:
            lista_retorno.append(Conjunto([elemento_de_a, elemento_de_b]))
    return Conjunto(lista_retorno)

# e) produto cartesiano dos conjuntos A e B (também vale para o mesmo conjunto) (A * B)

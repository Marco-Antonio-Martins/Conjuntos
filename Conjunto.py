class Conjunto:
    def __init__(self, elementos: list = []) -> None:
        self.__elementos = elementos

        if not isinstance(elementos, list):
            raise ValueError('Passe apenas listas como parâmetro do conjunto')

    @property
    def elementos(self):
        return self.__elementos

    def __str__(self) -> str:
        if len(self) > 0:
            ret = "{"
            for elemento in self.__elementos:
                ret += str(elemento) + ","
            ret = ret[:-1]
            ret += "}"
            return ret
        else:
            return "{} - CONJUNTO VAZIO"

    def __getitem__(self, posicao):
        return self.__elementos[posicao]

    def __len__(self):
        return len(self.__elementos)

    def __eq__(self, conjunto) -> bool:  # igualdade usando '=='
        return self.isEqual(conjunto)

    def __add__(self, conjunto):
        return uniao(self, conjunto)  # união usando '+'

    def __sub__(self, conjunto):
        return diferenca(self, conjunto)  # diferença usando '-'

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

    for elemento in a.elementos:
        if elemento not in retornoUniao:
            retornoUniao.append(elemento)

    for elemento in b.elementos:
        if elemento not in retornoUniao:
            retornoUniao.append(elemento)

    return Conjunto(retornoUniao)


def intersecao(a, b) -> Conjunto:  # Interseção
    retornoIntersecao = []
    for elemento in a.elementos:
        if elemento in b.elementos:
            retornoIntersecao.append(elemento)
    return Conjunto(retornoIntersecao)


def diferenca(a, b) -> Conjunto:  # diferenca usando função
    retornoDiferenca = []
    for elemento in a.elementos:
        if not b.possui(elemento):
            retornoDiferenca.append(elemento)
    return Conjunto(retornoDiferenca)


# FALTA CRIAR AS FUNÇÕES:
# d) conjunto das partes do conjunto A
# e) produto cartesiano dos conjuntos A e B (também vale para o mesmo conjunto)

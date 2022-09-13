class Conjunto(): 
    elementos: list = []

    def __init__(self, elementos=[]) -> None:
        self.elementos = elementos

    def __str__(self) -> str:
        if len(self.elementos) > 0:
            ret = "{"
            for elemento in self.elementos:
                ret += str(elemento) + ","
            ret = ret[:-1]
            ret += "}"
            return ret
        else:
            return "{} - CONJUNTO VAZIO"

    def __eq__(self, conjunto) -> bool:
        return self.__isEqual(conjunto)

    def possui(self, elemento) -> bool:  # Pertinência
        if elemento in self.elementos:
            return True
        return False

    def isSubconjunto(self, conjunto) -> bool:  # Subconjunto
        elementos = conjunto.elementos

        for elemento in self.elementos:
            if elemento not in elementos:
                return False
        return True

    def __isEqual(self, conjunto) -> bool:  # Igualdade
        if self.isSubconjunto(conjunto) and conjunto.isSubconjunto(self):
            return True
        return False


def uniao(a, b) -> Conjunto:  # União
    retornoUniao = []

    for elemento in a.elementos:
        if elemento not in retornoUniao:
            retornoUniao.append(elemento)

    for elemento in b.elementos:
        if elemento not in retornoUniao:
            retornoUniao.append(elemento)

    ret = Conjunto(retornoUniao)
    return ret


def intersecao(a, b) -> Conjunto:  # Interseção
    retornoIntersecao = []
    for elemento in a.elementos:
        if elemento in b.elementos:
            retornoIntersecao.append(elemento)
    ret = Conjunto(retornoIntersecao)
    return ret

# FALTA CRIAR AS FUNÇÕES:
# c) diferença entre dois conjuntos A e B
# d) conjunto das partes do conjunto A
# e) produto cartesiano dos conjuntos A e B (também vale para o mesmo conjunto)

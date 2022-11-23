from Conjunto import *

# CRIANDO CONJUNTOS
A = Conjunto()
B = Conjunto(1, 2, 3)
C = Conjunto(1, 2, 3)
D = Conjunto([1, 2, 3], [4, 5, 6], [7, 8, 9])
E = Conjunto(1, 2, 3, 4, [1, 2, 3])


# FUNÇÕES DE TESTE
def testaVerElementos():
    print(f'Conjunto A: {A}')
    print(f'Conjunto B: {B}')
    print(f'Conjunto C: {C}')
    print(f'Conjunto D: {D}')
    print(f'Conjunto E: {E}')
    print('-'*50)


def testaPertinencia():
    print(f"O elemento 7 pertence ao conjunto A? {A.possui(7)}")
    print(f"O elemento 1 pertence ao conjunto B? {B.possui(1)}")
    print("O elemento {1,2,3} pertence ao conjunto D?", D.possui([1, 2, 3]))
    print('-'*50)


def testaSubconjuntos():
    print(f'A é subconjunto de B? {A.isSubconjunto(B)}')
    print(f'B é subconjunto de E? {B.isSubconjunto(E)}')
    print(f'E é subconjunto de B? {E.isSubconjunto(B)}')
    print('-'*50)


def testaIgualdade():
    print(f'O Conjunto B é igual ao C? {B == C}')
    print(f'O Conjunto B é igual ao A? {B.isEqual(A)}')
    print('-'*50)


def testaUniao():
    print(f'Conjunto E: {E}')
    print(f'Conjunto B: {B}')
    print('E união entre o Conjunto E e o Conjunto B (E + B) é')
    print(E+B)
    print('E união entre o Conjunto B e o Conjunto E (B + E) é')
    print(uniao(B, E))
    print('-'*50)


def testaIntersecao():
    print(f'Conjunto E: {E}')
    print(f'Conjunto C: {C}')
    print('A intersecao entre o Conjunto E e o Conjunto C é')
    print(intersecao(E, C))
    print('A intersecao entre o Conjunto C e o Conjunto E é')
    print(intersecao(C, E))
    print('-'*50)


def testaDiferenca():
    print(f'Conjunto A: {A}')
    print(f'Conjunto B: {B}')
    print('A diferença entre o conjunto A e B (A-B) é')
    print(diferenca(A, B))
    print('A diferença entre o conjunto B e A (B-A) é')
    print(B-A)
    print('-'*50)


def testeConjuntoDasPartes():
    print("O conjunto das partes de D é")
    print(conjuntoDasPartes(D), end="\n\n")
    print("O conjunto das partes de B é")
    print(conjuntoDasPartes(B))
    print('-'*50)


def testeProdutoCartesiano():
    print(f'Conjunto A: {A}')
    print(f'Conjunto B: {B}')
    print(f'Conjunto E: {E}')
    print(f'Produto Cartesiano de B e E é: {produtoCartesiano(B, E)}')
    print(f'Produto Cartesiano de A e C é: {A * C}')


# EXECUTANDO TESTES
testaVerElementos()
testaPertinencia()
testaSubconjuntos()
testaIgualdade()
testaUniao()
testaIntersecao()
testaDiferenca()
testeConjuntoDasPartes()
testeProdutoCartesiano()

from Conjunto import *

# CRIANDO CONJUNTOS
A = Conjunto([8, 7])
B = Conjunto([0, 1, 2])
C = Conjunto([2, 1, 0, 3])
D = Conjunto()
E = Conjunto([7, 8])


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
    print(f"O elemento 0 pertence ao conjunto B? {B.possui(0)}")
    print(f"O elemento 5 pertence ao conjunto D? {D.possui(5)}")
    print('-'*50)


def testaSubconjuntos():
    print(f'A é subconjunto de B? {A.isSubconjunto(B)}')
    print(f'B é subconjunto de C? {B.isSubconjunto(C)}')
    print(f'C é subconjunto de B? {C.isSubconjunto(B)}')
    print('-'*50)


def testaIgualdade():
    print(f'O Conjunto A é igual ao E? {A == E}')
    print(f'O Conjunto A é igual ao B? {A.isEqual(B)}')
    print('-'*50)


def testaUniao():
    print(f'Conjunto A: {A}')
    print(f'Conjunto B: {B}')
    print('A união entre o Conjunto A e o Conjunto B (A + B) é')
    print(A+B)
    print('A união entre o Conjunto B e o Conjunto A (B + A) é')
    print(uniao(B, A))
    print('-'*50)


def testaIntersecao():
    print(f'Conjunto B: {B}')
    print(f'Conjunto C: {C}')
    print('A intersecao entre o Conjunto B e o Conjunto C é')
    print(intersecao(B, C))
    print('A intersecao entre o Conjunto C e o Conjunto B é')
    print(intersecao(C, B))
    print('-'*50)


def testaDiferenca():
    print(f'Conjunto A: {A}')
    print(f'Conjunto B: {B}')
    print('A diferença entre o conjunto A e B (A-B) é')
    print(diferenca(A, B))
    print('A diferença entre o conjunto B e A (B-A) é')
    print(B-A)


# EXECUTANDO TESTES
testaVerElementos()
testaPertinencia()
testaSubconjuntos()
testaIgualdade()
testaUniao()
testaIntersecao()
testaDiferenca()

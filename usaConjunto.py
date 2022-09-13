from Conjunto import *
# CRIANDO CONJUNTOS
A = Conjunto([7, 8])
B = Conjunto([0, 1, 2])
C = Conjunto([2, 1, 0, 3])
D = Conjunto()
E = Conjunto([7, 8])


def testaVerElementos():
    A.verElementos()
    B.verElementos()
    C.verElementos()
    D.verElementos()
    E.verElementos()
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
    print(f'O Conjunto A é igual ao E? {A.isEqual(E)}')
    print(f'O Conjunto A é igual ao B? {A.isEqual(B)}')
    print('-'*50)


def testaUniao():
    print('Conjunto A')
    A.verElementos()
    print('Conjunto B')
    B.verElementos()
    print('A união entre o Conjunto A e o Conjunto B é')
    uniao(A, B).verElementos()
    print('-'*50)


def testaIntersecao():
    print('Conjunto B')
    B.verElementos()
    print('Conjunto C')
    C.verElementos()
    print('A intersecao entre o Conjunto B e o Conjunto C é')
    intersecao(B, C).verElementos()
    print('-'*50)


testaVerElementos()
testaPertinencia()
testaSubconjuntos()
testaIgualdade()
testaUniao()
testaIntersecao()

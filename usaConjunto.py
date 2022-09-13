from Conjunto import *
# CRIANDO CONJUNTOS
A = Conjunto([8, 7])
B = Conjunto([0, 1, 2])
C = Conjunto([2, 1, 0, 3])
D = Conjunto()
E = Conjunto([7, 8])


def testaVerElementos():
    print(A)
    print(B)
    print(C)
    print(D)
    print(E)
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
    print(f'O Conjunto A é igual ao B? {A == B}')
    print('-'*50)


def testaUniao():
    print('Conjunto A')
    print(A)
    print('Conjunto B')
    print(B)
    print('A união entre o Conjunto A e o Conjunto B é')
    print(uniao(A, B))
    print('-'*50)


def testaIntersecao():
    print('Conjunto B')
    print(B)
    print('Conjunto C')
    print(C)
    print('A intersecao entre o Conjunto B e o Conjunto C é')
    print(intersecao(B, C))
    print('-'*50)


testaVerElementos()
testaPertinencia()
testaSubconjuntos()
testaIgualdade()
testaUniao()
testaIntersecao()

# from Conjunto import *

# class Teste:
#     def __init__(self, *args) -> None:  # usar args pra aceitar
#         print(*args)


# teste = Teste(1,2)

from pprint import pprint
from Conjunto import Conjunto


def conjuntoDasPartes(A):
    B = len(A)
    elementos = [elemento for elemento in A]
    ps = []
    for i in range(2 ** B):
        w = f'{i:0{B}b}'
        q = [elementos[j] for j, bit in enumerate(w) if bit == '1']
        ps.append(Conjunto(q))
    return Conjunto(ps)


A = Conjunto([8, 7])
B = Conjunto([0, 1, 2])
C = Conjunto([2, 1, 0, 3])
D = Conjunto()
E = Conjunto([7, 8])

print(conjuntoDasPartes(A))

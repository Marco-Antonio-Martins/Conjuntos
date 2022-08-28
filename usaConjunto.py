from Conjunto import *
# CRIANDO CONJUNTOS
A = Conjunto([7,8])
B = Conjunto([0,1,2])
C = Conjunto([2,1,0])

print("-"*50)
# PRINTANDO ELEMENTOS DE CADA CONJUNTO
print('Elementos de A')
A.verElementos()
print('Elementos de B')
B.verElementos()
print('Elementos de C')
C.verElementos()

print("-"*50)
# Verificando funções
print("O Conjunto A possui o elemento 2? {}".format(A.possui(2)))
print("O Conjunto A é subconjunto de B? {}".format(A.isSubconjunto(B))) #verificar se A é subCJ de A (igualdade)
print("O Conjunto B é subconjunto de A? {}".format(B.isSubconjunto(A)))
print("O Conjunto A é igual ao B? {}".format(A.isEqual(B)))
print("O Conjunto B é igual ao C? {}".format(B.isEqual(C)))

print("-"*50)
#UNIÃO DO CONJUNTO A E B
print("A união dos conjuntos A e B é:")
uniao(A,B).verElementos()

print("-"*50)
# INTERSEÇÃO DO CONJUNTO A E B
print("A interseção dos conjuntos A e B é:")
intersecao(A,B).verElementos()
print("-"*50)
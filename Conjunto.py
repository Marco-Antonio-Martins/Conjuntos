class Conjunto(): #criando a classe conjunto
  elementos = []
  
  def __init__(self, elementos=[]):
    self.elementos = elementos

  def verElementos(self):
    if len(self.elementos) > 0:
      ret="{"
      for elemento in self.elementos:
        ret+=str(elemento)+ ","
      ret=ret[:-1]
      ret+="}"
      print(ret)
    else:
      print("{} - CONJUNTO VAZIO")

  def possui(self, elemento): #Pertinência
    if elemento in self.elementos:
        return True
    return False

  def isSubconjunto(self, conjunto):
    elementos = conjunto.elementos

    for elemento in self.elementos:
      if elemento not in elementos:
        return False      
    return True

  def isEqual(self, conjunto):
    if self.isSubconjunto(conjunto) and conjunto.isSubconjunto(self):
      return True
    return False

def uniao(a,b):
  retornoUniao = []

  for elemento in a.elementos:
    if elemento not in retornoUniao:
      retornoUniao.append(elemento)

  for elemento in b.elementos:
    if elemento not in retornoUniao:
      retornoUniao.append(elemento)

  ret = Conjunto(retornoUniao)
  return ret

def intersecao(a,b):
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
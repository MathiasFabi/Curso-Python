# Tamanho e palavra invertida
def aula():
  print('A palavra digitada foi: ',x)
  print(len(x))
  invertida = x[:: -1]
  print('A palavra invertida é: ',invertida)
  if x in "aeiou": # aqui testa com o operador in
        return True
  else:
        return False

x = input('Digite uma palavra :')

aula()

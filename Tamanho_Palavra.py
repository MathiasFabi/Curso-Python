# Tamanho de uma palavra_se apareceu uma determinada letra
palavra = input('Digite uma palavra ')
print(len(palavra))
numero_vezes = 0

for z in palavra :
  if z  == "a" :
    numero_vezes = numero_vezes + 1
print(numero_vezes)    

# Procura o menor preço
def menor(a,s,m):
    min = a

    if s < min:
        min = s
    if m < min:
        min = m

    return min
  

a = float(input('Informe o valor do celular G9 na loja Americanas {}: R$'.format(n)))  
s = float(input('Informe o valor do celular G9 no Shoptime {}: R$'.format(n)))
m = float(input('Informe o valor do celular G9 na Magalu {}: R$'.format(n)))

print('O valor do celular G9 na Americanas: R$ {:.2f}'.format(a))  
print('O valor do celular G9 no Shoptime: R$ {:.2f}'.format(s))
print('O valor do celular G9 na Magalu: R$ {:.2f}'.format(m))
print('O menor valor: ', menor(a,s,m))

menor(a,s,m)

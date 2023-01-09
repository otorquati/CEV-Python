# Aula 06 - Tipos primitivos de Saídas de Dados
n1 = int(input('digite um valor:'))
n2 = int(input('digite um valor:'))
s = n1+n2
print('A soma vale ',s)
#
# Outra forma de mostrar o resultado
#
print('A soma entre ',n1,' e ',n2, ' é igual a ',s)
#
# Usando o método format
#
print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))

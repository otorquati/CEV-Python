# Aula 06 - Tipos primitivos de Saídas de Dados
n1 = float(input('digite um valor:'))
print(n1)
# Convertendo para string
n1 = str(input('digite um valor:'))
print(n1)
print(type(n1))
# Convertendo para Booleano
n1 = bool(input('digite um valor:'))
print(n1)
print(type(n1))
# Verificando o tipo para conversão com método de teste de tipos - isnumeric e isalpha
n1 = input('digite um valor:')
print(n1.isnumeric())
n1 = input('digite um valor:')
print(n1)
print(n1.isalpha())

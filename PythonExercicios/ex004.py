# Verificando o tipo para conversão com método de teste de tipos - isnumeric e isalpha
sVar = input('digite um valor:')
print('O tipo de dado digitado é {}'.format(type(sVar)))
print('o dado também é númerico?',sVar.isnumeric())
print('o dado também é alfanumérico?',sVar.isalnum())
print('o dado também é alfabético?',sVar.isalpha())
print('o dado também é maiúscula?',sVar.isupper())
print('o dado também é um digito?',sVar.isdigit())
print('o dado também é número real?',sVar.isdecimal())

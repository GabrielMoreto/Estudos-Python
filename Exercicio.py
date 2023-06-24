# Função .format chama a variável no {}
name = input('Qual o seu nome? ')

print('Olá é um prazer te conhecer {}!'.format(name))

# Crie um programa que leia dois números e mostre a soma entre eles.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 - n2

print('A subtração entre {} e {} é igual á {}'.format(n1, n2, s))

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo 
# primitivo e todas as informações possíveis sobre ele.
a = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumériico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())
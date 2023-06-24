# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever 
# na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

# # Metódo Composto:
pensar = randint(0, 5) #Faz o computador "Pensar"
print('-=-' * 20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
num = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if pensar == num:
    print('Você acertou, parabéns!')
else:
    print('Você errou, eu pensei em {} não em {}, tente novamente!'.format(pensar, num))


# # Metódo Simplificado:
pensar = randint(0, 5)
print(pensar)
num = int(input('Escolha um número de 0 a 5: '))
print('Você acertou, parabéns!' if pensar == num else 'Você errou, tente novamente.')


# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

# Metódo Composto:
velo = float(input('Qual a velocidade do carro? '))
multa = (velo - 80) * 7
if velo > 80:
    print('Você foi multado, o valor da multa é R${:.2f}.'.format(multa))
else:
    print('Parabéns, você estava no limite de velocidade permitida.')


# Metódo Simplificado:
velo = int(input('Qual a velocidade do carro? '))
multa = (velo - 80) * 7
print('Você foi multado, o valor da multa é R${:.2f}.'.format(multa) if velo > 80 else 'Parabéns, você estava no limite de velocidade permitida.')


# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Metódo Composto:
num = int(input('Digite um número inteiro: '))
resto = num % 2
if resto == 0:
    print('{} é um número par.'.format(num))
else:
    print('{} é um número ímpar.'.format(num))


# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço 
# da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

# Metódo Composto:
distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('O valor a ser pago pela viagem é R${:.2f}.'.format(valor))


# Metódo Simplificado:
distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
valor = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor a ser pago pela viagem é R${:.2f}.'.format(valor))


# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

ano = int(input('Que ano quer analizar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} Não é BISSEXTO.'.format(ano))


# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# # Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# #Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}.'.format(menor))
print('O maior valor digitado foi {}.'.format(maior))


# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do
# seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.
salario = float(input('Qual o seu salário? '))
if salario <= 1250.00:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('Seu novo salário é R${:.2f}.'.format(aumento))


# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.
print('-=-' * 8)
print('Analisador de Triângulos')
print('-=-' * 8)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')

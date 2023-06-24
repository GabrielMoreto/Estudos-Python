# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Forma 1:
import math
n = float(input('Digite um número: '))

print('A porção inteira de {} é {}.'.format(n, math.floor(n)))
print('A porção inteira de {} é {}.'.format(n, math.trunc(n)))


# Forma 2:
from math import trunc
n = float(input('Digite um número: '))

print('A porção inteira de {} é {}.'.format(n, trunc(n)))


# Forma 3:
n = float(input('Digite um número: '))

print('A porção inteira de {} é {}.'.format(n, int(n)))


# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# Maneira sem importação
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi= (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}.'.format(hi))


# # Maneira com importação
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print('A hipotenusa vai medir {:.2f}.'.format(hi))


# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, cos, sin, tan
import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print('O ângulo de {} tem o SENO de {:.2f}.'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(ang, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(ang, tangente))


# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
# nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)

print('O aluno escolhido foi {}.'.format(escolhido))


# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)

print('A ordem de apresentação será ')
print(lista)


# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()


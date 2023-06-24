# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos 
# de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('BUM! BUM! POOOW!')


# Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range (2, 51, 2):
    print(c, end = ' ')
print('FIM!')

for c in range (1, 51):
    par = c % 2
    if par == 0:
        print(c, end = ' ')
print('FIM!')    

for c in range (1, 51):
    if c % 2 == 0:
        print(c, end = ' ')
print('FIM!')


# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram 
# no intervalo de 1 até 500.

soma = 0
cont = 0

for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))

for c in range (1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))
        

# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando 
# um laço for.

n = int(input('Digite o número que deseja saber a tabuada: '))

print('-' * 12)

for c in range (0, 11):
    print('{} x {:2} = {}'.format(n, c, n * c))
print('-' * 12)


# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
cont = 0

for c in range (1, 7):
    n = int(input('Digite 0 {}º número: '. format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n
print('Você informou tantos {} pares e a soma entre eles é {}.'.format(cont, soma))

        
# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros 
# termos dessa progressão.

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão

for c in range(primeiro, decimo + razão, razão):
    print('{} '.format(c), end = '-> ')
print('ACABOU')


# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
tot = 0

for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end = '')
        tot += 1
    else:
        print('\033[31m', end = '')
    print('{} '.format(c), end = '')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))

if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')


# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando 
# os espaços. Exemplos de palíndromos:

# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frese: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

frase = str(input('Digite uma frese: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')



# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas 
# ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
menor = 0
maior = 0

for c in range (1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade\nE também tivemos {} menores de idade'.format(maior, menor))


# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for c in range (1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))


# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média 
# de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0

for c in range (1, 5):
    print('-' * 5, '{}ª PESSOA'.format(c), '-' *5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} com menos de 20 anos.'.format(totmulher20))

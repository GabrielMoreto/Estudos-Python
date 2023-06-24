# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número: '))

print('O sucessor é {} e o antecessor é {}.'.format((n+1), (n-1)))


# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite um número: '))

print('O dobro é {}, o triplo é {} e raiz quadrada é {:.2f}.'.format(n1 * 2, n1 * 3, n1 ** (1/2)))

n1 = int(input('Digite um número: '))

print('O dobro é {}, o triplo é {} e raiz quadrada é {:.2f}.'.format(n1 * 2, n1 * 3, pow(n1, (1/2))))


# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print('A média das notas é {:.1f}.'.format((nota1 + nota2) / 2))


# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
n = float(input('Digite um valor em metros: '))

print('Esse valor em cm é {:.0f}cm e em milimetros é {:.0f}mm.'.format(n * 100, n * 1000))


# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite o número que deseja saber a tabuada: '))

print('-' * 12)
print('{} x {:2} = {}'.format(n, 0, n * 0))
print('{} x {:2} = {}'.format(n, 1, n * 1))
print('{} x {:2} = {}'.format(n, 2, n * 2))
print('{} x {:2} = {}'.format(n, 3, n * 3))
print('{} x {:2} = {}'.format(n, 4, n * 4))
print('{} x {:2} = {}'.format(n, 5, n * 5))
print('{} x {:2} = {}'.format(n, 6, n * 6))
print('{} x {:2} = {}'.format(n, 7, n * 7))
print('{} x {:2} = {}'.format(n, 8, n * 8))
print('{} x {:2} = {}'.format(n, 9, n * 9))
print('{} x {:2} = {}'.format(n, 10, n * 10))
print('-' * 12)


# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere US$1,00 = R$3,27.
d = float(input('Quanto dinheiro você tem na carteira? R$'))

print('Com essa quantia você pode comprar US${:.2f}.'.format(d/3.27))


# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade 
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
tinta = (largura*altura) / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, largura*altura))
print('Para pintar essa parede você precisará de {}L de tinta.'.format(tinta))


# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)

print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))


# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 20% de aumento.
salário = float(input('Digite o salário: R$'))
novo = salário + (salário * 20 / 100)

print('O salário de R${:.2f} com 20% de aumento é R${:.2f}.'.format(salário, novo))


# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.


# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos 
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

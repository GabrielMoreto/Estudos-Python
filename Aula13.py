# Aula 13: Estrutura de repetiçaõ "for".

# De 1 até 6 ele faz 5 vezes, porque não considera o último número.
# De 0 até 6 ele faria 6 vezes.

# for c in range (1,6):         
#     print('Oi')
# print('FIM')

# for c in range (0,6):
#     print('Oi')
# print('FIM')

# Se atentar a identação:

# for c in range (0,6):
#     print('Oi')
# print('FIM')

# for c in range (0,6):
#     print('Oi')
#     print('FIM')

# Se no lugar de "Oi" eu mandar escrever "c", ele vai escrever de 0 á 5, pois c é a váriavel contadora.
# Se for fazer uma contagem de 0 até 6, faça "(0,7)" sempre lembrar de colocar 1 a mais.

# for c in range (0,6):
#     print(c)
# print('FIM')

# Para contar para trás usar o "-1" que é a iteração.

# for c in range (6, 0, -1):
#     print(c)
# print('FIM')

# Para contar pulando de 2 em 2.

# for c in range (0, 7, 2):
#     print(c)
# print('FIM')

# For recebndo uma váriavel "n" que determina até aonde o laço deve ir.

# n = int(input('Digite um número: '))

# for c in range (0, n):
#     print(c)
# print('FIM')

# For recebendo a váriavel de "início" de "Fim" e de "Passo".

# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))

# for c in range (i, f+1, p):
#     print(c)
# print('FIM')



s = 0

for c in range (0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
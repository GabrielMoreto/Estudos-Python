# Aula 09: Manipulação Texto

# Para selecionar só o caractere 9, lembrando que começa a contar do 0
# Obs:Espaços em branco contam como caractere
frase = 'Curso em Vídeo Python'
print(frase[9])

# Para selecionar do caractere 9 até o 13, mas o 13 não entra na contagem
frase = 'Curso em Vídeo Python'
print(frase[9:13])

# A frase 'Curso em Vídeo Pythin' tem 20 caracteres começando a contar do 0
# para selecionar tudo seguir o exemplo abaixo:
frase = 'Curso em Vídeo Python'
print(frase[9:21])

# Para pular de 2 em 2 seguir o exemplo abaixo:
frase = 'Curso em Vídeo Python'

# No print abaixo 9 é o começo, 21 é o final e o 2 é quantidade que sera pulada
print(frase[9:21:2])

# Para partir do ínicio pode se usar duas formas:
# Forma 1:
frase = 'Curso em Vídeo Python'
print(frase[:5])

# Forma 2:
print(frase[0:5])

# Para partir do final pode se usar duas formas:
# Forma 1:
frase = 'Curso em Vídeo Python'
print(frase[15:])

# Forma 2:
print(frase[15:21])

# Para pular de 3 em 3 pode se usar as duas formas abaixo:
# Forma 1:
frase = 'Curso em Vídeo Python'
print(frase[9::3])

# Forma 2:
print(frase[9:21:3])

# Para ler o comprimento da frase ou seja, saber quantos caracteres ela tem
# utilizar a função "len()"
frase = 'Curso em Vídeo Python'
print(len(frase))

# Para saber quantas vezes aparece um determinado caractere utilizar a função 
# ".count('caracter')", nesse exemplo não contaria os O's maiúsculos
frase = 'Curso em Vídeo Python'
print(frase.count('o'))

# Usando o fateamento, lembrando que o último valor sempre é ignorado
print(frase.count('o', 0, 13))

# Para saber em que momento começa um pedaço da string utilizar a função
# ".find('caractere')", essa função irá retornar a partir de onde começa 
frase = 'Curso em Vídeo Python'
print(frase.find('deo'))

# Se na função "find" você utilizar um valor que não existe retornará "-1"
frase = 'Curso em Vídeo Python'
print(frase.find('Android'))

# Operador "in", para saber se determinado valor existe na variável
frase = 'Curso em Vídeo Python'
print('Curso' in frase)

# Transformação de string

# Método .replace, para trocar um valor por outro 
frase = 'Curso em Vídeo Python'
print(frase.replace('Python', 'Android'))

# Método .upper() para deixar tudo em maiúsculo, .lower() para deixar em minúsculo,
# .capitalize() para jogar toda a frase em minúsculo e deixar a primeira letra da frase em maiúsculo
frase = 'Curso em Vídeo Python'
print(frase.upper())
print(frase.lower())
print(frase.capitalize())

# Método ".title()" para deixar a primeira letra de cada palavra em maiúsculo
frase = 'Curso em Vídeo Python'
print(frase.title())

# Método ".strip()" para remover espaçoes em branco no ínicio e no fim da variável,
# .rstrip() para remover os espaços em branco do final da variável,
# .lstrip() para remover os espaços em branco do ínicio da variável
frase = '   Aprendo Python  '
print(frase)
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

# Divisão de string

# Método ".split()" para quebrar a string e jogar em uma lista
frase = 'Curso em Vídeo Python'
print(frase.split())

# Método ".join()" para juntar a string
frase = 'Curso em Vídeo Python'
print('-'.join(frase))
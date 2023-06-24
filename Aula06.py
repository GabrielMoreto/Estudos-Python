# Aula10: Condições Simples e Compostas

# Lembrar de usar ":" no final das condições
# if = se
# else = senão

# Condição Composta:
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('--FIM--')

# Condição Simplificada:
tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

# Prática: Lembrar da identação
nome = str(input('Qual seu nome? '))
if nome == 'Gabriel':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}.'.format(nome))

# Condição Composta:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}.'.format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')

# Condição Simplificada:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}.'.format(m))
print('Parabéns!'if m >= 6 else 'Estude mais!')
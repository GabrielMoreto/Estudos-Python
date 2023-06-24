# Módulos

# Dentro do python para incluir bibliotecas se usa o comando "import".
# Exemplo:
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))

# Para incluir uma única função dentro da biblioteca utilizasse o "from".
# E para utilizar a função não necessita do "math."
from math import floor
num = int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

# Na biblioteca "math" existe as funções: ceil, floor, trunc, pow, sqrt, factorial e etc.
import math
from math import sqrt
from math import floor
from math import ceil
from math import trunc

# Biblioteca random serve para gerar números aleatórios

import random
num = random.randint(1, 10)
print(num)


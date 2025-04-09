#2. Escreva um código para importar a biblioteca numpy com o alias np.
import numpy as np

# 3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

# lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
from random import choice

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77];
print(f"Número escolhido: {choice(lista)}")

# 4. Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
# Dica: use a função randrange() da biblioteca random. Essa função recebe como parâmetro o valor limite para a escolha aleatória ou um intervalo se passado o limite mínimo e máximo. Por exemplo, randrange(5) gera valores inteiros menores que 5.

from random import randrange
print(f"O número e:{randrange(1,100)}")
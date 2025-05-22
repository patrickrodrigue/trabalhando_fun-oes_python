# #2. Escreva um código para importar a biblioteca numpy com o alias np.
# import numpy as np

# # 3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.

# # lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
# from random import choice

# lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77];
# print(f"Número escolhido: {choice(lista)}")

# # 4. Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
# # Dica: use a função randrange() da biblioteca random. Essa função recebe como parâmetro o valor limite para a escolha aleatória ou um intervalo se passado o limite mínimo e máximo. Por exemplo, randrange(5) gera valores inteiros menores que 5.
# from random import randrange
# print(f"O número e:{randrange(1,100)}")

# # 5. Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.
# from math import pow
# n1 =  int(input('Digite o primeiro número:'))
# n2 =  int(input('Digite o segundo número:'))
# print(f"{n1} elevado a {n2} e  {pow(n1,n2)}")

# # 6. Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.
# from random import choice
# participantes = int(input("Digite um número de participantes:"))
# numero = []
# for n in range(1, participantes + 1):
#     numero.append(n)
# print(f"O numero sorteado foi:{choice(numero)}")

# # 7. Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.
# #Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"
# from random import randrange
# nome = input('Qual e o seu nome?')
# tk =randrange(1000, 9998, 2)
# print(f"Olá, {nome}, o seu token de acesso é {tk}! Seja bem-vindo(a)!")

# # Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente.
# import random
# frutas = ["maçã", "banana", "uva", "pêra", 
#           "manga", "coco", "melancia", "mamão",
#           "laranja", "abacaxi", "kiwi", "ameixa"]
# salada = random.sample(frutas, 3)
# print(f"Salada de frutas surpresa: {salada}")

# #9.9. Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. A lista é a seguinte: numeros = [2, 8, 15, 23, 91, 112, 256] No final, informe quais números possuem raízes inteiras e seus respectivos valores.Dica: use a comparação entre a divisão inteira (//) da raiz por 1 com o valor da raiz para verificar se o número é inteiro.Saída:1.5 é inteiro? : False 2 é inteiro? : True
# import math
# numeros = [2, 8, 15, 23, 91, 112, 256]
# for n in numeros:
#     raiz = math.sqrt(n)
#     if raiz // 1 == raiz:
#         print(f"{raiz} é inteiro? : True")
#     else:
#         print(f"{raiz} é inteiro? : False")

#10. Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.Dica: use a variável pi e o método pow() da biblioteca math. O cálculo da área de um círculo é de: A = π*r^2 (lê-se pi vezes raio ao quadrado).Caso precise de ajuda, opções de solução das atividades estão disponíveis na seção “Opinião da pessoa instrutora”.
import math
raio = float(input("Digite o raio do jardim: "))
preco_metro_quadrado = 25.00
area = math.pi * math.pow(raio, 2)
preco_total = area * preco_metro_quadrado
print(f"O valor total a pagar pela grama é: R$ {preco_total:.2f}")
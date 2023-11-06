# Exercício Python 23: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

print(f'Essa é a soma de todos os múmeros múltiplos de 3 entre 1 à 500.')

for i in range(3, 498, 3):
    soma = sum(range(3, 498, 3))
print(f'A soma dos números é igual a {soma}')
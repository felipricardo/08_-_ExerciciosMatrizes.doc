"""1)Faça um programa que carregue uma matriz 3x5 com números inteiros, calcule e mostre a quantidade de elementos entre 15 e 20."""

# Criando a matriz 3x5 e preenchendo os valores
matriz = []
for i in range(3):
    linha = []
    for j in range(5):
        elemento = int(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
        linha += [elemento]
    matriz += [linha]

# Calculando a quantidade de elementos entre 15 e 20
contador = 0
for linha in matriz:
    for elemento in linha:
        if 15 <= elemento <= 20:
            contador += 1

# Exibindo o resultado
print("Quantidade de elementos entre 15 e 20:", contador)

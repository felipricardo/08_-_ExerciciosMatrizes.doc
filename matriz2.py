""" Faça um programa em python que receba as vendas semanais (de um mês) de cinco vendedores de uma loja e armazene essas vendas em uma matriz. Calcule e mostre:
a. O total de vendas do mês de cada vendedor
b. O total de vendas de cada semana (todos os vendedores juntos)
c .O total de vendas do mês """

# Criar uma matriz vazia para armazenar as vendas
vendas = [[] for _ in range(5)]

# Preencher a matriz de vendas
for i in range(5):
    print(f"Vendedor {i+1}")
    for j in range(4):  # Assume-se um mês com 4 semanas
        venda_semana = float(input(f"Vendas semana {j+1}: "))
        vendas[i].append(venda_semana)

# Calcular os totais
total_vendas_vendedor = []
total_vendas_semana = [0] * len(vendas[0])
total_vendas_mes = 0

for i in range(5):
    total_vendedor = 0
    for j in range(4):
        total_vendedor += vendas[i][j]
        total_vendas_semana[j] += vendas[i][j]
        total_vendas_mes += vendas[i][j]
    total_vendas_vendedor.append(total_vendedor)

# Mostrar os resultados
print("\nTotal de vendas do mês de cada vendedor:")
for i in range(5):
    print(f"Vendedor {i+1}: R${total_vendas_vendedor[i]}")

print("\nTotal de vendas de cada semana:")
for i in range(4):
    print(f"Semana {i+1}: R${total_vendas_semana[i]}")

print("\nTotal de vendas do mês: R$", total_vendas_mes)

#Ler uma lista de 10 números reais e mostre-os na ordem inversa.
# Inicializa uma lista vazia
numeros = []

for i in range(10):
    numero = float(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

print("Números na ordem inversa:")
for numero in reversed(numeros):
    print(numero)

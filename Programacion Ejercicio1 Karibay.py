# Escriba un programa que le solicite al usuario 3 números enteros y de como resultado una lista con los valores ordenados
print("Ingrese el primer valor: ")
valor1 = int(input())
print("Ingresé el segundo valor: ")
valor2 = int(input())
print("Ingresé el tercer valor: ")
valor3 = int(input())

# lista
valores = [valor1, valor2, valor3]

# Orden decreciente
valores.sort(reverse=True)

# Resultado
print("Los números en orden decreciente son: ")
print(valores[0], valores[1], valores[2])
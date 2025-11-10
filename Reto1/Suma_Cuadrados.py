#Suma de cuadrados

square = int(input("Ingrese un numero: "))
suma = 0
for i in range(1, square + 1):
    suma += i ** 2
print("La suma de los cuadrados es:", suma)
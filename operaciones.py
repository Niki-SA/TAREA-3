def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

print("Selecciona:")
print("1. Suma")
print("2. Resta")
print("3. Mu")
print("4. División")

eleccion = input("Ingresa elección (1/2/3/4): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if eleccion == '1':
    print("Resultado de la suma es:", suma(num1, num2))
elif eleccion == '2':
    print("Resultado de la resta es:", resta(num1, num2))
elif eleccion == '3':
    print("Resultado de la multiplicacion es:", multiplicacion(num1, num2))
elif eleccion == '4':
    print("Resultado de la division es:", division(num1, num2))
else:
    print("Entrada no válida")

from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "*", "/"]

# Cantidad de cuentas a resolver
times = 5

# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
cant_correcta = 0
cant_incorrecta = 0

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)

    # En el caso de que la division sea por el numero 0.
    if operator == "/" and number_2 == 0:
        randrange(1,10)
        
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")

    # Le pedimos al usuario el resultado
    result = int(input("resultado: "))
    match operator:
        case "+":
            if number_1 + number_2 == result:
                print("Respuesta correcta")
                cant_correcta += 1
            else:
                print("Respueta incorrecta")
                cant_incorrecta += 1
        case "-":
            if number_1 - number_2 == result:
                print("Respuesta correcta")
                cant_correcta += 1
            else:
                print("Respuesta incorrecta")
                cant_incorrecta += 1
        case "*":
            if number_1 * number_2 == result:
                print("Respuesta correcta")
                cant_correcta += 1
            else:
                print("Respuesta incorrecta")
                cant_incorrecta += 1
        case "/":
            if number_1 / number_2 == result:
                print("Respuesta correcta")
                cant_correcta += 1
            else:
                print("Respuesta incorrecta")
                cant_incorrecta += 1
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()

# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time

# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos")
print(f"\n Cantidad respuestas correctas {cant_correcta}")
print(f"\n Cantidad respuestas incorrectas {cant_incorrecta}")

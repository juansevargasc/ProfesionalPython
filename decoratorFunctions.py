from datetime import datetime, time

def execution_time(func): # args y kwargs sirve para decirle a la función que no importa cuantos argumentos tenga la función.
    def wrapper(*args, **kwargs): # *args, **kwargs -> argumentos posicionales, argumentos nombrados (argumentos por defecto para una función)
        initialTime = datetime.now() 
        func(*args, **kwargs)
        finalTime = datetime.now()
        timeElapsed = finalTime - initialTime # ¿Sumará o restará cada campo?
        print(f'Time Elapsed: {timeElapsed}, type: {type(timeElapsed)}')
        print("Pasaron " + str( timeElapsed.total_seconds() ) + " segundos" )
    return wrapper

@execution_time
def randomFunc():
    for _ in range(1, 100000000):
        pass

# Ejecución
# randomFunc()

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre='Cesar'):
    print("Hola " + nombre)

# Ejecuciones
randomFunc()
suma(4, 10)
saludo('Facundo')

# Decorador con parámetros
# Se añade una función adicional que recibe los parámetros.

def withCustomMessage(message): # Función adicional
    def message(function): # Función que recibe una función.
        print(f'{message}')
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
        return wrapper
    return message

@withCustomMessage("hello ")
def multiply(a, b):
    c = a * b
    print(f'The result of {a} * {b} is {c}')

multiply(11, 2)
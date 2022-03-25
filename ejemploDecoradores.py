def decorador(func):
    def envoltura():
        print('Esto se añade a mi función original')
        func()
    return envoltura

def saludo():
    print('¡Hola!')

# Decorador con sugar code (sintaxis más limpia)
def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return(f'{nombre}, recibiste un mensaje.')
# Este mensaje se debe imprimir en mayúsculas.
print(mensaje('Cesar'))



# Ejecuciones
# Función saludo sola.
saludo()

# Función saludo con decorador.
saludo = decorador(saludo)
saludo()
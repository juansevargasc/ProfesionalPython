# Hola 3 -> HolaHolaHola
# Closures:
# 1. Tenemos una nested function.
# 2. Esta nested function hace referencia a una variable de scope superior.
# 3. Esta nested function es recorada.

def makeRepeaterOf(n):
    def repeater(string):
        #assert para comprobar que sea string
        assert type(string) == str, "Sólo puedes utilizar cadenas"
        return string * n # Usa una variable de un alcance superior
    return repeater # retornar la función repeater.

def makeDivisionBy(n: int):
    """
        This closure returns a function that returns the division of an x number by n
    """
    def divide(number: int) -> int:
        assert n != 0, "n cannot be ZERO"
        return number / n
    return divide
    


def run():
    repeat5 = makeRepeaterOf(5)
    print(repeat5('Hola'))

    repeat10 = makeRepeaterOf(10)
    print(repeat10('Platzi'))

    divisionBy3 = makeDivisionBy(3)
    print(divisionBy3(18))

if __name__ == '__main__':
    run()
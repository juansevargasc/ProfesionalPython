import time

def fibo_gen(maximum):
    n1 = 0
    n2 = 1
    counter = 0

    while counter < maximum:
        print(f'counter: {counter}')
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            print(f'aux: {aux}')
            yield aux
        
if __name__ == '__main__':
    entrada = input("Introduce tu máximo: ")
    max = int(entrada)

    fibonacci = fibo_gen(max)
    for element in fibonacci:
        print(element)
        time.sleep(1)
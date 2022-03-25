def run():
    # https://python-reference.readthedocs.io/en/latest/docs/sets/
    print('SETS')
    myset1 = {3, 4, 5}
    myset2 = {5, 6, 7}

    print(myset1)
    print(myset2)

    myset3 = myset1 | myset2
    print('Unión: ', myset3)

    myset3 = myset1 & myset2
    print('Intersección: ', myset3)

    myset3 = myset1 - myset2
    print('Diferencia 1: ', myset3)

    myset3 = myset2 - myset1
    print('Diferencia 2: ', myset3)

    myset3 = myset1 ^ myset2
    print('Diferencia simétrica: ', myset3)

    # remove y discard
    '''
        Remove: Elimina el elemento indicado, pero si este no exite retorna un error index.
        Discard: Elimina el elemento indicado si existe, sino deja la lista igual.
    '''

run()
# Reto: Un programa que elimine los elementos de una lista con sets.

def remove_duplicates(someList):
    record = []
    for element in someList:
        if element not in record:
            # Then register it
            record.append(element)
    return record

def removeWithSet(someList):
    setNumbers = set(someList)
    record = list(setNumbers)
    return record

def run():
    randomList = [1, 1, 2, 2, 4]
    print('random list: ', randomList)
    print(remove_duplicates(randomList))

    print('\nSets')
    print('random list: ', randomList)
    print(removeWithSet(randomList))

if __name__ == '__main__':
    run()

# [1, 1, 2, 2, 4] -> [1, 2, 4]
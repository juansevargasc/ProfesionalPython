## Evaluar tipado estático: mypy programa.py --check-untyped-defs

def run():
    print('Holi')

    var = 1000
    print("Is palindrome ", var)
    print( isPalindrome(var) )

def isPalindrome(word: str) -> bool:
    word = word.replace(" ", "").lower()

    if word == word[::-1]:
        return True
    else:
        return False

def isPrime(num: int) -> bool:
    #divider = num / 2

    #if
    pass 


if __name__ == '__main__':
    run()


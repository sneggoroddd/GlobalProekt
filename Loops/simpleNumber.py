'''Определите, является ли данное число простым.'''
def isSimple(number):
    for i in range (2, number):
        if number % i == 0:
            return  False
    return  True


def main():
    number = int(input( "Введите число "))
    if isSimple(number) == True:
        print( "Простое")
    else:
        print("Не простое")


main()
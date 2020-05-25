def main():
    N = int(input("Кол-во товаров: "))
    total = 0
    maxcost = 0
    for i in range(N):
        cost = int(input("Введите стоимость товара: "))
        total = total+ cost
        if cost>maxcost :
            maxcost= cost
    print("Самый дорогой товар ", maxcost)
    print(" общая стоимость ", total)
main()

    ''' Функция делает скидку на товар. 1
    Если на 1000 то 5%, если больше 2000 то 10% '''
    
def price_discount(total):
    if total >= 1000 and total < 2000:
        return total * 0.95
    elif total >= 2000:
        return total * 0.9
    else:
        return total


def main():
    N = int(input("Кол-во товаров: "))
    total = 0
    maxcost = 0
    dopgood = 0
    for i in range(N):
        cost = int(input("Введите стоимость товара: "))
        total = total+ cost
        if cost>maxcost :
            maxcost= cost

    print("Самый дорогой товар ", maxcost)
    print(" общая стоимость ", total)
    dis = price_discount(total)
    print("Цена со скидкой", dis )

main()


    
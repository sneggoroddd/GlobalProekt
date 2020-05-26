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
    if total >= 1000 and total < 2000:
        print("Цена со скидкой", total*0.95, "Скидка 5%")
    elif total >= 2000:
        print("Цена со скидкой", total*0.9, 'Скидка 10%')
    else:
        dopgood = 1000 -total
        print('купите еще на', dopgood, "И получите скидку 5%")

main()


    
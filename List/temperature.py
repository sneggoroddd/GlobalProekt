'''дан список температур за N дней, определить самую высокую температуру,
определить кол-во дней с минимальной температурой.
 определить среднюю температуру.
 кол-во дней с температурой попадающей в указанный диапазон (например от 10 до 20)'''


def madelist():
    templist = []
    daycount = int(input("введите количество дней"))
    for i in range(daycount):
        tempday = int(input(f'Введите температуру {i} дня'))
        templist.append(tempday)
    return templist

def main():
    while True:
        madelist()



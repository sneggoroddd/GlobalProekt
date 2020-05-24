'''Дана дата из трех чисел (день, месяц и год).
Вывести yes, если такая дата существует (например, 12 02 1999 - yes, 22 13 2001 - no).
 Считать, что в феврале всегда 28 дней.
'''
#вводим дни, месяцы, года
#проводим проверку отдельно по каждому значению
# в функцию
def countday(mm):
    if mm == 2:
        return 28
    elif mm == 4 or mm == 6 or mm == 9 or mm  == 11:
        return 30
    else:
        return  31




def checkDate(dd, mm, gg):
    if mm<1 or mm > 12 or dd<1 or dd> countday(mm):
        return False
    else:
        return  True

def main():
    dd = int(input('введите день 1,2,3...' ))
    mm = int(input('введите месяц 1,2,3... ' ))
    gg = int(input('введите год 0000... ' ))

    if checkDate(dd,mm,gg):
        print('Yes')
    else:
        print('No')

main()
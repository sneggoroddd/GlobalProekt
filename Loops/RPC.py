'''Реализуйте серию из n игр "Камень, ножницы, бумага" с компьютером.
В результате выведите статистику: сколько игр выиграл пользователь,
сколько раз каждого вида ходов было выбрано.
 Дополните игру анализом компьютера ваших ходов и выбор наиболее подходящего против вас хода.'''
import random

def moveUser(start, end, message):
    while True:
        count = int(input(message))
        if count >= start and count<= end:
            break
        else:
            print(f"Не корретное значение, допустимое значение от {start} до {end}")
    return count

def moveComputer(sto, sci , paper):
    if sto == sci and  sci == paper:
        return random.randint(1, 3)
    else:
        if sto <= sci and sto <= paper:
            return 3
        elif sci<= paper and sci <= sto:
            return 1
        else:
            return  2



def main():
    end = 0
    sto = 0
    sci = 0
    pap = 0
    loss = 0
    win = 0
    math = 0

    while end == 0:
        count = moveUser(1,3,"Введите Камень- 1 или  Ножницы-2 или Бумага-3 :")
        if count == 1:
            sto += 1
        elif count == 2:
            sci += 1
        else:
            pap += 1
        value = moveComputer(sto, sci, pap)

        if count == value:
            print("Ничья")
        elif count == 1 and value == 2 or count == 2 and value == 3 or count == 3 and value == 1:
            print("Вы победили")
            win += 1
        else:
            print("Вы проиграли, компьютер загадал ", value)
            loss += 1
        math += 1
        print(f" Всего игр {math}, побед {win}, поражений {loss}")
        print(f"Вы выбрали камень {sto} раз, ножницы {sci} раз, бумага {pap} раз")
        end = int(input(' Продолжить да 0 нет 1'))
main()




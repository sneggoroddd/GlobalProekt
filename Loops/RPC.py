'''Реализуйте серию из n игр "Камень, ножницы, бумага" с компьютером.
В результате выведите статистику: сколько игр выиграл пользователь,
сколько раз каждого вида ходов было выбрано.
 Дополните игру анализом компьютера ваших ходов и выбор наиболее подходящего против вас хода.'''

def main():
    end = 0
    sto = 0
    sci = 0
    pap = 0
    loss = 0
    win = 0
    math = 0
    import random
    while end == 0:
        count = int(input(" Введите Камень- 1 или  Ножницы-2 или Бумага-3 :"))
        if count == 1:
            sto += 1
        elif count == 2:
            sci += 1
        else:
            pap += 1
        computer = random.randint(1, 3)

        if computer == 1:
            value = 1
        elif computer == 2:
            value = 2
        elif computer == 3:
            value = 3
        else:
            print("Нет такого значения")
            break
        if count == 1 and value == 1 or count == 2 and value == 2 or count == 3 and value ==3:
            print("Ничья")
        elif count == 1 and value == 2 or count == 2 and value == 3 or count == 3 and value == 1:
            print("Вы победили")
            win += 1
        else:
            print("Вы проиграли, компьютер загадал ", computer)
            loss += 1
        math += 1
        print(f" Всего игр {math}, побед {win}, поражений {loss}")
        print(f"Вы выбрали камень {sto} раз, ножницы {sci} раз, бумага {pap} раз")
        end = int(input(' Продолжить да 0 нет 1'))
main()




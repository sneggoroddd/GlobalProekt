'''Реализуйте серию из n игр "Камень, ножницы, бумага" с компьютером.
В результате выведите статистику: сколько игр выиграл пользователь,
сколько раз каждого вида ходов было выбрано.
 Дополните игру анализом компьютера ваших ходов и выбор наиболее подходящего против вас хода.'''

def main():
    end = 0
    import random
    while end == 0:
        count = int(input(" Введите Камень- 1 или  Ножницы-2 или Бумага-3 :"))
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
        else:
            print("Вы проиграли, компьютер загадал ", computer)
        end = int(input(' Продолжить да 0 нет 1'))
main()




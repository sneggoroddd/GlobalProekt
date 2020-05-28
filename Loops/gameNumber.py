
def main():
    import random

    #сделать возможность продолжить игру
    #добавить баланс = 100 каждая игра стоит по 10
    #если угадали с первой попытки то +50 со второго +30 с третьего +20
    #если баланса не хватает на игру то выводим сообщение об этом и завершаем игру
    #вести стастику пройгрышей и выйгрышей
    end = 1
    balance = 100


    while end == 1:
        computer = random.randint(1, 10)
        print(f' Баланс равен {balance}, стоимость игры 10')
        balance = balance - 10
        for i in range(3):
            user = int(input('Введите число: '))
            if user > computer:
                print('Введенное число больше')
            elif user < computer:
                print('Введенное число меньше')
            else:
                print('УРА! Угадали!')
                if i == 1:
                    balance = balance + 50
                elif i == 2:
                    balance = balance + 30
                else:
                    balance = balance + 20
                break
        else:
            print(f'Попытки закончены. Вы проиграли. Загаданное число = {computer}')

        print("Ваш баланс", balance)
        if  balance < 0:
            end = 0
        else:
            end = int(input("Продолжить игру? да- 1, нет- 0 :"))

main()
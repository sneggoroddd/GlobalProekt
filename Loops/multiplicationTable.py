'''Выведите на экран таблицу умножения для чисел от 1 до 10'''
def main():
     for i in range(1, 10):
        for j in range(1, 10):
            print((i*j), end=" ")
        print("")
main()
'''Вывести на экран фигуру из звездочек:
*******
*******
*******
*******
(квадрат из n строк, в каждой строке n звездочек)'''

def main():
    N = 0
    N = int(input("строк-столбцов N: "))
    for i in range(N):
        print('*'*N)
main()
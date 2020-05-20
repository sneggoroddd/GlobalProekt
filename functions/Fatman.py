def check_masa(massa):
    if massa < 94 or massa > 727:
        return False
    else:
        return True


def find_max(m1, m2, m3):
    if m1 >= m2 and m1 >= m3:
        max = m1
    elif m2 >= m3 and m2 >= m1:
        max = m2
    else:
        max = m3
    return max


def main():
    m1 = int(input('Введите массу толстяка 1 '))
    m2 = int(input('Введите массу толстяка 2 '))
    m3 = int(input('Введите массу толстяка 3 '))
    if not check_masa(m1)  or not check_masa(m2)  or not check_masa(m3):
        print('данные не корректны')
    else:
        max_ves = find_max(m1, m2, m3)
        print(max_ves)


main()

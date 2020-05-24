'''Дано время отправления часы и минуты,
дано время в пути часы и минуты.
написать функцию определяющую время прибытия
(часы не могу быть больше 24, минуты больше 60)'''
def calcTimeArrival(deptimeHour, deptimeMin, travelTimeHour, travelTimeMin):
    calcHour = deptimeHour + travelTimeHour
    calcmin =   deptimeMin + travelTimeMin
    if calcmin >= 60:
        calcHour = calcHour + 1
        calcmin = calcmin - 60
    if calcHour >= 24:
        calcHour = calcHour - 24
    return calcHour, calcmin


def main():

    deptimeHour = int(input('введите часы отправления ' ))
    deptimeMin = int(input('введите и  минуты отправления ' ))
    travelTimeHour = int(input('введите сколько часов в пути ' ))
    travelTimeMin = int(input('введите и минут в пути ' ))

    hour, min = calcTimeArrival(deptimeHour, deptimeMin, travelTimeHour, travelTimeMin)
    print(hour, min)

main()
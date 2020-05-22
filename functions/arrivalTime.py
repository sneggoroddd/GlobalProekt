'''Дано время отправления часы и минуты,
дано время в пути часы и минуты.
написать функцию определяющую время прибытия
(часы не могу быть больше 24, минуты больше 60)'''
"""ввод времени в пути
ввод времени отправления
проверка на правильность данных
определение времени прибытия
вывод времни прибытия"""
addhour = 0
remMin = 0
def hour( deptimeHour, travelTimeHour):
    if hour <0 or hour > 24:
        return False
    else:
        return True
def minutes( deptimeMin, travelTimeMin):
    if minutes <0 or minutes > 24:
        return False
    else:
        return True
def arTime(arTimeMin):
    if arTimeMin > 60:
        addhour = arTimeMin//60
        remMin = arTimeMin%60*60
    else:
        addhour = 0
        remMin = 0
    return addhour,remMin

deptimeHour = int(input('введите часы отправления ' ))
deptimeMin = int(input('введите и  минуты отправления ' ))
travelTimeHour = int(input('введите сколько часов в пути ' ))
travelTimeMin = int(input('введите и минут в пути ' ))
hour
minutes

print('ok')

arTimeHour = deptimeHour + travelTimeHour
arTimeMin = deptimeMin + travelTimeMin

arTime

arTimeHour= arTimeHour + addhour
arTimeMin = arTimeMin + remMin


if arTimeHour > 24:
    arTimeHour = arTimeHour// 24
else:
    True

print('время прибытия', 'часов', arTimeHour, ' минут', arTimeMin)
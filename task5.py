# вводим значения переменных
a, b = int(input()), int(input())
# если а равно 0 и б неравно 0, то корней нет
if a == 0 and b != 0:
    print('NO')
# если а и б равны 0, то корней бесконечное количество
elif a == 0 and b == 0:
    print('INF')
# если а неравно 0, то надо проверить сначала, делится ли -б на а, так как, делить на ноль нельзя
# и если все делится, то вывести ответ
elif a != 0 and -b // a != 0:
    print(-b//a)
# в остальных случаях корней нет
else:
    print('NO')
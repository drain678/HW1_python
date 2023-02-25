# вводим значения переменных
students, variants, Petya_row, Petya_var = int(input()), int(input()), int(input()), int(input())
# также добавим флаг, который будет обращаться в False,
# если Вася не сможет получить такой же вариант как у Пети
flag = True
# найдем вариант Пети
if Petya_var == 1:
    # если он сел справа, то нужно умножить ряд на два, т к две парты, и вычесть 1
    Petya_Vasya_num_var2 = 0  # это будет истинный вариант
    Petya_Vasya_num_var1 = Petya_row * 2 - 1  # а это промежуточный
    # может получиться больше самомго большего варианта, поэтому надо разделить с остатком и будет истинный вариант
    if Petya_Vasya_num_var1 > variants:
        Petya_Vasya_num_var2 = Petya_Vasya_num_var1 % variants
        if Petya_Vasya_num_var1 % variants == 0:
            Petya_Vasya_num_var2 = variants
    else:
        Petya_Vasya_num_var2 = Petya_Vasya_num_var1
else:  # аналогично если он сел слева
    Petya_Vasya_num_var2 = 0
    Petya_Vasya_num_var1 = Petya_row * 2
    if Petya_Vasya_num_var1 > variants:
        Petya_Vasya_num_var2 = Petya_Vasya_num_var1 % variants
        if Petya_Vasya_num_var1 % variants == 0:
            Petya_Vasya_num_var2 = variants
    else:
        Petya_Vasya_num_var2 = Petya_Vasya_num_var1
# теперь рассчитаем слева или справа будет сидеть Вася
if variants % 2 == 0 and (Petya_Vasya_num_var2 % 2 == 0 or Petya_Vasya_num_var2 % 2 != 0):  # если вариантов четное количество, то он будет сидеть там же, где Петя
    Vasya_var = Petya_var
elif variants % 2 != 0 and (Petya_Vasya_num_var2 % 2 != 0 or Petya_Vasya_num_var2 % 2 == 0):  # иначе, они поменяются
    if Petya_var == 1:
        Vasya_var = Petya_var + 1
    else:
        Vasya_var = 1
# если промежуточный вариант Пети и Васи не выходил за пределы основного варианта, то Вася не может сидеть перед Петей
if Petya_Vasya_num_var1 < variants:
    if (variants + Petya_Vasya_num_var1) % 2 == 0:  # если сумма основного варианта их варианта делится, то нужно их сложить и разделить на 2, т к парт две
        Vasya_row = (variants + Petya_Vasya_num_var1) // 2
    else:  # иначе, еще добавить один
        Vasya_row = ((variants + Petya_Vasya_num_var1) // 2) + 1
    # если количество вариантов получилось больше чем учеников, то присвоить флагу False
    if variants + Petya_Vasya_num_var1 > students:
        flag = False
else:
    # вычислим ряд Васи когда он будет сидеть после Пети
    if ((variants + Petya_Vasya_num_var2) + (Petya_Vasya_num_var1 % variants) * variants) % 2 == 0:
        posle_Petya = ((variants + Petya_Vasya_num_var2) + (
                Petya_Vasya_num_var1 % variants) * variants) // 2
    else:
        posle_Petya = (((variants + Petya_Vasya_num_var2) + (
                Petya_Vasya_num_var1 % variants) * variants) // 2) + 1
    # если удвоенный вариант Пети и Васи получился меньше чем учеников, то Вася сядет за Петей
    if Petya_Vasya_num_var1 * 2 <= students:
        Vasya_row = posle_Petya
    else:  # иначе, проверка на то чтобы промежуточный и истинный варианты не были одинаковыми
        if Petya_Vasya_num_var1 != Petya_Vasya_num_var2:  # вычисление места перед Петей
            pered_Petya = posle_Petya - (((Petya_Vasya_num_var1 - Petya_Vasya_num_var2) * 2) // 2)
            Vasya_row = pered_Petya
            if pered_Petya < 0:  # он если оно отрицательное, то флаг = False
                flag = False
        else:  # иначе, флаг = False
            flag = False
if flag:  # если флаг = True, то у Васи будет такой же вариант как у Пети
    print(Vasya_row, Vasya_var)
else:
    print(-1)

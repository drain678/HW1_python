# вводим значения переменных
students, varints, Petya_row, Petya_var = int(input()), int(input()), int(input()), int(input())
if Petya_var == 1:
    Petya_Vanya_num_var = Petya_row * 2 - 1
else:
    Petya_Vanya_num_var = Petya_row * 2
if Petya_Vanya_num_var <= varints:
    t = students - varints
else:
    Petya_Vanya_num_var = Petya_Vanya_num_var % varints
    t = students - varints * 2
#u = varints - Petya_Vanya_num_var
#t = students - varints - u

if t >= Petya_Vanya_num_var:
    if varints % 2 == 0 and varints >= Petya_Vanya_num_var:
        Vanya_row = Petya_row + ((varints - Petya_Vanya_num_var) // 2) + 1
        Vanya_var = Petya_var
        print(Vanya_row, Vanya_var)
    elif (varints % 2 == 0 and Petya_Vanya_num_var % 2 != 0) or (varints % 2 == 0 and Petya_Vanya_num_var % 2 == 0):
        Vanya_row = Petya_row + ((varints - Petya_Vanya_num_var) // 2) + 1
        Vanya_var = Petya_var
        print(Vanya_row, Vanya_var)
    elif varints % 2 != 0 and Petya_Vanya_num_var % 2 != 0:
        Vanya_var = Petya_var - 1
        Vanya_row = Petya_row + ((varints - Petya_Vanya_num_var) // 2) + 1
        print(Vanya_row, Vanya_var)
    elif varints % 2 != 0 and Petya_Vanya_num_var % 2 == 0:
        Vanya_var = Petya_var - 1
        Vanya_row = Petya_row + ((varints - Petya_Vanya_num_var) // 2) + 1
        print(Vanya_row, Vanya_var)
    else:
        print(-1)
else:
    print(-1)
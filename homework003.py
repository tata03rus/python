# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# Пример:
# 385916 -> yes
# 123456 -> no

nomer_bileta = str(input('Введите номер билета (6 цифр): '))
summa1 = int(nomer_bileta[0]) + int(nomer_bileta[1]) + int(nomer_bileta[2])
summa2 = int(nomer_bileta[3]) + int(nomer_bileta[4]) + int(nomer_bileta[5])
if (summa1==summa2):
    print ('Билет с номером ', nomer_bileta, ' - счастливый')
else:
    print ('Билет с номером ', nomer_bileta, ' - несчастливый')
    
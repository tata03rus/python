# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

S = int(input("Введите сумму чисел Х и Y: "))
P = int(input("Введите произведение чисео Х и Y: "))
D = S ** 2 - 4 * P
print(D)
if D > 0:
    y1 = (-S + D**(0.5))/-2
    x1 = S - y1
    print(x1, y1)
    y2 = (-S - D**(0.5))/-2
    x2 = S - y2
    print(x2, y2)
elif D == 0:
    y1 = -S/-2
    x1 = S - y1
    print(x1, y1)
else:
    print("Нет решения")
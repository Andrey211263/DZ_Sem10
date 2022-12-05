import re

# --------------------------
# Пишем формулу
# ------------------------


def formula(test, count):

    res = ''
    i = 0
    while count != 0:
        inter = test[i]
        if inter != 0:
            res += str(inter)
            res += 'x'
            if count != 1:
                res += '^'
                res += str(count)
            res += '+'
        count -= 1
        i += 1
    if test[i] != 0:
        res += str(test[i])
    else:
        res[-1] = ''  # убираем плюс, если =0
    res += '=0'
    return res

# --------------------------
# функция обработки сроки, убираем +^
# --------------------------


def splt(file):         #
    f = []
    for i in range(0, len(file)):
        f = list(file.strip().replace(
            '+', ' ').replace('^', ' ').replace('=0', '').split())

    return f

# --------------------------
# функция обработки сроки в int,
# 0-ой элемент степень многочлена
# --------------------------


def int_str(f):
    res = []
    dl = len(f)  # длина массива
    count = int(f[1])
    res.append(count)  # 0-ой содержит степень многочлена
    i = 0
    while dl > 2:
        tmp = int(f[i+1])
        if count == tmp:
            a = re.split(r'[x]', f[i])
            if a[0] == '':
                a[0] = 1
            res.append(a[0])
            count -= 1
        else:
            while count > tmp:
                res.append(0)
                count -= 1
        dl -= 2
        i += 2

    if 'x' in f[i]:
        if dl == 1:
            a = re.split(r'[x]', f[i])
            res.append(a[0])
            res.append(0)
        else:
            a = re.split(r'[x]', f[i])
            if count > 1:
                res.append(0)
            res.append(a[0])
            res.append(f[i+1])
    else:
        while count>0:
            res.append(0)
            count -= 1
        res.append(f[i])

    return res

# --------------------------
# сумируем строки
# условие вхождения a1 > a2
# --------------------------


def sum_str(str1, str2, a1, a2):
    result = []
    i = 1
    count = a1
    while a1 != a2:
        result.append(str1[i])
        i += 1
        a1 -= 1
    j = 1
    while a1 != 0:
        result.append(int(str1[i]) + int(str2[j]))
        i += 1
        j += 1
        a1 -= 1
    result.append(int(str1[i]) + int(str2[j]))

    return result
# ---------------------

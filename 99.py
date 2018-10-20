# 左侧朝上9*9乘法表
for n in range(1, 10):
    for m in range(1, n + 1):
        if m < n:
            if len(str(m * n)) == 1:  # 对齐
                print('{}*{}={}'.format(m, n, n * m), end='  ')
            elif len(str(m * n)) == 2:
                print('{}*{}={}'.format(m, n, n * m), end=' ')
        else:
            print('{}*{}={}'.format(m, n, n * m))
print()
# 右侧朝上9*9乘法表
for i in range(1, 10):
    print(' ' * (9 - i) * 7, end='')
    for j in range(i, 0, -1):
        if j != 1:
            if len(str(j * i)) == 1:  # 对齐
                print('{}*{}={}'.format(j, i, j * i), end='  ')
            elif len(str(j * i)) == 2:
                print('{}*{}={}'.format(j, i, j * i), end=' ')
        else:
            print('{}*{}={}'.format(j, i, j * i))
print()
# 右侧朝下9*9乘法表
for a in range(9, 0, -1):
    print(' ' * (9 - a) * 7, end='')
    for b in range(a, 0, -1):
        if b != 1:
            if len(str(b * a)) == 1:  # 对齐
                print('{}*{}={}'.format(b, a, b * a), end='  ')
            elif len(str(b * a)) == 2:
                print('{}*{}={}'.format(b, a, b * a), end=' ')
        else:
            print('{}*{}={}'.format(b, a, b * a))
print()
# 左侧朝下9*9乘法表
for s in range(9, 0, -1):
    for k in range(1, s + 1):
        if k < s:
            if len(str(k * s)) == 1:
                print('{}*{}={}'.format(k, s, k * s), end='  ')
            else:
                print('{}*{}={}'.format(k, s, k * s), end=' ')
        else:
            print('{}*{}={}'.format(k, s, k * s))

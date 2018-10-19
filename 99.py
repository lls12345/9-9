for n in range(1, 10):
    for m in range(1, n + 1):
        if m < n:
            print('{}*{}={}'.format(m, n, n * m, ), end=' ')
        else:
            print('{}*{}={}'.format(m, n, n * m))

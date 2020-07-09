def binary_search(l, n):
    x = set(l)
    y = list(x)
    y.sort()
    print(y)
    maximal = len(y)
    minimum = 0

    while minimum < (maximal-1):
        mid = (maximal + minimum) // 2
        if y[mid] == n:
            return True
        elif y[mid] >= n:
            maximal = mid
        else:
            minimum = mid
    return False


x = [5, 6, 7, 8, 9, 11, 5, 8, 9, 6, 3, 4, 7, 1, 2, 5, 9, 55, 88, 9, 77, 41, 123, 12, 16, 8, 99, 6, 65, 45, 156, 856,
     745, 896, 32, 512, 62, 35, 69, 87, 54, 1, 2, 52, 23, 2, 22]
print(binary_search(x, 10))

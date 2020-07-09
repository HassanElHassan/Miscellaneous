# binary search using list slicing
def binary_search(l,n):
    x = set(l)
    y = list(x)
    y.sort()
    print(y)

    while True:
        mid = len(y) // 2
        if n == y[mid] or n == y[0]:
            return True
        elif n < y[mid]:
            y = y[:mid]
        elif n > y[mid]:
            y = y[mid:]
        if len(y) == 1:
            return False


x = [5, 6, 7, 8, 9, 11, 5, 8, 9, 6, 3, 4, 7, 1, 2, 5, 9, 55, 88, 9, 77, 41, 123, 12, 16, 8, 99, 6, 65, 45, 156, 856,
     745, 896, 32, 512, 62, 35, 69, 87, 54, 1, 2, 52, 23, 2, 22]
print(binary_search(x, 10))

def intercalar(a, valor):
    i = len(a) - 2
    while i >= 0 and a[i] > valor:
        a[i + 1] = a[i]
        i = i - 1
    a[i + 1] = valor
    return a


arreglo = [1, 4, 5, 8, 9]
print("arreglo con valor intercalado en orden:", intercalar(arreglo, 7))  
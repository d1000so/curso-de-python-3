if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lista = []
    listas = []
    for i in range(x, y, z):
        lista.append(i)
        for j in range(x, y, z):
            lista.append(j)
            for k in range(x, y, z):
                lista.append(k)
                if i + j + k != n:
                    listas.append(lista)
                    lista.clear()
    print(listas)


n = int(input("n: "))
if n < 1 or n > 100:
    print("Ошибка входных данных")
else:
    A = list(map(int, input("A: ").split()))
    x = int(input("x: "))
    pos = 0
    for i in range(1, n + 1):
        if A[i - 1] == x:
            pos = i
            break
    print(pos if pos else "Элемент не найден")
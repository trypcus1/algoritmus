n = int(input("n: "))
if n < 1 or n > 100:
    print("Ошибка входных данных")
else:
    A = list(map(int, input("A: ").split()))
    ordered = True
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            ordered = False
            break
    print("Упорядочен" if ordered else "Не упорядочен")
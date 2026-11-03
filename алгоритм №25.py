n = int(input("n: "))
if n < 1 or n > 20:
    print("Ошибка входных данных")
else:
    A = list(map(int, input("A: ").split()))
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    print(A)
n = int(input("n: "))
if n < 1 or n > 100:
    print("Ошибка входных данных")
else:
    A = list(map(int, input("A: ").split()))
    left, right = 0, n - 1
    while left < right:
        A[left], A[right] = A[right], A[left]
        left += 1
        right -= 1
    print(A)
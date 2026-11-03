s = input("s: ")
if len(s) < 1 or len(s) > 100:
    print("Ошибка входных данных")
else:
    left, right = 0, len(s) - 1
    pal = True
    while left < right:
        if s[left] != s[right]:
            pal = False
            break
        left += 1
        right -= 1
    print("Палиндром" if pal else "Не палиндром")
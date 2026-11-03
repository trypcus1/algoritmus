s = input("s: ")
if len(s) > 100:
    print("Ошибка входных данных")
else:
    count = 0
    for ch in s:
        if ch in "aeiou":
            count += 1
    print(count)
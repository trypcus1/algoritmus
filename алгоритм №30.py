s = input("s: ")
if len(s) > 100:
    print("Ошибка входных данных")
else:
    balance = 0
    valid = True
    for ch in s:
        if ch == "(":
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                valid = False
                break
    print("Правильная" if valid and balance == 0 else "Неправильная")
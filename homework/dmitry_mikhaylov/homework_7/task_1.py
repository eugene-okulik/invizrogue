goal = 7
while True:
    attempt = int(input("Угадайте число от 1 до 10: "))
    if attempt == goal:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова\n")

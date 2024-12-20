import random


salary = int(input("Введите зарплату: "))
bonus = random.choice([True, False])

print(f"{salary}, {bonus} - "
      f"'${salary + (int(random.randrange(5000)) if bonus else 0)}'")

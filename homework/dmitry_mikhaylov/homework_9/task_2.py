temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22,
                22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_days = list(filter(lambda x: x > 28, temperatures))

print(f'Максимальная температура: {max(temperatures)}')
print(f'Минимальная температура: {min(temperatures)}')
print(f'Средняя температура: {round(sum(temperatures) / len(temperatures), 2)}')

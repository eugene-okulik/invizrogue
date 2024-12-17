string_1 = 'результат операции: 42'
string_2 = 'результат операции: 514'
string_3 = 'результат работы программы: 9'

number_1 = int(string_1[string_1.index(':') + 2:])
number_2 = int(string_2[string_2.index(':') + 2:])
number_3 = int(string_3[string_3.index(':') + 2:])

number_1 += 10
number_2 += 10
number_3 += 10

print(number_1)
print(number_2)
print(number_3)

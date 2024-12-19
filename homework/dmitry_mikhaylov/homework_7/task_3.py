def increase_parsed_number(string):
    return int(string.split()[-1]) + 10


string_1 = 'результат операции: 42'
string_2 = 'результат операции: 54'
string_3 = 'результат работы программы: 209'
string_4 = 'результат: 2'

print(increase_parsed_number(string_1))
print(increase_parsed_number(string_2))
print(increase_parsed_number(string_3))
print(increase_parsed_number(string_4))

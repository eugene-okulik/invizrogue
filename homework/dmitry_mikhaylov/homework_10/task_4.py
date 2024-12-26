PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

my_dict = {key: int(value[:-1]) for key, value
           in [tuple(x.split()) for x in PRICE_LIST.split('\n')]}
# print(my_dict)

my_dict = {}

my_dict['tuple'] = (1, 2, 'three', -4, 5.0, 'last')
my_dict['list'] = [1, 2, "three", -4, 5.0, 'not_last', 1]
my_dict['dict'] = {'first': 1, 'second': 2, 3: 'three',
                   'negative': -4, 'float': 5.0, -1: 'last'}
my_dict['set'] = set(my_dict['list'])

print(my_dict['tuple'][-1])

my_dict['list'].append('very_last')
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple'] = 42
del my_dict['dict']['second']

my_dict['set'].add(999999)
my_dict['set'].remove(1)

print(my_dict)

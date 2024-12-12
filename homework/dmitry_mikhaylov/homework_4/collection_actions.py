my_dict = {}

for collection_type in ['tuple', 'list', 'dict', 'set']:
    if collection_type == 'tuple':
        my_dict[collection_type] = (1, 2, 'three', -4, 5.0, 'last')
    if collection_type == 'list':
        my_dict[collection_type] = [1, 2, "three", -4, 5.0, 'not_last', 1]
    if collection_type == 'dict':
        my_dict[collection_type] = {'first': 1, 'second': 2, 3: 'three',
                                    'negative': -4, 'float': 5.0, -1: 'last'}
    if collection_type == 'set':
        my_dict[collection_type] = set(my_dict['list'])

for collection_type in my_dict.keys():
    if collection_type == 'tuple':
        print(my_dict[collection_type][-1])
    if collection_type == 'list':
        my_dict[collection_type].append('very_last')
        my_dict[collection_type].pop(1)
    if collection_type == 'dict':
        my_dict[collection_type]['42'] = 42
        del my_dict[collection_type]['second']
    if collection_type == 'set':
        my_dict[collection_type].add(999999)
        my_dict[collection_type].remove(1)

print(my_dict)

def print_keys(key, seq):
    for _ in range(seq):
        print(key, end='')
    print()


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, seq in words.items():
    print_keys(key, seq)

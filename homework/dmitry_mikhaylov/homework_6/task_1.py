text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = text.split()

new_words = []
for word in words:
    if word.endswith(',') or word.endswith('.'):
        sign = word[-1:]
        word = word[:-1]
        new_words.append(word + 'ing' + sign)
    else:
        new_words.append(word + 'ing')

print(' '.join(new_words))

# Текст взят из https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC

punks = ['!', '"', '#', '$', '%', '&', "'",
         '(', ')', '*', '+', ',', '-', '.',
         '/', ':', ';', '<', '=', '>', '?',
         '@', '[', '\\', ']', '^', '_', '`',
         '{', '|', '}', '~', '—']

with open('algorithm.txt', 'r') as file:
    content = file.read().replace('\n', ' ')

for punk in punks:
    content = content.replace(punk, '')

words = []

for word in content.split(' '):
    if not word.isspace() and word != '':
        words.append(word.lower())

words_counter_map = {}

for word in words:
    if word not in words_counter_map.keys():
        words_counter_map[word] = words.count(word)

max_repite_words_counter_map = dict(sorted(words_counter_map.items(), key=lambda x: -x[1])[:10])

print(max_repite_words_counter_map)

words = 'stars glitter turquoise violet buttercup venus diamonds sparkles horoscope'.split()

import random

random.shuffle(words)

random_word = words.pop()

for i in range(8):
    random.shuffle(words)
    random_word = words.pop()
    print(random_word)

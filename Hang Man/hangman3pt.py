import random

words = 'automobile computer laptop flags apple'.upper().split()

random.shuffle(words)
random_word = words.pop()

print(" The random word is %s " % random_word)
print("\n\n")

# Example 1- Print a word using a for loop.
print("--------- Printing a full word with a for loop ----------")
for i in random_word:
    print (i, end = ' ')
print("\n\n")

#Example 2- print a word with blanks instead of letters.
print("----- Print a full word with_ instead of letters -----")

for i in random_word:
    print('_', end = ' ')
print("\n\n")

# Print a word with only vowels showing

print("----- Print only the vowels in a given word -----")
for i in random_word:
    if i in 'AEIOU':
        print(i, end = ' ')
    else:
        print('_', end = ' ')
print("\n\n")

# Print a word with only consonants.
print("----- Print only the consonants in a given worm -----")
for i in random_word:
    if i  not in 'AEIOU':
        print(i, end= ' ')
    else:
        print('_', end=' ')
print()


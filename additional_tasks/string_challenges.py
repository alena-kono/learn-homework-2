# Вывести последнюю букву в слове
task = 'Вывести последнюю букву в слове'
word = 'Архангельск'
last_letter = word[-1]
print(f'{task} "{word}":\n{last_letter}')


# Вывести количество букв "а" в слове
task = 'Вывести количество букв "а" в слове'
word = 'Архангельск'
a_count = list(word.lower()).count('а')
print(f'{task} "{word}":\n{a_count}')


# Вывести количество гласных букв в слове
task = 'Вывести количество гласных букв в слове'
word = 'Архангельск'
VOWELS = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

sum_vowels = 0
for char in word.lower():
    if char in VOWELS:
        sum_vowels += 1
print(f'{task} "{word}":\n{sum_vowels}')


# Вывести количество слов в предложении
task = 'Вывести количество слов в предложении'
sentence = 'Мы приехали в гости'
word_count = len(sentence.split())
print(f'{task} "{sentence}":\n{word_count}')


# Вывести первую букву каждого слова на отдельной строке
task = 'Вывести первую букву каждого слова на отдельной строке'
sentence = 'Мы приехали в гости'
print(f'{task} "{sentence}":')

for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова.
task = 'Вывести усреднённую длину слова в'
sentence = 'Мы приехали в гости'

total_length = 0
for word in sentence.split():
    total_length += len(word)
ave_length = total_length/len(sentence.split())

print(f'{task} "{sentence}":\n{ave_length}')
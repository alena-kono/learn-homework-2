"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as user_file:
        user_file_content  = user_file.read()
        string_len = f'Length of the string: {len(user_file_content)}'
        words_count = f'Words count: {len(user_file_content.split())}'
        user_file_content = user_file_content.replace('.', '!')

    with open('referat2.txt', 'w', encoding='utf-8') as user_file:
        user_file.write('\n'.join((string_len, words_count, '')))
        user_file.write(user_file_content)


if __name__ == "__main__":
    main()

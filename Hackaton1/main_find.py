from find_modules import *


book_names = ['01-Азазель.txt', "02-Статский-советник.txt", "03-Турецкий-гамбит.txt"]  # c Список назв книг
books = read_books(book_names)  # c Словник {назва книги: книга}
indents = {name: count_indents(book) for name, book in books.items()}  # c Словник {назва книги: к-сть абз}
cipher = {1620: 11, 2025: 31, 775: 37, 76: 3}  # c Шифр {абзац: слово}

message = []

for indent_number, word_number in cipher.items():
    for book_name, book_text in books.items():
        if indent_number < indents[book_name]:
            indent = get_indent(book_text, indent_number)
            word = get_word(indent, word_number)
            # if word != -1:
            #     message.append(word)
            #     break
            message.append((book_name, indent_number, word_number, word))

# decipher = ' '.join(message)
# print(decipher)
for i in message:
    print(i)

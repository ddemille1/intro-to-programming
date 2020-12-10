with open("books_and_chapters.txt") as data:

    most_chapters = -1
    longest_book = ""

    for line in data:
        part = line.split(":")
        book = part[0].strip()
        chapter_number = int(part [1])
        scripture = part[2].strip()
        print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapter_number}')

        if chapter_number > most_chapters:
            most_chapters = chapter_number
            longest_book = book

print (f'The most chapters is {most_chapters}. The longest book is {longest_book}.')





with open("books_and_chapters.txt") as data:

    bom_most_chapters = -1
    bom_longest_book = ""

    for line in data:
        part = line.split(":")
        book = part[0].strip()
        chapter_number = int(part [1])
        scripture = part[2].strip()

        if scripture.lower() == 'book of mormon':
            print(f'Scripture: {scripture}, Book: {book}, Chapters: {chapter_number}')

            if chapter_number > bom_most_chapters:
                bom_most_chapters = chapter_number
                bom_longest_book = book

print (f'The longest book in the Book of Mormon is {bom_longest_book}. It has {bom_most_chapters} chapters.')





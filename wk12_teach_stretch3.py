with open("books_and_chapters.txt") as data:
    
    user_choice = input('Which volume of scripture would you like to learn about? ')
    most_chapters = -1
    longest_book = ""

    for line in data:
        part = line.split(":")
        book = part[0].strip()
        chapter_number = int(part [1])
        scripture = part[2].strip()

        if scripture.lower() == user_choice:

            if chapter_number > most_chapters:
                most_chapters = chapter_number
                longest_book = book

print (f'The longest book in {user_choice} is {longest_book}. It has {most_chapters} chapters.')

         

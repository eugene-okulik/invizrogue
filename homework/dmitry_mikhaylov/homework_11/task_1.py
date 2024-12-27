class Book:
    page_material = 'бумага'
    text_presence = True

    def __init__(self, book_title, author, page_count, isbn, reserved=False):
        self.book_title = book_title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved

    def book_info(self):
        book_info = (f'Название: {self.book_title}, '
                     f'Автор: {self.author}, '
                     f'страниц: {self.page_count}, '
                     f'материал: {self.page_material}')
        if self.reserved:
            book_info += ', зарезервирована'
        print(book_info)


class Schoolbook(Book):
    has_tasks = True

    def __init__(self, book_title, author, page_count,
                 isbn, subject, grade, reserved=False):
        super().__init__(book_title, author, page_count, isbn, reserved)
        self.subject = subject
        self.grade = grade

    def book_info(self):
        book_info = (f'Название: {self.book_title}, '
                     f'Автор: {self.author}, '
                     f'страниц: {self.page_count}, '
                     f'предмет: {self.subject}, '
                     f'класс: {self.grade}')
        if self.reserved:
            book_info += ', зарезервирована'
        print(book_info)


book_1 = Book('Три мушкетёра', 'Дюма', 704,
              '5-7586-0001-6')
book_2 = Book('Пером и шпагой', 'Пикуль', 416,
              '5-87144-001-0', True)
book_3 = Book('Записки сумасшедшего', 'Гоголь', 318,
              '5-87107-040-X')
book_4 = Book('На заре ты ее не буди', 'Фет', 640,
              '978-5-699-56140-7')
book_5 = Book('Басни', 'Эзоп', 336,
              '5-7406-0243-2')

book_1.book_info()
book_2.book_info()
book_3.book_info()
book_4.book_info()
book_5.book_info()

schoolbook_1 = Schoolbook('История отечества', 'Петров', 200,
                          '5-7586-0001-6', 'История', '5')
schoolbook_2 = Schoolbook('Математика. 3 класс', 'Иванов', 177,
                          '5-7586-0001-6', 'Математика', '3', True)
schoolbook_3 = Schoolbook('Физика. 7 класс', 'Сидоров', 250,
                          '5-7586-0001-6', 'Физика', '7')

schoolbook_1.book_info()
schoolbook_2.book_info()
schoolbook_3.book_info()

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book():
    def __init__(self,id_:int,name:str,pages:int):
        """
        Создание объекта книга
        :param id_: id книги
        :param name: имя книги
        :param pages: число страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id_ = {self.id},name = {self.name!r},pages = {self.pages})'

# TODO написать класс Library
class Library():
    def __init__(self,books=[]):
        """
        :param books: список книг в библиотеке
        """
        self.books = books

    def get_next_book_id(self) -> int:
        """
        :return:  Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
        """
        return (len(self.books) +1)

    def get_index_by_book_id(self, id:int) -> int:
        """
        :param id: id книги, индекс которой хотим получить
        :return: Метод, возвращающий индекс книги в списке
        """
        for item in enumerate(self.books,start=1):
            if item[1].id == id:
                return item[0]

        raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

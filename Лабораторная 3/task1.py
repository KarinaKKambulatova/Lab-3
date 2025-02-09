import doctest

class Book:
    """ Базовый класс книги.

    Пример свойства getter для атрибута name:
    >>> book = Book('Преступление и наказание', 'Ф.М. Достовеский')
    >>> name = book.name
    >>> print(name)
    Преступление и наказание

    Пример свойства getter для атрибута author:
    >>> book = Book('Преступление и наказание', 'Ф.М. Достовеский')
    >>> author = book.author
    >>> print(author)
    Ф.М. Достовеский
    """
    def __init__(self, name: str, author: str):
        """
        Создание экземпляра класса.
        :param name: Название книги.
        :param author: Автор книги.

        Пример:
        >>> book = Book('Преступление и наказание', 'Ф.М. Достовеский')
        """
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        self._name = name
        self._author = author

    def __str__(self):
        """
        Функция, которая возвращает строку с названием книги.
        :return: Строка, которая предназначена для чтения людьми.

        Пример:
        >>> book = Book('Преступление и наказание', 'Ф.М. Достовеский')
        >>> print(book)
        Книга Преступление и наказание. Автор Ф.М. Достовеский
        """
        return f'Книга {self.name}. Автор {self.author}'

    def __repr__(self):
        """
        Функция, которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр.
        :return: Строка, которая показывает, как может быть инициализирован экземпляр.

        Пример:
        >>> book = Book('Преступление и наказание', 'Ф.М. Достовеский')
        >>> print(f'{book!r}')
        Book(name='Преступление и наказание', author='Ф.М. Достовеский')
        """
        return f'{self.__class__.__name__}(name={self.name!r}, author={self.author!r})'

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook (Book):
    """
    Дочерний класс книги.

    Пример свойства getter для атрибута pages:
    >>> paper_book = PaperBook('Преступление и наказание', 'Ф.М. Достовеский', 600)
    >>> pages = paper_book.pages
    >>> print(pages)
    600

    Пример свойства setter для атрибута pages:
    >>> paper_book = PaperBook('Преступление и наказание', 'Ф.М. Достовеский', 600)
    >>> paper_book.pages = 700
    >>> print(paper_book.pages)
    700
    """
    def __init__(self, name: str, author: str, pages: int):
        """
        Создание экзампляра класса.

        :param name: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц в бумажной книге.

        Пример:
        >>> paper_book = PaperBook('Преступление и наказание', 'Ф.М. Достовеский', 600)
        """
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        """"
        Функция, которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр.
        :return: Строка, которая показывает, как может быть инициализирован экземпляр.

        Пример:
        >>> paper_book = PaperBook('Преступление и наказание', 'Ф.М. Достовеский', 600)
        >>> print(f'{paper_book!r}')
        PaperBook(name='Преступление и наказание', author='Ф.М. Достовеский', pages=600)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook (Book):
    """
    Дочерний класс книги.

    Пример свойства getter для атрибута duration:
    >>> audio_book = AudioBook('Преступление и наказание', 'Ф.М. Достовеский', 25.5)
    >>> duration = audio_book.duration
    >>> print(duration)
    25.5

    Пример свойства setter для атрибута duration:
    >>> audio_book = AudioBook('Преступление и наказание', 'Ф.М. Достовеский', 25.5)
    >>> audio_book.duration = 27.5
    >>> print(audio_book.duration)
    27.5
    """
    def __init__(self, name: str, author: str, duration: float):
        """
        Создание экземпляра класса
        :param name: Название книги.
        :param author: Автор книги.
        :param duration: Продолжительность аудиокниги.

        Пример:
        >>> audio_book = AudioBook('Преступление и наказание', 'Ф.М. Достовеский', 25.5)
        """
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        """"
         Функция, которая возвращает валидную python строку, по которой можно инициализировать точно такой же экземпляр.
        :return: Строка, показывающая, как может быть инициализирован экземпляр.

        Пример:
        >>> audio_book = AudioBook('Преступление и наказание', 'Ф.М. Достовеский', 25.5)
        >>> print(f'{audio_book!r}')
        AudioBook(name='Преступление и наказание', author='Ф.М. Достовеский', duration=25.5)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = new_duration


if __name__ == "__main__":
    doctest.testmod()
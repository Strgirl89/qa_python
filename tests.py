from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_and_set_book_genre(self):
        collector = BooksCollector()
        name = "Дюна"
        genre = "Фантастика"
        collector.add_new_book(name)
        assert name in collector.books_genre
        collector.set_book_genre(name, genre)
        result = collector.get_book_genre(name)
        expected = genre
        assert expected == result

    import pytest
    @pytest.mark.parametrize("name, expected_result", [
        ("Каштанка", True),
        ("", False),  # Пустая строка
        ("N" * 42, False),  # Строка длиной 42 символа
    ])
    def test_add_new_book(self, name, expected_result):
        collector = BooksCollector()
        collector.add_new_book(name)
        result = name in collector.books_genre
        assert result == expected_result

    def test_get_book_genre_existing_book(self):
        collector = BooksCollector()
        collector.books_genre["Ревизор"] = "Комедия"
        assert collector.books_genre ["Ревизор"] == "Комедия"

    def test_get_books_with_specific_genre_non_existence(self):
        collector = BooksCollector()
        collector.books_genre = {"Детективы": ["Десять негритят","Милые кости"]}
        assert collector.get_books_with_specific_genre("Ужасы") == []


    def test_get_books_genre(self):
        collector = BooksCollector()
        result = collector.get_books_genre()
        expected = {}
        assert result == expected

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.books_genre = {"Каштанка": "Мультфильмы", "Незнайка на Луне": "Мультфильмы", "Дракула": "Ужасы"}
        collector.genre = ["Мультфильмы"]
        collector.genre_age_rating = {}
        expected_result = ["Каштанка", "Незнайка на Луне"]
        result = collector.get_books_for_children()
        assert result == expected_result

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.books_genre = {"Каштанка": "Мультфильмы"}
        name = "Каштанка"
        collector.add_book_in_favorites(name)
        assert "Каштанка" in collector.favorites

    def test_delete_book_from_favorites_non_existence(self):
        collector = BooksCollector()
        collector.books_genre = {"Незнайка на Луне": "Мультфильмы"}
        name = "Незнайка на Луне"
        collector.delete_book_from_favorites(name)
        assert "Незнайка на Луне" not in collector.favorites

    def test_get_list_of_favorites(self):
        collector = BooksCollector()
        result = collector.get_list_of_favorites_books()
        expected = []
        assert result == expected









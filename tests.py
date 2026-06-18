import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


def test_add_new_book_add_two_books(collector):
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')

    assert len(collector.get_books_genre()) == 2


def test_add_new_book_not_add_book_with_name_longer_than_40_symbols(collector):
    long_name = 'А' * 41

    collector.add_new_book(long_name)

    assert long_name not in collector.get_books_genre()


def test_set_book_genre_sets_valid_genre(collector):
    collector.add_new_book('Дюна')

    collector.set_book_genre('Дюна', 'Фантастика')

    assert collector.get_book_genre('Дюна') == 'Фантастика'


def test_get_book_genre_returns_genre_by_name(collector):
    collector.add_new_book('Шерлок Холмс')
    collector.set_book_genre('Шерлок Холмс', 'Детективы')

    assert collector.get_book_genre('Шерлок Холмс') == 'Детективы'


def test_get_books_with_specific_genre_returns_books_of_selected_genre(collector):
    collector.add_new_book('Дюна')
    collector.add_new_book('Оно')

    collector.set_book_genre('Дюна', 'Фантастика')
    collector.set_book_genre('Оно', 'Ужасы')

    assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']


def test_get_books_for_children_returns_books_without_age_rating(collector):
    collector.add_new_book('Дюна')
    collector.add_new_book('Оно')

    collector.set_book_genre('Дюна', 'Фантастика')
    collector.set_book_genre('Оно', 'Ужасы')

    assert collector.get_books_for_children() == ['Дюна']


def test_add_book_in_favorites_adds_book_to_favorites(collector):
    collector.add_new_book('Дюна')

    collector.add_book_in_favorites('Дюна')

    assert 'Дюна' in collector.get_list_of_favorites_books()


def test_add_book_in_favorites_not_add_duplicate_book(collector):
    collector.add_new_book('Дюна')

    collector.add_book_in_favorites('Дюна')
    collector.add_book_in_favorites('Дюна')

    assert len(collector.get_list_of_favorites_books()) == 1


def test_delete_book_from_favorites_removes_book(collector):
    collector.add_new_book('Дюна')

    collector.add_book_in_favorites('Дюна')
    collector.delete_book_from_favorites('Дюна')

    assert 'Дюна' not in collector.get_list_of_favorites_books()


def test_get_list_of_favorites_books_returns_favorites_list(collector):
    collector.add_new_book('Дюна')

    collector.add_book_in_favorites('Дюна')

    assert collector.get_list_of_favorites_books() == ['Дюна']
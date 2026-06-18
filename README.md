# qa_python

## Описание проекта

Проект содержит класс `BooksCollector` и набор автотестов для проверки его работы с использованием `pytest`.

### Реализованный функционал

* добавление новых книг;
* установка жанра книге;
* получение жанра книги;
* получение списка книг определённого жанра;
* получение списка книг для детей;
* добавление книги в избранное;
* удаление книги из избранного;
* получение списка избранных книг.

## Технологии

* Python 3.14
* Pytest 9.0.3

## Запуск тестов

Перейдите в директорию проекта:

```bash
cd qa_python
```

Запустите тесты:

```bash
python -m pytest -v tests.py
```

## Реализованные тесты

* `test_add_new_book_add_two_books` - Добавление двух книг
* `test_add_new_book_not_add_book_with_name_longer_than_40_symbols` - Книга с названием более 40 символов не добавляется
* `test_set_book_genre_sets_valid_genre` - Установка корректного жанра книге
* `test_get_book_genre_returns_genre_by_name` - Получение жанра книги по названию
* `test_get_books_with_specific_genre_returns_books_of_selected_genre` - Получение списка книг заданного жанра
* `test_get_books_for_children_returns_books_without_age_rating` - Получение списка детских книг без возрастных ограничений
* `test_add_book_in_favorites_adds_book_to_favorites` - Добавление книги в избранное
* `test_add_book_in_favorites_not_add_duplicate_book` - Проверка отсутствия дубликатов в избранном
* `test_delete_book_from_favorites_removes_book` - Удаление книги из избранного
* `test_get_list_of_favorites_books_returns_favorites_list` - Получение списка избранных книг

## Результат запуска тестов

```text
========================== 10 passed in 0.04s ==========================
```

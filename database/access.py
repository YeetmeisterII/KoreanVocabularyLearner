import sqlite3
from typing import Tuple, Any

from database.connection import WordStorageConnection
from database.word import Word


class Access:
    @staticmethod
    def _get_rows(query: str) -> Tuple[Tuple[Any, ...], ...]:
        try:
            connection = WordStorageConnection()
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            connection.close()
        except sqlite3.Error as error:
            print(error)
            exit(0)
        return tuple(rows)

    @staticmethod
    def _get_ids(query: str) -> Tuple[int, ...]:
        row: Tuple[int]
        return tuple(row[0] for row in Access._get_rows(query))

    @staticmethod
    def get_unit_ids() -> Tuple[int, ...]:
        query = "SELECT unit_id FROM main.units"
        return Access._get_ids(query)

    @staticmethod
    def get_lesson_ids(unit_id) -> Tuple[int, ...]:
        query = f"SELECT lesson_id FROM main.lessons WHERE unit_id = {unit_id}"
        return Access._get_ids(query)

    @staticmethod
    def get_word_ids(lesson_id) -> Tuple[int, ...]:
        query = f"SELECT word_id FROM lesson_word WHERE lesson_id = {lesson_id}"
        return Access._get_ids(query)

    @staticmethod
    def get_lesson_titles(lesson_id: Tuple[int, ...]) -> Tuple[str, ...]:
        lesson_id_str = ', '.join(map(str, lesson_id))
        query = f"SELECT title FROM lessons WHERE lesson_id IN ({lesson_id_str})"
        row: Tuple[str]
        return tuple(row[0] for row in Access._get_rows(query))

    @staticmethod
    def get_words(word_ids: Tuple[int, ...]) -> Tuple[Word, ...]:
        word_ids_str = ', '.join(map(str, word_ids))
        query = f"SELECT word_id, english, korean, success_rating FROM words WHERE word_id IN ({word_ids_str})"
        row: Tuple[int, str, str, int]
        return tuple(Word(*row) for row in Access._get_rows(query))

    @staticmethod
    def update_word_record(word: Word) -> None:
        query = f"Update main.words SET success_rating = {word.get_score()} WHERE word_id = {word.get_id()}"
        try:
            connection = WordStorageConnection()
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.close()
            connection.commit()
            connection.close()
        except sqlite3.Error as error:
            print(error)
            exit(0)

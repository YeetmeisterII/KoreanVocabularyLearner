import sqlite3
from typing import Tuple, Any

from database.connection import WordStorageConnection
from database.word import Word


class Access:
    """
    Methods to Read and Write to the database.
    """

    @staticmethod
    def _get_rows(query: str) -> Tuple[Tuple[Any, ...], ...]:
        """
        Connect to the database, run the query argument and return the retrieved data of every row.
        :param query: Query to execute on the database to select rows.
        :return: Tuple of tuples each representing a row.
        """
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
        """
        Performs the general pattern for all the get id methods.
        :param query: Query to execute on the database to select rows.
        :return:
        """
        row: Tuple[int]
        return tuple(row[0] for row in Access._get_rows(query))

    @staticmethod
    def get_unit_ids() -> Tuple[int, ...]:
        """
        :return: The id of every unit in the database.
        """
        query = "SELECT unit_id FROM main.units"
        return Access._get_ids(query)

    @staticmethod
    def get_lesson_ids(unit_id) -> Tuple[int, ...]:
        """
        Retrieve the id of every lesson within a unit based on its id.
        :param unit_id: unit_id to discriminate lessons in the database by.
        :return: Tuple containing the lesson_ids.
        """
        query = f"SELECT lesson_id FROM main.lessons WHERE unit_id = {unit_id}"
        return Access._get_ids(query)

    @staticmethod
    def get_word_ids(lesson_id) -> Tuple[int, ...]:
        """
        Retrieve the id of every word within a lesson based on its id.
        :param lesson_id:
        :return: Tuple containing the word_ids.
        """
        query = f"SELECT word_id FROM lesson_word WHERE lesson_id = {lesson_id}"
        return Access._get_ids(query)

    @staticmethod
    def get_lesson_titles(lesson_ids: Tuple[int, ...]) -> Tuple[str, ...]:
        """
        Retrieve the title of lessons based on the lesson_ids.
        :param lesson_ids: Ids for the lesson titles to retrieve.
        :return: Tuple containing the lesson titles.
        """
        lesson_id_str = ', '.join(map(str, lesson_ids))
        query = f"SELECT title FROM lessons WHERE lesson_id IN ({lesson_id_str})"
        row: Tuple[str]
        return tuple(row[0] for row in Access._get_rows(query))

    @staticmethod
    def get_words(word_ids: Tuple[int, ...]) -> Tuple[Word, ...]:
        """
        Retrieve the word data based on word_ids and return Word objects based on the row data.
        :param word_ids: Ids for the word records to retrieve.
        :return: Tuple of Word objects.
        """
        word_ids_str = ', '.join(map(str, word_ids))
        query = f"SELECT word_id, english, korean, success_rating FROM words WHERE word_id IN ({word_ids_str})"
        row: Tuple[int, str, str, int]
        return tuple(Word(*row) for row in Access._get_rows(query))

    @staticmethod
    def update_word_record(word: Word) -> None:
        """
        Update the success score of a word record based on it's Word object representation.
        :param word: Word object representation of a word record.
        """
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

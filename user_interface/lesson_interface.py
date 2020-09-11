from typing import Tuple

from hangul_romanize import Transliter
from hangul_romanize.rule import academic

from database.word import Word
from user_interface.base_interface import BaseInterface


class LessonInterface(BaseInterface):
    """
    Interface used during a lesson for user IO.
    """
    _romanize = Transliter(academic).translit

    @staticmethod
    def eng_to_kor(answer: Word):
        """
        Ask the user to translate an english word to Korean.
        :param answer: Word object of the word to translate.
        """
        print(f"Translate '{answer.get_english()}' to Korean?"
              f"")

    @staticmethod
    def eng_to_kor_result(correct: bool, actual_word: Word, input_korean: str) -> None:
        """
        Output whether the attempt to translate an English word to Korean was correct.
        :param correct: If the attempt was successful.
        :param actual_word: Word object of the word to translate.
        :param input_korean: User attempt to translate it.
        """
        actual = f"{actual_word.get_korean()} ({actual_word.get_romanized()})"
        user_input = f"{input_korean} ({LessonInterface._romanize(input_korean)})"
        LessonInterface._result(correct, user_input, actual)

    @staticmethod
    def eng_to_kor_correction(word: Word):
        """
        Tell the user to type the Korean version of a word.
        :param word: Word object of the word.
        """
        print(f"Type '{word.get_korean()}'")

    @staticmethod
    def kor_to_eng(answer_pool: Tuple[Word, Word, Word, Word, Word], answer: Word) -> None:
        """
        Output a word in Korean and options in a list of 1 to 5 that are potential answers.
        :param answer_pool: Potential answers and will include the Word object of the argument 'answer'.
        :param answer: The Word object of the word being tested.
        """
        print(f"What is '{answer.get_korean()}' ({answer.get_romanized()}) in English?")
        for i, word in enumerate(answer_pool, 1):
            print(f"{i}. {word.get_english()}")

    @staticmethod
    def kor_to_eng_result(correct: bool, correct_word: Word, chosen_word: Word) -> None:
        """
        Output whether the attempt to choose the correct English translation of a Korean word was correct.
        :param correct: If the attempt was successful.
        :param correct_word: Word object of the word the user should have chosen.
        :param chosen_word: Word object of the word the user chose.
        """
        LessonInterface._result(correct, chosen_word.get_english(), correct_word.get_english())

    @staticmethod
    def _result(correct: bool, user_input: str, actual: str) -> None:
        """
        Base result method that outputs whether an attempt was correct and the user's answer versus the real answer.
        :param correct: If the attempt was successful.
        :param user_input: User answer.
        :param actual: Actual answer.
        """
        string = f"Your answer:\t\t{user_input}\nExpected answer:\t{actual}\n"
        colour = "green" if correct else "red"
        print(LessonInterface._paint_string(colour, string))

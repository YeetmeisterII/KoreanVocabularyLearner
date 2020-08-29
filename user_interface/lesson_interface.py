from typing import Tuple

from hangul_romanize import Transliter
from hangul_romanize.rule import academic

from database.word import Word
from user_interface.base_interface import BaseInterface


class LessonInterface(BaseInterface):
    """
    Input & Output for translation based questions.
    """
    _romanize = Transliter(academic).translit

    @staticmethod
    def eng_to_kor(answer: Word):
        print(f"Convert '{answer.get_english()}' to Korean?")

    @staticmethod
    def eng_to_kor_result(correct: bool, actual_word: Word, input_korean: str) -> None:
        actual = f"{actual_word.get_korean()} ({actual_word.get_romanized()})"
        user_input = f"{input_korean} ({LessonInterface._romanize(input_korean)})"
        LessonInterface._result(correct, user_input, actual)

    @staticmethod
    def eng_to_kor_correction(word: Word):
        print(f"Type '{word.get_korean()}'")

    @staticmethod
    def kor_to_eng(answer_pool: Tuple[Word, Word, Word, Word, Word], answer: Word) -> None:
        print(f"What is '{answer.get_korean()}' ({answer.get_romanized()}) in English?\n")
        for i, word in enumerate(answer_pool, 1):
            print(f"{i}. {word.get_english()}")

    @staticmethod
    def kor_to_eng_result(correct: bool, correct_word: Word, chosen_word: Word) -> None:
        LessonInterface._result(correct, chosen_word.get_english(), correct_word.get_english())

    @staticmethod
    def _result(correct: bool, user_input: str, actual: str) -> None:
        string = f"Your answer:\t\t{user_input}\nExpected answer:\t{actual}\n"
        colour = "green" if correct else "red"
        print(LessonInterface._paint_string(colour, string))

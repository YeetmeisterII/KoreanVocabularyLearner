import random
from typing import Tuple, Sequence

from database.access import Access
from database.word import Word
from user_interface.lesson_interface import LessonInterface


class Lesson:
    def __init__(self, lesson_id: int):
        self.words = Access.get_words(Access.get_word_ids(lesson_id))

    def main(self) -> None:
        questions = {0: self._kor_to_eng, 1: self._eng_to_kor}
        while True:
            for _ in range(15):
                questions[random.randint(0, 1)]()
                self._update_word_records()

    def _get_word_weights(self, words: Sequence[Word]) -> Tuple[int, ...]:
        return tuple(word.get_score() for word in words)

    def _get_random_word(self, words: Sequence[Word]) -> Word:
        return random.choices(words, weights=self._get_word_weights(words))[0]

    def _get_five_random_words(self) -> Tuple[Word, Word, Word, Word, Word]:
        words_copy = list(self.words)
        five_words = list()
        for _ in range(5):
            word = self._get_random_word(words_copy)
            words_copy.remove(word)
            five_words.append(word)
        return tuple(five_words)

    def _update_word_records(self) -> None:
        for word in self.words:
            word.update_record()

    def _eng_to_kor(self) -> None:
        question_word = self._get_random_word(self.words)
        LessonInterface.eng_to_kor(question_word)
        user_string = LessonInterface.str_input()
        correct = bool(user_string == question_word.get_korean())
        question_word.update_eng_to_kor(correct)
        LessonInterface.eng_to_kor_result(correct, question_word, user_string)
        if not correct:
            self._eng_to_kor_correction(question_word)

    def _eng_to_kor_correction(self, question_word: Word) -> None:
        user_string = None
        while user_string != question_word.get_korean():
            LessonInterface.eng_to_kor_correction(question_word)
            user_string = LessonInterface.str_input()

    def _kor_to_eng(self) -> None:
        five_words = self._get_five_random_words()
        question_word = self._get_random_word(five_words)
        LessonInterface.kor_to_eng(five_words, question_word)
        user_int = five_words[LessonInterface.int_input(5) - 1]
        correct = bool(question_word.get_korean() == user_int.get_korean())
        LessonInterface.kor_to_eng_result(correct, question_word, user_int)
        question_word.update_kor_to_eng(correct)

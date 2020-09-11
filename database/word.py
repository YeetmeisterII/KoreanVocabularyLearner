from hangul_romanize import Transliter
from hangul_romanize.rule import academic


class Word:
    """
    Object representation of a word record that can update the success_rating of that record.
    """
    _romanize = Transliter(academic).translit

    def __init__(self, _id: int, english: str, korean: str, score: int):
        self._id = _id
        self._english = english
        self._korean = korean
        self._romanized = self._romanize(korean)
        self._score = score

    def __repr__(self) -> str:
        return f"<Word(English: '{self._english}', Korean:'{self._korean}')>"

    def get_id(self):
        return self._id

    def get_english(self):
        return self._english

    def get_korean(self):
        return self._korean

    def get_romanized(self):
        return self._romanized

    def get_score(self):
        return self._score

    def update_eng_to_kor(self, correct: bool) -> None:
        self._score += -2 if correct else 1
        if self._score < 10:
            self._score = 0

    def update_kor_to_eng(self, correct: bool) -> None:
        if not correct:
            self._score += 2
        elif 10 < self._score:
            self._score -= 1
        if self._score < 10:
            self._score = 0

    def update_record(self):
        from database.access import Access
        Access.update_word_record(self)

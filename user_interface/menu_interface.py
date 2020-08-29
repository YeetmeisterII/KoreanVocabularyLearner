from typing import Tuple

from user_interface.base_interface import BaseInterface


class MenuInterface(BaseInterface):
    @staticmethod
    def out_unit_options(unit_ids: Tuple[int, ...]) -> None:
        print("Pick a unit.")
        for i, unit_number in enumerate(unit_ids, 1):
            print(f"{i}. Unit {unit_number}")

    @staticmethod
    def out_lesson_options(lesson_titles: Tuple[str, ...]) -> None:
        print("Pick a lesson.")
        for i, lesson_title in enumerate(lesson_titles, 1):
            print(f"{i}. {lesson_title}")

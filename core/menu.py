from core.lesson import Lesson
from database.access import Access
from user_interface.menu_interface import MenuInterface


class Menu:
    def main(self) -> Lesson:
        unit_id = self._unit_selection()
        lesson_id = self._lesson_selection(unit_id)
        return Lesson(lesson_id)

    def _unit_selection(self) -> int:
        unit_ids = Access.get_unit_ids()
        MenuInterface.out_unit_options(unit_ids)
        unit_id_index = MenuInterface.int_input(len(unit_ids)) - 1
        return unit_ids[unit_id_index]

    def _lesson_selection(self, unit_id: int) -> int:
        lesson_ids = Access.get_lesson_ids(unit_id)
        MenuInterface.out_lesson_options(Access.get_lesson_titles(lesson_ids))
        lesson_id_index = MenuInterface.int_input(len(lesson_ids)) - 1
        return lesson_ids[lesson_id_index]

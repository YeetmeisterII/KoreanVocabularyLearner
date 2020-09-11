from core.lesson import Lesson
from database.access import Access
from user_interface.menu_interface import MenuInterface


class Menu:
    """
    Class for choosing a lesson to do.
    """

    def main(self) -> Lesson:
        """
        Lets the user select an unit and then lesson from that unit.
        :return: Lesson object.
        """
        unit_id = self._unit_selection()
        lesson_id = self._lesson_selection(unit_id)
        return Lesson(lesson_id)

    def _unit_selection(self) -> int:
        """
        Has the user choose a unit to learn from.
        :return: Unit id.
        """
        unit_ids = Access.get_unit_ids()
        MenuInterface.out_unit_options(unit_ids)
        unit_id_index = MenuInterface.int_input(len(unit_ids)) - 1
        return unit_ids[unit_id_index]

    def _lesson_selection(self, unit_id: int) -> int:
        """
        Has the user choose a lesson from the previously selected unit to learn from.
        :param unit_id: Unit selected.
        :return: Lesson id.
        """
        lesson_ids = Access.get_lesson_ids(unit_id)
        MenuInterface.out_lesson_options(Access.get_lesson_titles(lesson_ids))
        lesson_id_index = MenuInterface.int_input(len(lesson_ids)) - 1
        return lesson_ids[lesson_id_index]

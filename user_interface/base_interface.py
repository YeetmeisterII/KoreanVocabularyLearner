class BaseInterface:
    """
    Contains the methods all Interface classes should have.
    """
    _colours = {"red": "\u001b[31;1m", "green": "\u001b[32;1m"}

    @staticmethod
    def _paint_string(colour: str, string: str) -> str:
        """
        Wrap escape codes on a string to change it's colour when printed to the console.
        :param colour: Option between red and green.
        :param string: String to be wrapped.
        :return: The same as the string argument but with a specified colour when printed.
        """
        return f"{BaseInterface._colours[colour]}{string}\u001b[0m"

    @staticmethod
    def _out_invalid_input() -> None:
        print("Invalid Input\n")

    @staticmethod
    def int_input(maximum: int) -> int:
        """
        Ask for an input. Repeated unless the input is an integer between [1, maximum] (inclusive, inclusive).
        :param maximum: Maximum value the integer can be.
        :return: Integer inputted by the user.
        """
        while True:
            try:
                user_int = int(input(">>> "))
                if 1 <= user_int <= maximum:
                    print()
                    return user_int
            except ValueError:
                pass
            print()
            BaseInterface._out_invalid_input()

    @staticmethod
    def str_input():
        """
        Ask for an input. Repeat if the input is empty.
        :return: Inputted string.
        """
        while True:
            user_int = input(">>> ")
            print()
            if user_int:
                return user_int
            BaseInterface._out_invalid_input()

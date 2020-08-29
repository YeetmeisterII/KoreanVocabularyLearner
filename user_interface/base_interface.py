class BaseInterface:
    _colours = {"red": "\u001b[31;1m", "green": "\u001b[32;1m"}

    @staticmethod
    def _paint_string(colour: str, string: str) -> str:
        return f"{BaseInterface._colours[colour]}{string}\u001b[0m"

    @staticmethod
    def _out_invalid_input() -> None:
        print("Invalid Input\n")

    @staticmethod
    def int_input(maximum: int) -> int:
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
        while True:
            user_int = input(">>> ")
            print()
            if user_int:
                return user_int
            BaseInterface._out_invalid_input()

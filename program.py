import os
from typing import List


def clear_terminal():
    os.system("cls||clear")


def print_section(title: str, data: List[str]):
    data_copy = data.copy()
    data_copy.append(title)

    print(title)
    print("-" * max([len(line) for line in data_copy]))
    print(*data, sep="\n", end="\n\n")


class Program:

    def __init__(self):
        self._running = False

    def run(self):
        self._running = True
        while self._running:
            clear_terminal()
            self._prompt()

    def _prompt_file_name(self):
        path = os.getcwd() + "\\data\\"
        if not os.path.isdir(path):
            os.mkdir(path)

        available_files = os.listdir(path)
        print_section("Available Files", available_files)

        if not available_files:
            return

        result = ""
        while result == "":
            result = input("Which file would you like to read from?")

            if result == "quit":
                self._running = False
                return

            if not result in available_files and result:
                print(f"{result} is not an available file.")
                result = ""

        return result

    def _prompt(self):
        file_name = self._prompt_file_name()

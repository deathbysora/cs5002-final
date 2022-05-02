import os
import re

from pandas import read_csv

from data_plotter import DataPlotter

SOURCE_PATH = "data\\cities\\"


def main() -> None:
    for file_name in os.listdir(SOURCE_PATH):
        print(f"beginning operation on {file_name}")
        airport = re.findall(r"[A-Z]{3}", file_name)[0]
        handler = DataPlotter(airport, read_csv(SOURCE_PATH + file_name))
        handler.run()


if __name__ == "__main__":
    main()

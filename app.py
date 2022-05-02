import os
import re

from pandas import read_csv

from data_plotter import DataPlotter


def main() -> None:
    source_path = "data\\cities\\"
    for file_name in os.listdir(source_path):
        print(f"beginning operation on {file_name}")
        airport = re.findall(r"[A-Z]{3}", file_name)[0]
        handler = DataPlotter(airport, read_csv(source_path + file_name))
        handler.run()


if __name__ == "__main__":
    main()

import os
import re

import pandas


def main() -> None:
    source_path = "data\\cities\\"
    for file_name in os.listdir(source_path):
        print(f"beginning operation on {file_name}")
        airport = re.findall(r"[A-Z]{3}", file_name)[0]
        data = pandas.read_csv(source_path + file_name)

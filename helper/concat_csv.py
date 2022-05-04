"""Combines all csv files in a directory into one csv."""
import os

import pandas


def main():
    """Entry Point."""
    source = "data\\source\\"
    file_paths = [source + name for name in os.listdir(source)]
    combined = pandas.concat([pandas.read_csv(file_path)
                              for file_path in file_paths])
    combined.to_csv(source + "combined_data.csv", index=False)


if __name__ == "__main__":
    main()

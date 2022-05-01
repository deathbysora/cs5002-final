"""Combines csv's into one."""
import os
import pandas


def main():
    """Entry Point."""
    source = os.getcwd() + r"\source"
    file_names = [source + "\\" + name for name in os.listdir(source)]
    combined_csv = pandas.concat([pandas.read_csv(file)
                                 for file in file_names])
    combined_csv.to_csv("combined_data.csv", index=False)


if __name__ == "__main__":
    main()

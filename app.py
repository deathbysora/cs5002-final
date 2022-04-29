"""Quick reading of data from combined."""

# import csv
# import os
# from typing import Dict, List, Tuple
# import time
# from graph import display

# WANTED = [
#     "JFK",
#     "AUS",
#     "HNL",
#     "MIA",
#     "LAX",
# ]

# header: List[str]
# columns: Dict[str, int]

# FILTERED_PATH = os.getcwd() + "\\filtered"


# def read_data() -> Dict[str, List[List[str]]]:
#     result: Dict[str, List[List[str]]] = {}
#     with open("combined_data.csv", "r") as file:
#         reader = csv.reader(file)

#         global header
#         header = next(reader)

#         global columns
#         columns = {key: index for index, key in enumerate(header)}

#         line = next(reader, None)
#         while not line is None:
#             key = line[columns["ORIGIN"]] + line[columns["DEST"]]
#             key = key.replace("SEA", "")
#             if key in WANTED:
#                 if key in result:
#                     result[key].append(line)
#                 else:
#                     result[key] = [line]

#             line = next(reader, None)

#     return result


# def print_quick_results(collected: Dict[str, List[List[str]]]):
#     print("RESULTS", "-" * 10)
#     for key, collection in collected.items():
#         destination_count = sum(
#             [1 for entry in collection if entry[columns["DEST"]] == key])
#         origin_count = sum(
#             [1 for entry in collection if entry[columns["ORIGIN"]] == key])
#         print(
#             f"SEA -> {key}: {destination_count}",
#             f"{key} -> SEA: {origin_count}",
#             f"{key} total: {len(collection)}",
#             sep="\n")
#         print()


# def create_filtered_files(collected: Dict[str, List[List[str]]]):
#     if not os.path.isdir(FILTERED_PATH):
#         os.mkdir(FILTERED_PATH)

#     for key, data in collected.items():
#         file_path = FILTERED_PATH + "\\" + key + ".csv"
#         with open(file_path, "w", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow(header)
#             writer.writerows(data)


# def collect_data(file_name: str) -> List[Tuple[str, float]]:
#     path = FILTERED_PATH + "\\" + file_name
#     if not os.path.isfile(path):
#         raise FileNotFoundError(
#             f"{file_name} does not exist in {FILTERED_PATH}")

#     with open(path, "r") as file:
#         reader = csv.reader(file)
#         line = next(reader)
#         line = next(reader)
#         result: List[Tuple[str, float]] = []
#         while not line is None:
#             result.append(
#                 (line[columns["FL_DATE"]], line[columns["DEP_DELAY"]]))
#             line = next(reader, None)

#     return result


# def main():
#     """Entry point."""
#     if input("Collect data: ") == "y":
#         print("Running...")
#         start = time.time()
#         collected = read_data()
#         duration = time.time() - start
#         print(f"Took {round(duration, 3)} seconds.\n")

#         print_quick_results(collected)
#         create_filtered_files(collected)

#     austin_data = collect_data("AUS.csv")
#     x, y = map(list, zip(*austin_data))
#     display(x, y)

def main():
    path = os.getcwd() + "\\data\\"
    file_name =


if __name__ == "__main__":
    main()

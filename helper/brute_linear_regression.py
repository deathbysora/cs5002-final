import csv
import re
from typing import Any, Dict, List


def extract(value: str) -> float:
    if re.match(r"\d+\.?\d+", value):
        return float(value)

    return float(0)


def analyze(xkey: str, ykey: str, data: List[List[str]], columns: Dict[str, int]):
    x = [extract(line[columns[xkey]]) for line in data]
    y = [extract(line[columns[ykey]]) for line in data]

    xmean = sum(x) / len(x)
    ymean = sum(y) / len(y)

    xdifference = list(map(lambda x: x - xmean, x))
    ydifference = list(map(lambda y: y - ymean, y))

    numerator = sum(map(lambda x, y: x * y, xdifference, ydifference))
    denominator = sum(map(lambda x: x**2, xdifference))

    result = numerator / denominator

    print(xkey, "x", ykey)
    print("mean:", round(xmean, 3), round(ymean, 3))
    print("R^2:", round(result, 3))
    print("\n\n")


def main():
    path = "data\\weather.csv"
    with open(path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [line for line in reader]

    columns = {label: value for value, label in enumerate(header)}

    xs = [
        "DEP_TIME",
        "OP_CARRIER_AIRLINE_ID",
    ]

    ykey = "DEP_DELAY"
    for xkey in xs:
        analyze(xkey, ykey, data, columns)

"""
for each field:
    for each airport:
        linear regression(depdelay, field)
        save to 
"""

if __name__ == "__main__":
    main()

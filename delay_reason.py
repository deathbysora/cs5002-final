from typing import Dict

import seaborn
from matplotlib import pyplot
from pandas import DataFrame, read_csv


def filter_reasons(data: DataFrame) -> Dict[str, int]:
    headers = [
        "CARRIER_DELAY",
        "WEATHER_DELAY",
        "NAS_DELAY",
        "SECURITY_DELAY",
        "LATE_AIRCRAFT_DELAY",
    ]

    result: Dict[str, int] = {}
    for header in headers:
        filtered = data[data[header] > 0]
        key = header
        key = key.replace("_DELAY", "")
        key = key.replace("_", " ")
        key = key.title()
        result[key] = len(filtered)

    total_length = len(data)
    result["None"] = total_length - sum(result.values())
    return result


def main():
    with open("data\\cities\\combined_v3.csv", "r") as file:
        data = read_csv(file)

    airports = data["ORIGIN"].unique()
    for airport in airports:
        filtered = data[data["ORIGIN"] == airport]
        result = filter_reasons(filtered)  # type: ignore
        pyplot.figure(figsize=(11, 8))
        plot = seaborn.barplot(x=list(result.keys()),
                               y=list(result.values()))
        plot.set_title(airport + " Delay Reasons 2019")
        plot.bar_label(plot.containers[0])
        pyplot.savefig("graphs\\DELAY_REASONS_" + airport + ".png")


main()

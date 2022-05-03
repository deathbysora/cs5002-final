import sys

import pandas
import seaborn
from matplotlib import pyplot


def show_graph(xlabel: str, ylabel: str, data: pandas.DataFrame) -> None:
    seaborn.set_palette(seaborn.color_palette("Spectral"))
    seaborn.scatterplot(x=xlabel, y=ylabel, data=data)
    pyplot.show()
    pyplot.clf()


def write_describe(xlabel: str, ylabel: str, data: pandas.DataFrame) -> None:
    series = data[xlabel]
    print(series.astype(float).describe())
    # collected = {
    #     "count": series.count(),
    #     "mean": series.mean(),
    #     "min": series.min(),
    #     "std": series.std(),
    #     "25%": series.quantile(0.25),
    #     "50%": series.quantile(0.50),
    #     "75%": series.quantile(0.75),
    #     "max": series.max()
    # }

    # print(xlabel)
    # for label, value in collected.items():
    #     print(f"{label}: {value}")


def main():
    try:
        command = sys.argv[1]
    except IndexError:
        print("Please include a command when calling this script.")
        return

    xlabels = [
        "ORIGIN_WIND_SPEED",
        "ORIGIN_VISIBILITIES",
        "DEST_WIND_SPEED",
        "DEST_VISIBILITIES",
    ]

    ylabels = [
        "DEP_DELAY",
        "ARR_DELAY",
    ]

    commands = {
        "show": show_graph,
        "describe": write_describe,
    }

    path = "data\\weather.csv"
    data = pandas.read_csv(path)
    for x in xlabels:
        for y in ylabels:
            commands[command](x, y, data)


if __name__ == "__main__":
    main()

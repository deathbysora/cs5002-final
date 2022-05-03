import pandas
import seaborn
from matplotlib import pyplot


def boxplot_data(xcolumn: str, ycolumn: str) -> None:
    path = "data\\"
    data = pandas.read_csv(path + "weather.csv")
    destination_path = "graphs\\"
    file_path = destination_path + xcolumn + "x" + ycolumn

    lbound = data[ycolumn].quantile(0.05)
    ubound = data[ycolumn].quantile(0.95)

    data = data[(data[ycolumn] > lbound) & (data[ycolumn] < ubound)]

    seaborn.set_palette(seaborn.color_palette("Spectral"))
    seaborn.boxplot(x=xcolumn, y=ycolumn, data=data)
    pyplot.show()
    # pyplot.savefig(file_path + ".png")
    pyplot.clf()

    # airports = data[xcolumn].unique()
    # with open(file_path + ".txt", "w") as file:
    #     # for airport in airports:
    #     # filtered = data[data[xcolumn] == airport]
    #     series = data[ycolumn]

    #     file.write("combined" + "\n")
    #     file.write("-" * 10 + "\n")

    #     collected = {
    #         "count": series.count(),
    #         "mean": series.mean(),
    #         "min": series.min(),
    #         "std": series.std(),
    #         "25%": series.quantile(0.25),
    #         "50%": series.quantile(0.50),
    #         "75%": series.quantile(0.75),
    #         "max": series.max()
    #     }

    #     for label, value in collected.items():
    #         file.write(f"{label}: {value}\n")
    #     file.write("\n\n")

    print(f"Box plot saved to {file_path}")


def main():
    xs = [
        "ORIGIN",
        "DEST",
    ]

    ys = [
        "DEP_DELAY",
        "ARR_DELAY",
    ]

    for x in xs:
        for y in ys:
            boxplot_data(x, y)


if __name__ == "__main__":
    main()

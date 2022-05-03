import seaborn
from matplotlib import pyplot
from pandas import read_csv


def main():
    with open("data\\cities\\combined_v3.csv", "r") as file:
        data = read_csv(file)

    ykey = "DEP_DELAY"
    xkey = "ORIGIN"

    file_name = "".join(["graphs\\", ykey, "x", xkey])
    stream = open(file_name + ".txt", "w")
    stream.write(f"{ykey} statistis for each airport\n")
    stream.write(f"y = {ykey}\n")
    stream.write(f"x = {xkey}\n")
    stream.write("\n")

    pyplot.figure(figsize=(11, 8))
    plot = seaborn.boxplot(x=xkey, y=ykey, data=data)
    plot.set_title(xkey + " 2019")

    pyplot.savefig(file_name + ".png")

    airports = data[xkey].unique()
    for airport in airports:
        filtered = data[data[xkey] == airport]
        series = filtered[ykey]

        stream.write(airport + "\n")
        stream.write("-" * 10 + "\n")

        collected = {
            "count": series.count(),
            "mean": series.mean(),
            "min": series.min(),
            "std": series.std(),
            "25%": series.quantile(0.25),
            "50%": series.quantile(0.50),
            "75%": series.quantile(0.75),
            "max": series.max()
        }

        for label, value in collected.items():
            stream.write(f"{label}: {round(value, 3)}\n")
        stream.write("\n\n")


main()
